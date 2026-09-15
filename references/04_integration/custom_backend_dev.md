# 泛微OA (E-Cology 9) 后端 Java 二次开发实战指南

在泛微 OA（Ecology 9）项目中，除了通过 HTTP REST API 与外部系统交互外，很多业务场景需要在 OA 系统内部编写 Java 扩展代码。本文档归纳了泛微 OA 最常用的后端核心二次开发规范与实战模版。

---

## 1. 流程自定义 Action 开发 (`Action`)

### 1.1 应用场景
- 流程节点前附加操作、节点后附加操作、出口附加操作。
- 业务数据校验（如校验预算金额、校验库存，不满足时阻断流转并弹出提示）。
- 流程审批通过后自动向第三方系统（ERP、MES、CRM、SAP）同步数据或回写业务表。

### 1.2 接口规范
实现泛微标准接口 `weaver.interfaces.workflow.action.Action`：

```java
package com.custom.workflow.action;

import weaver.general.BaseBean;
import weaver.general.Util;
import weaver.interfaces.workflow.action.Action;
import weaver.soa.workflow.request.Cell;
import weaver.soa.workflow.request.DetailTable;
import weaver.soa.workflow.request.Property;
import weaver.soa.workflow.request.RequestInfo;
import weaver.soa.workflow.request.Row;

import java.util.HashMap;
import java.util.Map;

/**
 * 泛微E9 流程自定义Action示例
 */
public class SampleWorkflowAction extends BaseBean implements Action {

    @Override
    public String execute(RequestInfo requestInfo) {
        String requestId = requestInfo.getRequestid();
        String workflowId = requestInfo.getWorkflowid();
        String src = requestInfo.getRequestManager().getSrc(); // 提交类型: submit, save, reject
        
        writeLog("===> SampleWorkflowAction 触发, RequestID=" + requestId + ", WorkflowID=" + workflowId + ", Src=" + src);

        try {
            // 1. 获取主表字段数据
            Map<String, String> mainData = new HashMap<>();
            Property[] properties = requestInfo.getMainTableInfo().getProperty();
            if (properties != null) {
                for (Property prop : properties) {
                    mainData.put(prop.getName().toLowerCase(), Util.null2String(prop.getValue()));
                }
            }

            String applicant = mainData.get("sqr"); // 申请人ID
            String amountStr = mainData.get("sqje"); // 申请金额
            double amount = Util.getDoubleValue(amountStr, 0.0);

            writeLog("流程主表数据: 申请人=" + applicant + ", 申请金额=" + amount);

            // 2. 获取明细表数据 (明细表1)
            DetailTable[] detailTables = requestInfo.getDetailTableInfo().getDetailTable();
            if (detailTables != null && detailTables.length > 0) {
                DetailTable dt1 = detailTables[0];
                Row[] rows = dt1.getRow();
                if (rows != null) {
                    for (int i = 0; i < rows.length; i++) {
                        Row row = rows[i];
                        Cell[] cells = row.getCell();
                        for (Cell cell : cells) {
                            writeLog("明细1 第" + (i + 1) + "行 字段=" + cell.getName() + ", 值=" + cell.getValue());
                        }
                    }
                }
            }

            // 3. 业务校验逻辑与阻断流转示例
            if (amount <= 0) {
                // 阻断流转并向前台抛出错误提示信息
                requestInfo.getRequestManager().setMessageid("111111");
                requestInfo.getRequestManager().setMessagecontent("【系统校验拦截】申请金额必须大于0元，无法提交！");
                return Action.FAILURE_AND_CONTINUE; // 或 return "0";
            }

            // 4. 调用外部系统或执行本地业务更新
            // ...

            return Action.SUCCESS; // 成功返回 "1"
        } catch (Exception e) {
            writeLog("SampleWorkflowAction 执行发生异常: " + e.getMessage());
            requestInfo.getRequestManager().setMessageid("999999");
            requestInfo.getRequestManager().setMessagecontent("【后台异常】" + e.getMessage());
            return Action.FAILURE_AND_CONTINUE;
        }
    }
}
```

### 1.3 后台配置路径
1. 将编译后的 `.class` 文件或 `.jar` 放置在 OA 服务器 `weaver/ecology/classbean/` 或 `WEB-INF/lib/` 目录下。
2. 登录 OA 后台：`集成中心 -> 流程流转集成 -> 动作集成`，新建动作集成，填入完整的类路径（如 `com.custom.workflow.action.SampleWorkflowAction`）。
3. 进入 `流程引擎 -> 路径管理 -> 流程流转设置`，在对应节点的【节点前/节点后附加操作】中勾选并绑定该 Action。

---

## 2. 数据库访问与事务管理 (`RecordSet` / `RecordSetTrans`)

泛微 Ecology 封装了高效安全的数据库访问工具类 `weaver.conn.RecordSet`。

### 2.1 常规 SQL 执行与防 SQL 注入
```java
import weaver.conn.RecordSet;
import weaver.general.Util;

public class DbHelper {
    public void queryUserData(String departmentId) {
        RecordSet rs = new RecordSet();
        // 推荐使用参数化查询，杜绝SQL注入
        String sql = "SELECT id, lastname, workcode, mobile, email, status FROM HrmResource WHERE departmentid = ? AND status IN (0, 1, 2, 3)";
        rs.executeQuery(sql, departmentId);

        while (rs.next()) {
            String id = Util.null2String(rs.getString("id"));
            String name = Util.null2String(rs.getString("lastname"));
            String workcode = Util.null2String(rs.getString("workcode"));
            String mobile = Util.null2String(rs.getString("mobile"));
            System.out.println("员工: " + id + " - " + name + " (" + workcode + ")");
        }
    }

    public boolean updateUserInfo(String userId, String mobile) {
        RecordSet rs = new RecordSet();
        String sql = "UPDATE HrmResource SET mobile = ? WHERE id = ?";
        return rs.executeUpdate(sql, mobile, userId);
    }
}
```

### 2.2 编程式事务处理 (`RecordSetTrans`)
对于跨表操作或需要保证原子性的业务操作，使用 `RecordSetTrans`：

```java
import weaver.conn.RecordSetTrans;

public class TransactionDemo {
    public boolean executeBusiness(String billId, double amount, String operator) {
        RecordSetTrans rst = new RecordSetTrans();
        rst.setAutoCommit(false); // 开启事务

        try {
            // 步骤1：插入主表记录
            String sql1 = "INSERT INTO uf_custom_order (billid, total_amount, creater, createdate) VALUES (?, ?, ?, ?)";
            rst.executeUpdate(sql1, billId, amount, operator, "2026-08-14");

            // 步骤2：更新台账扣减
            String sql2 = "UPDATE uf_budget SET used_amount = used_amount + ? WHERE billid = ?";
            rst.executeUpdate(sql2, amount, billId);

            rst.commit(); // 提交事务
            return true;
        } catch (Exception e) {
            rst.rollback(); // 异常回滚
            e.printStackTrace();
            return false;
        }
    }
}
```

---

## 3. 定时调度任务开发 (`BaseCronJob`)

### 3.1 实现代码
继承泛微基类 `weaver.interfaces.schedule.BaseCronJob`：

```java
package com.custom.schedule;

import weaver.general.BaseBean;
import weaver.interfaces.schedule.BaseCronJob;

/**
 * 泛微OA 定时同步任务
 */
public class SyncOrganizationCronJob extends BaseCronJob {
    
    private BaseBean log = new BaseBean();

    @Override
    public void execute() {
        log.writeLog("===> 定时任务 SyncOrganizationCronJob 开始执行...");
        try {
            // 执行业务同步逻辑，如拉取HR系统人员并更新Ecology
            long start = System.currentTimeMillis();
            doSync();
            log.writeLog("===> 定时任务执行完毕，耗时: " + (System.currentTimeMillis() - start) + "ms");
        } catch (Exception e) {
            log.writeLog("SyncOrganizationCronJob 执行异常: " + e.getMessage());
        }
    }

    private void doSync() {
        // 同步逻辑实现
    }
}
```

### 3.2 后台配置
1. 后台路径：`集成中心 -> 计划任务 -> 计划任务管理`。
2. 新增计划任务，填写 **任务标识**、**完整类名**（如 `com.custom.schedule.SyncOrganizationCronJob`）、**Cron 表达式**（如 `0 0 2 * * ?` 每天凌晨2点执行）。

---

## 4. 自定义 RESTful WebService 开发 (JAX-RS)

在泛微 E9 中暴露自定义 RESTful 服务：

```java
package com.custom.api.rest;

import com.alibaba.fastjson.JSONObject;
import weaver.general.BaseBean;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;

@Path("/custom/integration")
public class CustomIntegrationRestService extends BaseBean {

    @GET
    @Path("/health")
    @Produces(MediaType.APPLICATION_JSON)
    public String healthCheck() {
        JSONObject res = new JSONObject();
        res.put("status", "1");
        res.put("message", "Custom REST service is running healthy.");
        return res.toJSONString();
    }

    @POST
    @Path("/syncOrder")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public String syncOrder(String requestBody, @Context HttpServletRequest request, @Context HttpServletResponse response) {
        writeLog("收到自定义REST请求: " + requestBody);
        
        JSONObject result = new JSONObject();
        try {
            JSONObject body = JSONObject.parseObject(requestBody);
            String orderNo = body.getString("orderNo");
            
            // 业务处理...
            
            result.put("status", "1");
            result.put("msg", "订单 " + orderNo + " 同步成功");
            result.put("code", 200);
        } catch (Exception e) {
            result.put("status", "0");
            result.put("msg", "处理失败: " + e.getMessage());
            result.put("code", 500);
        }
        return result.toJSONString();
    }
}
```

---

## 5. 常用数据字典与核心系统表对照

| 模块 | 核心数据库表名 | 用途说明 |
| :--- | :--- | :--- |
| **人力资源** | `HrmResource` | 员工主表（包含工号、姓名、部门、分部、状态、手机号、账号等） |
| **人力资源** | `HrmDepartment` | 部门信息表（部门编码、名称、上级部门、所属分部等） |
| **人力资源** | `HrmSubCompany` | 分部/公司信息表 |
| **人力资源** | `HrmJobTitles` | 岗位信息表 |
| **工作流** | `workflow_requestbase` | 流程请求主表（包含 requestid, workflowid, requestname, status, creater, createdate 等） |
| **工作流** | `workflow_base` | 流程定义主表（流程名称、所属表单 formid、类型等） |
| **工作流** | `workflow_currentoperator` | 流程当前操作人/待办表（包含 requestid, userid, isremark, isprocessed 等） |
| **工作流** | `workflow_requestLog` | 流程流转签字意见日志表 |
| **知识文档** | `DocDetail` | 文档主信息表（docid, docsubject, seccategory, doccreaterid 等） |
| **知识文档** | `DocImageFile` | 文档与附件关联表 |
| **知识文档** | `ImageFile` | 实际物理附件存储信息表（imagefileid, imagefilename, filerealpath 等） |
| **表单建模** | `modeinfo` | 建模模块主表 |
| **表单建模** | `workflow_bill` | 系统与自定义单据表定义主表 |
| **系统矩阵** | `Matrixtable` / `Matrixfield` | 自定义矩阵数据表与字段配置 |

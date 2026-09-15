# 泛微OA (E-Cology) WebService (SOAP) 接口开发规范与指南

泛微 OA 除了提供 RESTful API 外，长期以来广泛采用基于 **SOAP / WSDL** 协议的 WebService 接口。无论是 E8 还是 E9，绝大多数企业老旧系统（SAP、ERP、MES、CRM）仍大量依赖 WebService 进行流程触发与文档归档。

---

## 1. 核心 WebService 接口服务清单

| 服务名称 | 服务用途 | WSDL 访问地址 |
| :--- | :--- | :--- |
| **`WorkflowService`** | 工作流核心服务（流程创建、流转、待办查询、表单数据读写） | `http://{OA_HOST}:{PORT}/services/WorkflowService?wsdl` |
| **`DocService`** | 知识文档服务（新建文档、绑定流程文档、上传 Base64 附件） | `http://{OA_HOST}:{PORT}/services/DocService?wsdl` |
| **`HrmService`** | 人力资源服务（人员同步、部门同步、分部查询、岗位职务） | `http://{OA_HOST}:{PORT}/services/HrmService?wsdl` |
| **`ModeDataService`** | 表单建模数据服务（建模数据 CRUD、权限控制） | `http://{OA_HOST}:{PORT}/services/ModeDataService?wsdl` |

---

## 2. 前置准备与 IP 白名单配置

调用 WebService 接口前，必须将调用方服务器 IP 加入白名单，否则调用时会直接报错 `2: 无权限调用此接口`。

- **配置文件路径**：`weaver/ecology/WEB-INF/prop/HrmWebserviceIP.properties`
- **配置内容示例**：
  ```properties
  # 允许调用 WebService 的 IP 列表（支持通配符或逗号分隔）
  HrmWebserviceIP = 127.0.0.1, 192.168.1.*, 10.0.0.15
  ```
- **重载方式**：修改保存后，进入后台 `集成中心 -> WebService 管理` 点击刷新，或重启服务。

---

## 3. WorkflowService 核心方法详解

### 3.1 创建流程实例 (`doCreateWorkflowRequest`)

#### 核心入参对象：`WorkflowRequestInfo`
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:webservices="http://webservices.workflow.weaver">
   <soapenv:Header/>
   <soapenv:Body>
      <webservices:doCreateWorkflowRequest>
         <webservices:in0>
            <!-- 流程创建人ID (HrmResource) -->
            <webservices:creatorId>1</webservices:creatorId>
            <!-- 流程请求标题 -->
            <webservices:requestName>采购申请流程-ERP自动同步</webservices:requestName>
            <!-- 流程等级：0-正常, 1-重要, 2-紧急 -->
            <webservices:requestLevel>0</webservices:requestLevel>
            <webservices:workflowBaseInfo>
               <!-- 流程定义ID (workflow_base 表中的 id) -->
               <webservices:workflowId>105</webservices:workflowId>
            </webservices:workflowBaseInfo>
            <!-- 流程主表表单数据 -->
            <webservices:workflowMainTableInfo>
               <webservices:requestProperties>
                  <webservices:workflowRequestTableField>
                     <webservices:fieldName>sqr</webservices:fieldName>
                     <webservices:fieldValue>1</webservices:fieldValue>
                     <webservices:viewFlag>true</webservices:viewFlag>
                     <webservices:editFlag>true</webservices:editFlag>
                  </webservices:workflowRequestTableField>
                  <webservices:workflowRequestTableField>
                     <webservices:fieldName>sqje</webservices:fieldName>
                     <webservices:fieldValue>9980.00</webservices:fieldValue>
                     <webservices:viewFlag>true</webservices:viewFlag>
                     <webservices:editFlag>true</webservices:editFlag>
                  </webservices:workflowRequestTableField>
               </webservices:requestProperties>
            </webservices:workflowMainTableInfo>
            <!-- 流程明细表数据 (可选) -->
            <webservices:workflowDetailTableInfos>
               <webservices:workflowDetailTableInfo>
                  <webservices:workflowRequestTableRecords>
                     <webservices:workflowRequestTableRecord>
                        <webservices:workflowRequestTableFields>
                           <webservices:workflowRequestTableField>
                              <webservices:fieldName>wpmc</webservices:fieldName>
                              <webservices:fieldValue>Dell 服务器 R740</webservices:fieldValue>
                           </webservices:workflowRequestTableField>
                           <webservices:workflowRequestTableField>
                              <webservices:fieldName>sl</webservices:fieldName>
                              <webservices:fieldValue>2</webservices:fieldValue>
                           </webservices:workflowRequestTableField>
                        </webservices:workflowRequestTableFields>
                     </webservices:workflowRequestTableRecord>
                  </webservices:workflowRequestTableRecords>
               </webservices:workflowDetailTableInfo>
            </webservices:workflowDetailTableInfos>
         </webservices:in0>
         <!-- 当前操作人ID -->
         <webservices:in1>1</webservices:in1>
      </webservices:doCreateWorkflowRequest>
   </soapenv:Body>
</soapenv:Envelope>
```

#### 返回值说明
- 返回新建流程生成的 `requestId`（大于 0 的整数字符串，如 `"398210"`）。
- 若返回负数表示创建失败：
  - `-1`: 创建失败（参数不合法或流程定义不存在）
  - `-2`: 没有创建权限
  - `-3`: 表单字段必填校验未通过

---

## 4. DocService 创建文档与附件上传 (`createDoc`)

### 4.1 附件 Base64 结构规范
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:webservices="http://webservices.docs.weaver">
   <soapenv:Header/>
   <soapenv:Body>
      <webservices:createDoc>
         <webservices:in0>
            <webservices:docsubject>系统上线操作手册.pdf</webservices:docsubject>
            <webservices:doccontent><![CDATA[<p>附件为最新操作手册，请查收。</p>]]></webservices:doccontent>
            <webservices:seccategory>12</webservices:seccategory>
            <!-- 附件列表 -->
            <webservices:attachments>
               <webservices:DocAttachment>
                  <webservices:filename>系统操作手册.pdf</webservices:filename>
                  <!-- 文件的 Base64 字节流字符串 -->
                  <webservices:filecontent>JVBERi0xLjQKJSDl...==</webservices:filecontent>
                  <webservices:iszip>0</webservices:iszip>
               </webservices:DocAttachment>
            </webservices:attachments>
         </webservices:in0>
         <!-- 创建人ID -->
         <webservices:in1>1</webservices:in1>
      </webservices:createDoc>
   </soapenv:Body>
</soapenv:Envelope>
```

- 返回值：新建文档的 `docid`。

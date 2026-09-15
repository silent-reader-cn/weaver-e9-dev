package com.custom.workflow.action;

import weaver.conn.RecordSet;
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
 * 泛微 Ecology 9 流程节点自定义 Action 完整示范
 * 功能：
 * 1. 解析流程主表及明细表数据
 * 2. 校验业务合规性，如果不符合则拦截流转并向前端提示错误
 * 3. 校验通过后，使用 RecordSet 更新外部台账表
 */
public class CustomWorkflowAction extends BaseBean implements Action {

    @Override
    public String execute(RequestInfo requestInfo) {
        String requestId = requestInfo.getRequestid();
        String workflowId = requestInfo.getWorkflowid();
        String src = requestInfo.getRequestManager().getSrc();

        writeLog("====== [CustomWorkflowAction] 触发 ======");
        writeLog("RequestID: " + requestId + ", WorkflowID: " + workflowId + ", 操作类型 Src: " + src);

        try {
            // 1. 读取流程主表数据
            Map<String, String> mainData = new HashMap<>();
            Property[] properties = requestInfo.getMainTableInfo().getProperty();
            if (properties != null) {
                for (Property prop : properties) {
                    mainData.put(prop.getName().toLowerCase(), Util.null2String(prop.getValue()));
                }
            }

            String applicant = mainData.get("sqr");     // 申请人ID (HrmResource)
            String totalAmountStr = mainData.get("sqje"); // 申请总金额
            String projectCode = mainData.get("xmbh");  // 项目编号

            double totalAmount = Util.getDoubleValue(totalAmountStr, 0.0);
            writeLog("主表解析: 申请人=" + applicant + ", 申请总金额=" + totalAmount + ", 项目编号=" + projectCode);

            // 2. 业务校验：金额必须大于0
            if (totalAmount <= 0) {
                // 阻断流转并弹出提示
                requestInfo.getRequestManager().setMessageid("ERR_AMOUNT_INVALID");
                requestInfo.getRequestManager().setMessagecontent("【流程提交拦截】申请总金额必须大于 0 元！");
                return Action.FAILURE_AND_CONTINUE;
            }

            // 3. 读取明细表1数据 (明细行循环)
            DetailTable[] detailTables = requestInfo.getDetailTableInfo().getDetailTable();
            if (detailTables != null && detailTables.length > 0) {
                DetailTable dt1 = detailTables[0];
                Row[] rows = dt1.getRow();
                if (rows != null) {
                    for (int i = 0; i < rows.length; i++) {
                        Row row = rows[i];
                        Map<String, String> rowData = new HashMap<>();
                        for (Cell cell : row.getCell()) {
                            rowData.put(cell.getName().toLowerCase(), Util.null2String(cell.getValue()));
                        }
                        String itemName = rowData.get("mc");
                        String itemAmount = rowData.get("je");
                        writeLog("明细行 [" + (i + 1) + "]: 费用项目=" + itemName + ", 金额=" + itemAmount);
                    }
                }
            }

            // 4. 数据库操作：更新自定义台账状态
            RecordSet rs = new RecordSet();
            String updateSql = "UPDATE uf_project_ledger SET status = '1', last_requestid = ? WHERE project_code = ?";
            boolean success = rs.executeUpdate(updateSql, requestId, projectCode);
            if (!success) {
                writeLog("台账更新失败: " + projectCode);
            }

            writeLog("====== [CustomWorkflowAction] 执行成功 ======");
            return Action.SUCCESS; // 返回 "1" 代表执行成功，流程继续流转

        } catch (Exception e) {
            writeLog("CustomWorkflowAction 发生未捕获异常: " + e.getMessage());
            requestInfo.getRequestManager().setMessageid("ERR_SYSTEM_EXCEPTION");
            requestInfo.getRequestManager().setMessagecontent("【系统错误】节点后附加操作异常: " + e.getMessage());
            return Action.FAILURE_AND_CONTINUE;
        }
    }
}

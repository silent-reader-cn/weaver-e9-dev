package com.custom.hrm.sync;

import weaver.conn.RecordSet;
import weaver.general.BaseBean;
import weaver.general.Util;

import java.util.Map;

/**
 * 泛微 Ecology 9 组织架构与人员数据同步服务实现
 */
public class OrganizationSyncService extends BaseBean {

    /**
     * 同步或创建部门信息
     */
    public String syncDepartment(String deptCode, String deptName, String supDeptId, String subCompanyId) {
        RecordSet rs = new RecordSet();
        String sql = "SELECT id FROM HrmDepartment WHERE departmentcode = ?";
        rs.executeQuery(sql, deptCode);

        if (rs.next()) {
            String deptId = rs.getString("id");
            String updateSql = "UPDATE HrmDepartment SET departmentname = ?, supdepid = ?, subcompanyid1 = ? WHERE id = ?";
            rs.executeUpdate(updateSql, deptName, Util.null2String(supDeptId), Util.null2String(subCompanyId), deptId);
            writeLog("更新部门成功: ID=" + deptId + ", Name=" + deptName);
            return deptId;
        } else {
            String insertSql = "INSERT INTO HrmDepartment (departmentname, departmentcode, supdepid, subcompanyid1, canceled) VALUES (?, ?, ?, ?, '0')";
            rs.executeUpdate(insertSql, deptName, deptCode, Util.null2String(supDeptId), Util.null2String(subCompanyId));
            
            RecordSet queryNew = new RecordSet();
            queryNew.executeQuery("SELECT id FROM HrmDepartment WHERE departmentcode = ?", deptCode);
            if (queryNew.next()) {
                String newId = queryNew.getString("id");
                writeLog("新建部门成功: ID=" + newId + ", Name=" + deptName);
                return newId;
            }
        }
        return null;
    }

    /**
     * 同步或创建人员信息
     */
    public boolean syncUser(Map<String, String> userInfo) {
        String workcode = userInfo.get("workcode");
        String name = userInfo.get("lastname");
        String loginid = userInfo.get("loginid");
        String deptId = userInfo.get("departmentid");
        String subcompanyId = userInfo.get("subcompanyid1");
        String mobile = userInfo.get("mobile");
        String email = userInfo.get("email");
        String status = userInfo.getOrDefault("status", "1"); // 1为正式员工

        if (Util.null2String(workcode).isEmpty() || Util.null2String(name).isEmpty()) {
            writeLog("工号或姓名为空，跳过同步");
            return false;
        }

        RecordSet rs = new RecordSet();
        rs.executeQuery("SELECT id FROM HrmResource WHERE workcode = ?", workcode);

        if (rs.next()) {
            String userId = rs.getString("id");
            String updateSql = "UPDATE HrmResource SET lastname = ?, loginid = ?, departmentid = ?, subcompanyid1 = ?, mobile = ?, email = ?, status = ? WHERE id = ?";
            boolean ok = rs.executeUpdate(updateSql, name, loginid, deptId, subcompanyId, mobile, email, status, userId);
            writeLog("更新员工 [" + workcode + "] " + name + (ok ? " 成功" : " 失败"));
            return ok;
        } else {
            String insertSql = "INSERT INTO HrmResource (workcode, lastname, loginid, departmentid, subcompanyid1, mobile, email, status, seclevel) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 10)";
            boolean ok = rs.executeUpdate(insertSql, workcode, name, loginid, deptId, subcompanyId, mobile, email, status);
            writeLog("新增员工 [" + workcode + "] " + name + (ok ? " 成功" : " 失败"));
            return ok;
        }
    }
}

package com.custom.api.rest;

import com.alibaba.fastjson.JSONObject;
import weaver.conn.RecordSet;
import weaver.general.BaseBean;
import weaver.general.Util;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;

/**
 * 泛微 Ecology 9 自定义 JAX-RS RESTful API 接口
 * 访问路径: http://oa-server/rest/custom/service/...
 */
@Path("/custom/service")
public class CustomRestService extends BaseBean {

    /**
     * 服务健康检查
     */
    @GET
    @Path("/ping")
    @Produces(MediaType.APPLICATION_JSON)
    public String ping() {
        JSONObject res = new JSONObject();
        res.put("code", 200);
        res.put("status", "1");
        res.put("message", "Ecology custom service is active.");
        res.put("serverTime", System.currentTimeMillis());
        return res.toJSONString();
    }

    /**
     * 根据工号查询员工详情
     */
    @GET
    @Path("/getUserByWorkcode")
    @Produces(MediaType.APPLICATION_JSON)
    public String getUserByWorkcode(@QueryParam("workcode") String workcode) {
        JSONObject result = new JSONObject();
        if (Util.null2String(workcode).isEmpty()) {
            result.put("status", "0");
            result.put("msg", "工号参数不能为空");
            return result.toJSONString();
        }

        RecordSet rs = new RecordSet();
        String sql = "SELECT id, lastname, workcode, departmentid, subcompanyid1, jobtitle, mobile, email, status " +
                     "FROM HrmResource WHERE workcode = ?";
        rs.executeQuery(sql, workcode);

        if (rs.next()) {
            JSONObject userObj = new JSONObject();
            userObj.put("id", rs.getString("id"));
            userObj.put("name", rs.getString("lastname"));
            userObj.put("workcode", rs.getString("workcode"));
            userObj.put("deptId", rs.getString("departmentid"));
            userObj.put("subcompanyId", rs.getString("subcompanyid1"));
            userObj.put("mobile", rs.getString("mobile"));
            userObj.put("email", rs.getString("email"));
            userObj.put("status", rs.getString("status"));

            result.put("status", "1");
            result.put("data", userObj);
            result.put("msg", "查询成功");
        } else {
            result.put("status", "0");
            result.put("msg", "未找到工号为 " + workcode + " 的员工信息");
        }

        return result.toJSONString();
    }

    /**
     * 接收外部系统推送的业务数据
     */
    @POST
    @Path("/receiveData")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public String receiveData(String body, @Context HttpServletRequest request, @Context HttpServletResponse response) {
        JSONObject resp = new JSONObject();
        writeLog("收到外部数据推送: " + body);

        try {
            JSONObject json = JSONObject.parseObject(body);
            String billCode = json.getString("billCode");
            String remark = json.getString("remark");

            // 保存到建模表
            RecordSet rs = new RecordSet();
            String sql = "INSERT INTO uf_thirdparty_data (billcode, remark, createdate) VALUES (?, ?, ?)";
            rs.executeUpdate(sql, billCode, remark, weaver.general.TimeUtil.getCurrentTimeString());

            resp.put("status", "1");
            resp.put("msg", "数据接收并保存成功");
            resp.put("billCode", billCode);
        } catch (Exception e) {
            writeLog("处理外部数据异常: " + e.getMessage());
            resp.put("status", "0");
            resp.put("msg", "处理失败: " + e.getMessage());
        }

        return resp.toJSONString();
    }
}

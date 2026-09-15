# 泛微OA 数据表: `workplanrevisionlog`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanrevisionlog`
- **字段总数**: `54`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | ID |
| 2 | `groupid` | 目标计划组id | `integer` | - | 是 | 目标计划组id |
| 3 | `type_n` | 工作计划类型 | `char` | 1 | 是 | 0：工作安排；1：会议日程；2：项目日程；3：客户联系；4：个人便签；6：目标计划 |
| 4 | `name` | 计划名称 | `varchar2` | 1000 | 是 | 计划名称 |
| 5 | `objid` | 计划负责单位id | `integer` | - | 是 | 计划负责单位id |
| 6 | `resourceid` | 计划接收人id | `varchar2` | 1000 | 是 | 计划接收人id |
| 7 | `oppositegoal` | 对应目标id | `integer` | - | 是 | 对应目标id |
| 8 | `begindate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 9 | `planproperty` | 计划性质 | `integer` | - | 是 | 计划性质 |
| 10 | `principal` | 负责人 | `varchar2` | 1000 | 是 | 负责人 |
| 11 | `cowork` | 协作人 | `varchar2` | 1000 | 是 | 协作人 |
| 12 | `upprincipal` | 上游 | `varchar2` | 1000 | 是 | 上游 |
| 13 | `downprincipal` | 下游 | `varchar2` | 1000 | 是 | 下游 |
| 14 | `teamrequest` | 协作请求 | `clob` | 4000 | 是 | 协作请求 |
| 15 | `begintime` | 开始时间 | `char` | 8 | 是 | 开始时间 |
| 16 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 17 | `endtime` | 结束时间 | `char` | 8 | 是 | 结束时间 |
| 18 | `rbegindate` | 实际开始日期 | `char` | 10 | 是 | 实际开始日期 |
| 19 | `renddate` | 实际结束日期 | `char` | 10 | 是 | 实际结束日期 |
| 20 | `rbegintime` | 实际开始时间 | `char` | 8 | 是 | 实际开始时间 |
| 21 | `rendtime` | 实际结束时间 | `char` | 8 | 是 | 实际结束时间 |
| 22 | `cycle` | 周期 | `char` | 1 | 是 | 周期 |
| 23 | `plantype` | 计划类型 | `char` | 1 | 是 | 计划类型 |
| 24 | `percent_n` | 权重 | `varchar2` | 40 | 是 | 权重 |
| 25 | `color` | 颜色 | `char` | 6 | 是 | 颜色 |
| 26 | `description` | 描述 | `clob` | 4000 | 是 | 描述 |
| 27 | `requestidn` | 审批流程 | `integer` | - | 是 | 审批流程 |
| 28 | `requestid` | 相关流程 | `varchar2` | 1000 | 是 | 相关流程 |
| 29 | `projectid` | 相关项目 | `varchar2` | 1000 | 是 | 相关项目 |
| 30 | `crmid` | 相关客户 | `varchar2` | 1000 | 是 | 相关客户 |
| 31 | `docid` | 相关文档 | `varchar2` | 1000 | 是 | 相关文档 |
| 32 | `meetingid` | 相关会议 | `varchar2` | 800 | 是 | 相关会议 |
| 33 | `status` | 状态 | `char` | 1 | 是 | 状态 |
| 34 | `isremind` | 是否提醒 | `integer` | - | 是 | 是否提醒 |
| 35 | `waketime` | 提醒时间 | `integer` | - | 是 | 单位：天 |
| 36 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 37 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 38 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |
| 39 | `deleted` | 是否删除 | `char` | 1 | 是 | 是否删除 |
| 40 | `taskid` | 相关项目任务 | `varchar2` | 1000 | 是 | 相关项目任务 |
| 41 | `urgentlevel` | 紧急度 | `char` | 1 | 是 | 紧急度 |
| 42 | `agentid` | 代理人 | `integer` | - | 是 | 代理人 |
| 43 | `deptid` | 部门id | `integer` | - | 是 | 部门id |
| 44 | `subcompanyid` | 分公司id | `integer` | - | 是 | 分公司id |
| 45 | `creatertype` | 创建者类型 | `char` | 1 | 是 | 创建者类型 |
| 46 | `finishremind` | 结束提醒 | `integer` | - | 是 | 结束提醒 |
| 47 | `relatedprj` | 相关项目 | `varchar2` | 1000 | 是 | 相关项目 |
| 48 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | 相关客户 |
| 49 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | 相关流程 |
| 50 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | 相关文档 |
| 51 | `allshare` | 共享给所有人 | `char` | 1 | 是 | 共享给所有人 |
| 52 | `plandate` | 目标计划日期 | `varchar2` | 160 | 是 | 目标计划日期 |
| 53 | `modifystatus` | 修改状态 | `char` | 1 | 是 | 修改状态 |
| 54 | `modifyuser` | 修改人 | `integer` | - | 是 | 修改人 |

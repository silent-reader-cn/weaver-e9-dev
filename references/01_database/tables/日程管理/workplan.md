# 泛微OA 数据表: `workplan`

- **所属模块**: `日程管理`
- **数据库表名**: `workplan`
- **字段总数**: `72`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键id |
| 2 | `deleted` | 是否删除 | `char` | 1 | 是 | 是否删除 |
| 3 | `urgentlevel` | 紧急度 | `char` | 1 | 是 | 紧急度 |
| 4 | `agentid` | 代理人 | `integer` | - | 是 | 代理人 |
| 5 | `deptid` | 部门ID | `integer` | - | 是 | 部门ID |
| 6 | `subcompanyid` | 分公司ID | `integer` | - | 是 | 分公司ID |
| 7 | `name` | 计划名称 | `varchar2` | 1000 | 是 | 计划名称 |
| 8 | `creatertype` | 创建人类型 | `char` | 1 | 是 | 创建人类型 |
| 9 | `finishremind` | 结束提醒 | `integer` | - | 是 | 结束提醒 |
| 10 | `relatedprj` | 相关项目 | `varchar2` | 1000 | 是 | 相关项目 |
| 11 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | 相关客户 |
| 12 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | 相关流程 |
| 13 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | 相关文档 |
| 14 | `taskid` | 相关项目任务 | `varchar2` | 1000 | 是 | 相关项目任务 |
| 15 | `groupid` | 计划组ID | `integer` | - | 是 | 计划组ID |
| 16 | `objid` | 计划所有者对象 | `integer` | - | 是 | 计划所有者对象 |
| 17 | `oppositegoal` | 计划对应目标 | `integer` | - | 是 | 计划对应目标 |
| 18 | `planproperty` | 日程属性 | `integer` | - | 是 | 日程属性 |
| 19 | `principal` | 计划负责人 | `varchar2` | 4000 | 是 | 计划负责人 |
| 20 | `cowork` | 协作人 | `varchar2` | 1000 | 是 | 协作人 |
| 21 | `upprincipal` | 上游负责人 | `varchar2` | 1000 | 是 | 上游负责人 |
| 22 | `downprincipal` | 下游负责人 | `varchar2` | 1000 | 是 | 下游负责人 |
| 23 | `teamrequest` | 计划相关交流 | `varchar2` | 1000 | 是 | 计划相关交流 |
| 24 | `rbegindate` | 预期开始日期 | `char` | 10 | 是 | 预期开始日期 |
| 25 | `renddate` | 预期结束日期 | `char` | 10 | 是 | 预期结束日期 |
| 26 | `rbegintime` | 预期开始时间 | `char` | 8 | 是 | 预期开始时间 |
| 27 | `rendtime` | 预期结束时间 | `char` | 8 | 是 | 预期结束时间 |
| 28 | `cycle` | 周期 | `char` | 1 | 是 | 周期 |
| 29 | `plantype` | 计划的类型 | `char` | 1 | 是 | 计划的类型 |
| 30 | `percent_n` | 计划的比重 | `integer` | - | 是 | 计划的比重 |
| 31 | `requestidn` | 相关请求 | `integer` | - | 是 | 相关请求 |
| 32 | `allshare` | 是否共享所有人 | `char` | 1 | 是 | 是否共享所有人 |
| 33 | `plandate` | 计划的日期 | `varchar2` | 160 | 是 | 是否共享所有人 |
| 34 | `modifystatus` | 变更状态 | `char` | 1 | 是 | 计划的日期 |
| 35 | `modifyuser` | 变更人 | `integer` | - | 是 | 变更状态 |
| 36 | `remindtype` | 提醒方式 | `varchar2` | 1000 | 是 | 变更人 |
| 37 | `remindtimesbeforestart` | 开始前提醒时间数 | `integer` | - | 是 | 提醒方式 |
| 38 | `remindtimesbeforeend` | 结束前提醒时间数 | `integer` | - | 是 | 开始前提醒时间数 |
| 39 | `remindbeforestart` | 开始前提醒 | `char` | 1 | 是 | 结束前提醒时间数 |
| 40 | `remindbeforeend` | 结束前提醒 | `char` | 1 | 是 | 开始前提醒 |
| 41 | `reminddatebeforestart` | 开始前提醒日期 | `char` | 10 | 是 | 结束前提醒 |
| 42 | `remindtimebeforestart` | 开始前提醒时间 | `char` | 8 | 是 | 开始前提醒日期 |
| 43 | `reminddatebeforeend` | 结束前提醒日期 | `char` | 10 | 是 | 开始前提醒时间 |
| 44 | `remindtimebeforeend` | 结束前提醒时间 | `char` | 8 | 是 | 结束前提醒时间 |
| 45 | `hrmperformancecheckdetailid` | 自定义考核叶子节点ID | `integer` | - | 是 | 自定义考核叶子节点ID |
| 46 | `type_n` | 工作计划类型 | `integer` | - | 是 | 0：工作安排；1：会议日程；2：项目日程；3：客户联系；4：个人便签；6：目标计划 |
| 47 | `resourceidold` | 旧的接收人id | `varchar2` | 4000 | 是 | 旧的接收人id |
| 48 | `hasremindedbeforestart` | 是否已经开始前提醒 | `char` | 1 | 是 | 1：是 0或其它：否 |
| 49 | `hasremindedbeforeend` | 是否已经结束前提醒 | `char` | 1 | 是 | 1：是 0或其它：否 |
| 50 | `location` | 地图位置 | `varchar2` | 800 | 是 | 地图位置 |
| 51 | `sellchanceid` | 商机id | `integer` | - | 是 | 商机id,客户模块用 |
| 52 | `contacterid` | 合同id | `integer` | - | 是 | 合同id,客户模块用 |
| 53 | `fileid` | 文件id | `varchar2` | 2000 | 是 | 文件id，客户模块用 |
| 54 | `attachs` | 日程详情附件 | `varchar2` | 1000 | 是 | 日程详情附件 |
| 55 | `resourceid` | 计划接收人id | `clob` | 4000 | 是 | 计划接收人id |
| 56 | `begindate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 57 | `begintime` | 开始时间 | `char` | 8 | 是 | 开始时间 |
| 58 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 59 | `endtime` | 结束时间 | `char` | 8 | 是 | 结束时间 |
| 60 | `color` | 颜色 | `char` | 6 | 是 | 日程显示控件中的颜色 |
| 61 | `description` | 计划内容 | `varchar2` | 4000 | 是 | 计划内容 |
| 62 | `requestid` | 相关流程 | `varchar2` | 1000 | 是 | 相关流程 |
| 63 | `projectid` | 相关项目 | `varchar2` | 1000 | 是 | 相关项目 |
| 64 | `crmid` | 相关客户 | `varchar2` | 500 | 是 | 相关客户 |
| 65 | `docid` | 相关文档 | `varchar2` | 1000 | 是 | 相关文档 |
| 66 | `meetingid` | 会议id | `varchar2` | 800 | 是 | 会议日程对应的会议id |
| 67 | `status` | 状态 | `char` | 1 | 是 | 0：代办；1：完成；2、归档 |
| 68 | `isremind` | 是否提醒 | `integer` | - | 是 | 是否提醒 |
| 69 | `waketime` | 提醒时间 | `integer` | - | 是 | 单位：天 |
| 70 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 71 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 72 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |

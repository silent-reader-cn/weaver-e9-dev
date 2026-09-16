# 泛微OA 数据表: `hrmperformanceplanmodul`

- **中文名称**: 人力资源计划工作模板表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceplanmodul`
- **主键**: `id`
- **字段数**: `72`

> 说明：人力资源计划工作模板表, 周期日程数据

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `principal` | 负责人 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `ruletag` | 规则标记 | `integer` | - | 否 | 否 | 否 | - | 0 | 0 原来的规则 1新的规则. 为了兼容老数据 |
| 3 | `ruleregex` | 重复规则 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `nextdate` | 下一个日期点 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 新规则下,下一个日期点 |
| 5 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `groupid` | 分组id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 7 | `type_n` | 类型 | `char` | 1 | 是 | 否 | 否 | - | - | 目标计划：6 工作安排：0 |
| 8 | `name` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `objid` | 对象id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 10 | `resourceid` | 人员id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `oppositegoal` | oppositegoal | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 12 | `begindate` | 开始时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 13 | `planproperty` | 计划属性 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 14 | `principalold` | oppositegoal | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 15 | `cowork` | cowork | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `upprincipal` | upprincipal | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `downprincipal` | downprincipal | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `teamrequest` | teamrequest | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `begintime` | 开始时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 20 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `endtime` | 结束时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 22 | `rbegindate` | rbegindate | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 23 | `renddate` | renddate | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 24 | `rbegintime` | rbegintime | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 25 | `rendtime` | rendtime | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 26 | `cycle` | 定期模式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 27 | `plantype` | 计划所属类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 28 | `percent_n` | 上级名称 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 29 | `color` | 颜色 | `char` | 6 | 是 | 否 | 否 | - | - | - |
| 30 | `description` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 31 | `requestidn` | requestidn | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 32 | `requestid` | 相关流程 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 33 | `projectid` | 相关项目 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 34 | `crmid` | 相关客户 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 35 | `docid` | 相关文档 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 36 | `meetingid` | 相关会议 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 37 | `status` | 状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 38 | `isremind` | 是否提醒 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 39 | `waketime` | 提醒时间 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 40 | `createrid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 41 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 42 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 43 | `deleted` | 删除标记 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 44 | `taskid` | 任务id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 45 | `urgentlevel` | 所属等级 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 46 | `agentid` | agentid | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 47 | `deptid` | 部门id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 48 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 49 | `creatertype` | 创建类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 50 | `finishremind` | 是否已经提醒 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 51 | `relatedprj` | relatedprj | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 52 | `relatedcus` | relatedcus | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 53 | `relatedwf` | relatedwf | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 54 | `relateddoc` | relateddoc | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 55 | `allshare` | allshare | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 56 | `plandate` | 计划日期 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 57 | `timemodul` | 定期模式 | `char` | 1 | 是 | 否 | 否 | - | - | 0,1,2&nbsp; 周月年 |
| 58 | `frequency` | 重复规则(老) | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 59 | `frequencyy` | 重复规则(老) | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 60 | `workplantypeid` | 工作计划类型id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 61 | `createtype` | 创建时间 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 62 | `workplancreatetime` | 工作计划创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 63 | `persistenttype` | 持续方式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 64 | `persistenttimes` | 持续时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 65 | `availablebegindate` | 有效期开始时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 66 | `availableenddate` | 有效期截止时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 67 | `remindbeforestart` | 是否开始前提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 68 | `remindbeforeend` | 是否结束前提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 69 | `remindtype` | 提醒方式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 70 | `remindtimesbeforestart` | 开始前提醒时间 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 71 | `remindtimesbeforeend` | 结束前提醒时间 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 72 | `immediatetouch` | 是否立即触发 | `integer` | - | 是 | 否 | 否 | - | 0 | 1为触发 |

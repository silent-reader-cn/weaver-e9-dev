# 泛微OA 数据表: `hrmperformanceplanmodul`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceplanmodul`
- **字段总数**: `72`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `principal` | 负责人 | `clob` | 4000 | 是 | - |
| 2 | `ruletag` | 规则标记 | `integer` | - | 否 | 0  原来的规则  1新的规则.  为了兼容老数据 |
| 3 | `ruleregex` | 重复规则 | `varchar2` | 1000 | 是 | - |
| 4 | `nextdate` | 下一个日期点 | `varchar2` | 80 | 是 | 新规则下,下一个日期点 |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `groupid` | 分组id | `integer` | - | 是 | - |
| 7 | `type_n` | 类型 | `char` | 1 | 是 | 目标计划：6 工作安排：0 |
| 8 | `name` | 名称 | `varchar2` | 1000 | 是 | - |
| 9 | `objid` | 对象id | `integer` | - | 是 | - |
| 10 | `resourceid` | 人员id | `varchar2` | 1000 | 是 | - |
| 11 | `oppositegoal` | oppositegoal | `integer` | - | 是 | - |
| 12 | `begindate` | 开始时间 | `char` | 10 | 是 | - |
| 13 | `planproperty` | 计划属性 | `integer` | - | 是 | - |
| 14 | `principalold` | oppositegoal | `varchar2` | 4000 | 是 | - |
| 15 | `cowork` | cowork | `varchar2` | 1000 | 是 | - |
| 16 | `upprincipal` | upprincipal | `varchar2` | 1000 | 是 | - |
| 17 | `downprincipal` | downprincipal | `varchar2` | 1000 | 是 | - |
| 18 | `teamrequest` | teamrequest | `varchar2` | 4000 | 是 | - |
| 19 | `begintime` | 开始时间 | `char` | 8 | 是 | - |
| 20 | `enddate` | 结束日期 | `char` | 10 | 是 | - |
| 21 | `endtime` | 结束时间 | `char` | 8 | 是 | - |
| 22 | `rbegindate` | rbegindate | `char` | 10 | 是 | - |
| 23 | `renddate` | renddate | `char` | 10 | 是 | - |
| 24 | `rbegintime` | rbegintime | `char` | 8 | 是 | - |
| 25 | `rendtime` | rendtime | `char` | 8 | 是 | - |
| 26 | `cycle` | 定期模式 | `char` | 1 | 是 | - |
| 27 | `plantype` | 计划所属类型 | `char` | 1 | 是 | - |
| 28 | `percent_n` | 上级名称 | `integer` | - | 是 | - |
| 29 | `color` | 颜色 | `char` | 6 | 是 | - |
| 30 | `description` | 描述 | `varchar2` | 4000 | 是 | - |
| 31 | `requestidn` | requestidn | `integer` | - | 是 | - |
| 32 | `requestid` | 相关流程 | `varchar2` | 800 | 是 | - |
| 33 | `projectid` | 相关项目 | `varchar2` | 800 | 是 | - |
| 34 | `crmid` | 相关客户 | `varchar2` | 800 | 是 | - |
| 35 | `docid` | 相关文档 | `varchar2` | 800 | 是 | - |
| 36 | `meetingid` | 相关会议 | `varchar2` | 800 | 是 | - |
| 37 | `status` | 状态 | `char` | 1 | 是 | - |
| 38 | `isremind` | 是否提醒 | `integer` | - | 是 | - |
| 39 | `waketime` | 提醒时间 | `integer` | - | 是 | - |
| 40 | `createrid` | 创建人id | `integer` | - | 是 | - |
| 41 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 42 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 43 | `deleted` | 删除标记 | `char` | 1 | 是 | - |
| 44 | `taskid` | 任务id | `integer` | - | 是 | - |
| 45 | `urgentlevel` | 所属等级 | `char` | 1 | 是 | - |
| 46 | `agentid` | agentid | `integer` | - | 是 | - |
| 47 | `deptid` | 部门id | `integer` | - | 是 | - |
| 48 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 49 | `creatertype` | 创建类型 | `char` | 1 | 是 | - |
| 50 | `finishremind` | 是否已经提醒 | `integer` | - | 是 | - |
| 51 | `relatedprj` | relatedprj | `varchar2` | 1000 | 是 | - |
| 52 | `relatedcus` | relatedcus | `varchar2` | 1000 | 是 | - |
| 53 | `relatedwf` | relatedwf | `varchar2` | 1000 | 是 | - |
| 54 | `relateddoc` | relateddoc | `varchar2` | 1000 | 是 | - |
| 55 | `allshare` | allshare | `char` | 1 | 是 | - |
| 56 | `plandate` | 计划日期 | `varchar2` | 160 | 是 | - |
| 57 | `timemodul` | 定期模式 | `char` | 1 | 是 | 0,1,2&nbsp; 周月年 |
| 58 | `frequency` | 重复规则(老) | `integer` | - | 是 | - |
| 59 | `frequencyy` | 重复规则(老) | `integer` | - | 是 | - |
| 60 | `workplantypeid` | 工作计划类型id | `integer` | - | 是 | - |
| 61 | `createtype` | 创建时间 | `char` | 1 | 是 | - |
| 62 | `workplancreatetime` | 工作计划创建时间 | `char` | 8 | 是 | - |
| 63 | `persistenttype` | 持续方式 | `char` | 1 | 是 | - |
| 64 | `persistenttimes` | 持续时间 | `varchar2` | 80 | 是 | - |
| 65 | `availablebegindate` | 有效期开始时间 | `char` | 10 | 是 | - |
| 66 | `availableenddate` | 有效期截止时间 | `char` | 10 | 是 | - |
| 67 | `remindbeforestart` | 是否开始前提醒 | `char` | 1 | 是 | - |
| 68 | `remindbeforeend` | 是否结束前提醒 | `char` | 1 | 是 | - |
| 69 | `remindtype` | 提醒方式 | `char` | 1 | 是 | - |
| 70 | `remindtimesbeforestart` | 开始前提醒时间 | `integer` | - | 是 | - |
| 71 | `remindtimesbeforeend` | 结束前提醒时间 | `integer` | - | 是 | - |
| 72 | `immediatetouch` | 是否立即触发 | `integer` | - | 是 | 1为触发 |

# 泛微OA 数据表: `voting`

- **中文名称**: 调查主表
- **所属模块**: `网上调查`
- **数据库表名**: `voting`
- **主键**: `id`
- **字段数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 主键id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 3 | `subject` | 主题 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `detail` | 废弃字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 废弃字段 |
| 5 | `createrid` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 8 | `approverid` | 触发审批流id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `approvedate` | 审批日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 10 | `approvetime` | 审批时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 11 | `begindate` | 开始日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `begintime` | 开始时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 13 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `endtime` | 结束时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `isanony` | 是否匿名 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 16 | `docid` | 相关文档 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `crmid` | 相关客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `projid` | 相关项目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `requestid` | 相关流程 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `votingcount` | 投票数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 0未开始 1正常 |
| 22 | `isseeresult` | 投票后查看结果 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 0不可查看 1可查看 |
| 23 | `votingtype` | 调查类型 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 24 | `descr` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `deploytype` | 发布类型 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 26 | `autoshowvote` | 自动弹出调查 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 27 | `votetimecontrol` | 调查时间控制 | `varchar2` | 40 | 是 | 否 | 否 | - | - | 废弃 |
| 28 | `votetimecontroltime` | 调查时间控制的时间 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 废弃 |
| 29 | `forcevote` | 强制调查 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 30 | `remindtype` | 提醒类型 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 31 | `remindtimebeforestart` | 开始前提醒时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 32 | `remindtimebeforeend` | 结束前提醒时间 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 33 | `hasremindedbeforestart` | 提醒开始时间设置 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 34 | `hasremindedbeforeend` | 提醒结束时间控制 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |
| 35 | `istemplate` | 是否是模板 | `varchar2` | 40 | 是 | 否 | 否 | - | - | - |

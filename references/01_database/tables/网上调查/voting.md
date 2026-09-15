# 泛微OA 数据表: `voting`

- **所属模块**: `网上调查`
- **数据库表名**: `voting`
- **字段总数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 2 | `id` | 主键id | `integer` | - | 否 | - |
| 3 | `subject` | 主题 | `varchar2` | 800 | 是 | - |
| 4 | `detail` | 废弃字段 | `varchar2` | 4000 | 是 | 废弃字段 |
| 5 | `createrid` | 创建人 | `integer` | - | 是 | - |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 7 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 8 | `approverid` | 触发审批流id | `integer` | - | 是 | - |
| 9 | `approvedate` | 审批日期 | `char` | 10 | 是 | - |
| 10 | `approvetime` | 审批时间 | `char` | 8 | 是 | - |
| 11 | `begindate` | 开始日期 | `char` | 10 | 是 | - |
| 12 | `begintime` | 开始时间 | `char` | 8 | 是 | - |
| 13 | `enddate` | 结束日期 | `char` | 10 | 是 | - |
| 14 | `endtime` | 结束时间 | `char` | 8 | 是 | - |
| 15 | `isanony` | 是否匿名 | `varchar2` | 40 | 是 | - |
| 16 | `docid` | 相关文档 | `integer` | - | 是 | - |
| 17 | `crmid` | 相关客户 | `integer` | - | 是 | - |
| 18 | `projid` | 相关项目 | `integer` | - | 是 | - |
| 19 | `requestid` | 相关流程 | `integer` | - | 是 | - |
| 20 | `votingcount` | 投票数 | `integer` | - | 是 | - |
| 21 | `status` | 状态 | `integer` | - | 是 | 0未开始 1正常 |
| 22 | `isseeresult` | 投票后查看结果 | `varchar2` | 80 | 是 | 0不可查看 1可查看 |
| 23 | `votingtype` | 调查类型 | `integer` | - | 是 | - |
| 24 | `descr` | 描述 | `varchar2` | 1000 | 是 | - |
| 25 | `deploytype` | 发布类型 | `varchar2` | 40 | 是 | - |
| 26 | `autoshowvote` | 自动弹出调查 | `varchar2` | 40 | 是 | - |
| 27 | `votetimecontrol` | 调查时间控制 | `varchar2` | 40 | 是 | 废弃 |
| 28 | `votetimecontroltime` | 调查时间控制的时间 | `varchar2` | 800 | 是 | 废弃 |
| 29 | `forcevote` | 强制调查 | `varchar2` | 40 | 是 | - |
| 30 | `remindtype` | 提醒类型 | `varchar2` | 40 | 是 | - |
| 31 | `remindtimebeforestart` | 开始前提醒时间 | `varchar2` | 400 | 是 | - |
| 32 | `remindtimebeforeend` | 结束前提醒时间 | `varchar2` | 400 | 是 | - |
| 33 | `hasremindedbeforestart` | 提醒开始时间设置 | `varchar2` | 40 | 是 | - |
| 34 | `hasremindedbeforeend` | 提醒结束时间控制 | `varchar2` | 40 | 是 | - |
| 35 | `istemplate` | 是否是模板 | `varchar2` | 40 | 是 | - |

# 泛微OA 数据表: `crm_contactlog`

- **中文名称**: 客户联系日志
- **所属模块**: `客户管理`
- **数据库表名**: `crm_contactlog`
- **主键**: `id`
- **字段数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 2 | `customerid` | 客户id | `integer` | - | 是 | 否 | 否 | - | - | 客户id |
| 3 | `contacterid` | 联系人id | `integer` | - | 是 | 否 | 否 | - | - | 联系人id |
| 4 | `resourceid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 5 | `contactway` | 联系方式id | `integer` | - | 是 | 否 | 否 | - | - | 联系方式id |
| 6 | `ispassive` | 是否客户主动 | `integer` | - | 是 | 否 | 否 | - | - | 是否客户主动 |
| 7 | `subject` | 标题 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 标题 |
| 8 | `contacttype` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | 1-常规2-业务相关3-客户埋怨 |
| 9 | `contactdate` | 联系日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | 联系日期 |
| 10 | `contacttime` | 联系时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | 联系时间 |
| 11 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 如出差上门服务等 |
| 12 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 结束时间 |
| 13 | `contactinfo` | 联系情况 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 联系情况 |
| 14 | `documentid` | 文档ID | `integer` | - | 是 | 否 | 否 | - | - | 文档ID |
| 15 | `submitdate` | 提交日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 提交日期 |
| 16 | `submittime` | 提交时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 提交时间 |
| 17 | `issublog` | 是否字批注 | `integer` | - | 是 | 否 | 否 | - | - | 是否字批注 |
| 18 | `parentid` | 所属批注的条目id | `integer` | - | 是 | 否 | 否 | - | - | 所属批注的条目id |
| 19 | `isprocessed` | 是否已存档 | `integer` | - | 是 | 否 | 否 | - | - | 是否已存档 |
| 20 | `processdate` | 联系情况处理日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 联系情况处理日期 |
| 21 | `processtime` | 联系情况处理时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 联系情况处理时间 |
| 22 | `isfinished` | 是否完成 | `integer` | - | 是 | 否 | 否 | - | - | 是否完成 |
| 23 | `agentid` | 代理商id | `integer` | - | 是 | 否 | 否 | - | - | 代理商id |

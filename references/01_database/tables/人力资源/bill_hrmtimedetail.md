# 泛微OA 数据表: `bill_hrmtimedetail`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmtimedetail`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | ID |
| 2 | `requestid` | 流程id | `integer` | - | 是 | 流程id |
| 3 | `name` | 说明 | `varchar2` | 1000 | 是 | 说明 |
| 4 | `resourceid` | 提交人 | `integer` | - | 是 | 提交人 |
| 5 | `accepterid` | 接收人 | `varchar2` | 1000 | 是 | 接收人 |
| 6 | `begindate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 7 | `begintime` | 开始时间 | `char` | 8 | 是 | 开始时间 |
| 8 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 9 | `endtime` | 结束时间 | `char` | 8 | 是 | 结束时间 |
| 10 | `wakedate` | 提醒日期 | `char` | 10 | 是 | 提醒日期 |
| 11 | `delaydate` | 完成时间 | `char` | 10 | 是 | 完成时间 |
| 12 | `crmid` | 相关客户 | `integer` | - | 是 | 相关客户 |
| 13 | `projectid` | 相关项目 | `integer` | - | 是 | 相关项目 |
| 14 | `relatedrequestid` | 关联流程id | `integer` | - | 是 | 关联流程id |
| 15 | `isopen` | 是否开启 | `integer` | - | 是 | 是否开启 |
| 16 | `remark` | 详细 | `varchar2` | 2000 | 是 | 详细 |
| 17 | `alldoc` | 相关文档 | `varchar2` | 1000 | 是 | 相关文档 |
| 18 | `requestlevel` | 流程级别 | `integer` | - | 是 | 流程级别 |

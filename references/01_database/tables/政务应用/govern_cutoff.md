# 泛微OA 数据表: `govern_cutoff`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_cutoff`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `taskid` | 办结任务id | `integer` | - | 是 | govern_task表 id字段 |
| 3 | `categoryid` | 督办类型id | `integer` | - | 是 | - |
| 4 | `requestid` | 流程requestid | `integer` | - | 是 | - |
| 5 | `cutdate` | 结束日期 | `varchar2` | 10 | 是 | - |
| 6 | `cuttime` | 结束时间 | `varchar2` | 8 | 是 | - |
| 7 | `applicant` | 申请人 | `integer` | - | 是 | - |
| 8 | `type` | 完结类型 | `integer` | - | 是 | 0：办结（通过流程结束的任务）1：完成 |

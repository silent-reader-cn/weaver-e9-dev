# 泛微OA 数据表: `govern_extension`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_extension`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `taskid` | 延期任务id | `integer` | - | 是 | govern_task表 id字段 |
| 3 | `categoryid` | 督办类型id | `integer` | - | 是 | - |
| 4 | `requestid` | 流程requestid | `integer` | - | 是 | - |
| 5 | `date1` | 延期前计划结束日期 | `varchar2` | 10 | 是 | - |
| 6 | `time1` | 延期前计划结束时间 | `varchar2` | 8 | 是 | - |
| 7 | `date2` | 延期后计划结束日期 | `varchar2` | 10 | 是 | - |
| 8 | `time2` | 延期后计划结束时间 | `varchar2` | 8 | 是 | - |
| 9 | `applicant` | 申请人 | `integer` | - | 是 | - |
| 10 | `appdept` | 申请人单位 | `integer` | - | 是 | - |
| 11 | `appdate` | 申请日期 | `varchar2` | 10 | 是 | - |
| 12 | `apptime` | 申请时间 | `varchar2` | 8 | 是 | - |
| 13 | `reason` | 延期原因 | `clob` | - | 是 | - |

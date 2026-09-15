# 泛微OA 数据表: `govern_operator`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_operator`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `taskid` | 任务id | `integer` | - | 否 | 对应govern_task表id |
| 3 | `projid` | 事项id | `integer` | - | 是 | 对应govern_task表id |
| 4 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 5 | `operatedate` | 创建（下发）日期 | `varchar2` | 10 | 是 | - |
| 6 | `operatetime` | 创建（下发）时间 | `varchar2` | 8 | 是 | - |
| 7 | `startdate` | 计划开始日期 | `varchar2` | 10 | 是 | - |
| 8 | `starttime` | 计划开始时间 | `varchar2` | 8 | 是 | - |
| 9 | `enddate` | 计划结束日期 | `varchar2` | 10 | 是 | - |
| 10 | `endtime` | 计划结束时间 | `varchar2` | 8 | 是 | - |
| 11 | `astartdate` | 实际开始日期 | `varchar2` | 10 | 是 | - |
| 12 | `astarttime` | 实际开始时间 | `varchar2` | 8 | 是 | - |
| 13 | `aenddate` | 实际结束日期 | `varchar2` | 10 | 是 | - |
| 14 | `aendtime` | 实际结束时间 | `varchar2` | 8 | 是 | - |
| 15 | `dealer` | 处理人 | `integer` | - | 是 | - |
| 16 | `status` | 状态 | `integer` | - | 是 | - |
| 17 | `dealtype` | 处理类型 | `integer` | - | 是 | 0主办、1协办 |
| 18 | `signdate` | 签收日期 | `varchar2` | 10 | 是 | - |
| 19 | `signtime` | 签收时间 | `varchar2` | 8 | 是 | - |
| 20 | `issign` | 是否签收 | `integer` | - | 是 | - |

# 泛微OA 数据表: `govern_operator`

- **中文名称**: 督查督办任务操作者表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_operator`
- **主键**: `id`
- **字段数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `taskid` | 任务id | `integer` | - | 否 | 否 | 否 | - | - | 对应govern_task表id |
| 3 | `projid` | 事项id | `integer` | - | 是 | 否 | 否 | - | - | 对应govern_task表id |
| 4 | `categoryid` | 类型id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `operatedate` | 创建（下发）日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 6 | `operatetime` | 创建（下发）时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 7 | `startdate` | 计划开始日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `starttime` | 计划开始时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 9 | `enddate` | 计划结束日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 10 | `endtime` | 计划结束时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 11 | `astartdate` | 实际开始日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `astarttime` | 实际开始时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 13 | `aenddate` | 实际结束日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `aendtime` | 实际结束时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 15 | `dealer` | 处理人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `dealtype` | 处理类型 | `integer` | - | 是 | 否 | 否 | - | - | 0主办、1协办 |
| 18 | `signdate` | 签收日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 19 | `signtime` | 签收时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 20 | `issign` | 是否签收 | `integer` | - | 是 | 否 | 否 | - | - | - |

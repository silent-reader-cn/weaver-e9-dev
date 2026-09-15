# 泛微OA 数据表: `task_log`

- **所属模块**: `项目管理`
- **数据库表名**: `task_log`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `projectid` | 项目id | `integer` | - | 是 | 项目id |
| 2 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 3 | `logtype` | 日志类型 | `char` | 2 | 是 | 日志类型 |
| 4 | `submitdate` | 提交日期 | `varchar2` | 80 | 是 | 提交日期 |
| 5 | `submittime` | 提交时间 | `varchar2` | 64 | 是 | 提交时间 |
| 6 | `submiter` | 提交人 | `integer` | - | 是 | 提交人 |
| 7 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |
| 8 | `submitertype` | 提交类型 | `integer` | - | 是 | 提交类型 |

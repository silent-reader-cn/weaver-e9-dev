# 泛微OA 数据表: `task_modify`

- **所属模块**: `项目管理`
- **数据库表名**: `task_modify`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `projectid` | 项目id | `integer` | - | 是 | 项目id |
| 2 | `taskid` | 任务id | `integer` | - | 是 | 任务id |
| 3 | `fieldname` | 字段名称 | `varchar2` | 800 | 是 | 字段名称 |
| 4 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 5 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
| 6 | `original` | 原值 | `varchar2` | 1000 | 是 | 原值 |
| 7 | `modified` | 新值 | `varchar2` | 1000 | 是 | 新值 |
| 8 | `modifier` | 修改者 | `integer` | - | 是 | 修改者 |
| 9 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |
| 10 | `submitertype` | 提交类型 | `integer` | - | 是 | 提交类型 |
| 11 | `logtype` | 日志类型 | `char` | 1 | 是 | 日志类型 |

# 泛微OA 数据表: `prj_log`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_log`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `projectid` | 项目id | `integer` | - | 是 | 项目id |
| 2 | `logtype` | 日志类型 | `char` | 2 | 是 | 日志类型 |
| 3 | `documentid` | 文档id | `integer` | - | 是 | 文档id |
| 4 | `logcontent` | 日志内容 | `varchar2` | 1000 | 是 | 日志内容 |
| 5 | `submitdate` | 提交日期 | `varchar2` | 10 | 是 | 提交日期 |
| 6 | `submittime` | 提交时间 | `varchar2` | 8 | 是 | 提交时间 |
| 7 | `submiter` | 提交者 | `integer` | - | 是 | 提交者 |
| 8 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |
| 9 | `submitertype` | 提交类型 | `integer` | - | 是 | 提交类型 |

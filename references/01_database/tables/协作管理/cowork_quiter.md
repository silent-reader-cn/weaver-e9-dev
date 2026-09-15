# 泛微OA 数据表: `cowork_quiter`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_quiter`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `itemid` | 协作id | `integer` | - | 是 | - |
| 3 | `userid` | 退出协作者 | `varchar2` | 176 | 是 | - |
| 4 | `quitdate` | 退出日期 | `char` | 10 | 是 | - |
| 5 | `quittime` | 退出时间 | `char` | 8 | 是 | - |
| 6 | `coworkothers` | 被提醒过人字段 | `varchar2` | 4000 | 是 | - |

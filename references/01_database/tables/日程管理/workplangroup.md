# 泛微OA 数据表: `workplangroup`

- **所属模块**: `日程管理`
- **数据库表名**: `workplangroup`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | 主键 |
| 2 | `planname` | 提醒内容 | `varchar2` | 800 | 是 | 提醒内容 |
| 3 | `cycle` | 提醒周期 | `char` | 1 | 是 | 提醒周期 |
| 4 | `plandate` | 当前计划时间 | `varchar2` | 400 | 是 | 当前计划时间 |
| 5 | `objid` | 操作者id | `integer` | - | 是 | 操作者的id |
| 6 | `status` | 状态 | `char` | 1 | 是 | 状态 |
| 7 | `type_d` | 操作者类型 | `char` | 1 | 是 | 操作者类型 |
| 8 | `requestid` | 请求id | `integer` | - | 是 | 请求的id |

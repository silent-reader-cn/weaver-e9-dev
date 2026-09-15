# 泛微OA 数据表: `workplanmonitor`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanmonitor`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workplanmonitorid` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `hrmid` | 日程创建人id | `integer` | - | 是 | 日程创建人id |
| 3 | `workplantypeid` | 日程类型id | `integer` | - | 是 | 日程类型id |
| 4 | `operatordate` | 最后更新日期 | `char` | 10 | 是 | 最后更新日期 |
| 5 | `operatortime` | 最后更新时间 | `char` | 8 | 是 | 最后更新时间 |

# 泛微OA 数据表: `workplanmonitor`

- **中文名称**: 日程监控表
- **所属模块**: `日程管理`
- **数据库表名**: `workplanmonitor`
- **主键**: `workplanmonitorid`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `workplanmonitorid` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 主键 |
| 2 | `hrmid` | 日程创建人id | `integer` | - | 是 | 否 | 否 | - | - | 日程创建人id |
| 3 | `workplantypeid` | 日程类型id | `integer` | - | 是 | 否 | 否 | - | - | 日程类型id |
| 4 | `operatordate` | 最后更新日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最后更新日期 |
| 5 | `operatortime` | 最后更新时间 | `char` | 8 | 是 | 否 | 否 | - | - | 最后更新时间 |

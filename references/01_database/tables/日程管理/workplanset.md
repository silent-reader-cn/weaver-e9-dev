# 泛微OA 数据表: `workplanset`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `viewtype` | 未知 | `integer` | - | 是 | 未知 |
| 2 | `weekstartday` | 日程日历，一览表 周开始第一天 | `integer` | - | 是 | 0：周日 1：周一 |
| 3 | `id` | ID | `integer` | - | 否 | id |
| 4 | `timerangestart` | 日历开始值 | `integer` | - | 是 | 默认0 |
| 5 | `timerangeend` | 日历结束值 | `integer` | - | 是 | 默认23 |
| 6 | `amandpm` | 是否拆分上下午 | `integer` | - | 是 | 0不拆分 1拆分 |
| 7 | `amstart` | 上午开始时间 | `varchar2` | 64 | 是 | 拆分上下午时有效 |
| 8 | `amend` | 上午结束时间拆分上下午时有效上午结束时间拆分上下午时有效 | `varchar2` | 64 | 是 | 上午结束时间拆分上下午时有效上午结束时间拆分上下午时有效 |
| 9 | `pmstart` | 下午开始时间 | `varchar2` | 64 | 是 | 拆分上下午时有效 |
| 10 | `pmend` | 下午结束时间 | `varchar2` | 64 | 是 | 拆分上下午时有效 |
| 11 | `datasplit` | 是否拆分数据 | `integer` | - | 是 | - |

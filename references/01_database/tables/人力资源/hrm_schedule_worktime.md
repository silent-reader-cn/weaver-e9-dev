# 泛微OA 数据表: `hrm_schedule_worktime`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_schedule_worktime`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `delflag` | delflag | `integer` | - | 否 | delflag |
| 3 | `creater` | 创建人 | `integer` | - | 否 | 创建人 |
| 4 | `create_time` | 创建时间 | `varchar2` | 100 | 否 | 创建时间 |
| 5 | `last_modifier` | 最后修改人 | `integer` | - | 否 | 最后修改人 |
| 6 | `last_modification_time` | 最后修改时间 | `varchar2` | 100 | 否 | 最后修改时间 |
| 7 | `field001` | 时段名称 | `varchar2` | 100 | 否 | 时段名称 |
| 8 | `field002` | 上班时间 | `varchar2` | 100 | 否 | 上班时间 |
| 9 | `field003` | 下班时间 | `varchar2` | 100 | 否 | 下班时间 |
| 10 | `field004` | 签到开始时间 | `integer` | - | 否 | 签到开始时间 |
| 11 | `field005` | 最晚签退时间 | `integer` | - | 否 | 最晚签退时间 |
| 12 | `field006` | 说明 | `varchar2` | 1000 | 是 | 说明 |
| 13 | `field007` | 工作小时数 | `number` | (5,1) | 否 | 工作小时数 |

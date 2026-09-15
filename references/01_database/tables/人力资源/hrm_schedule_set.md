# 泛微OA 数据表: `hrm_schedule_set`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_schedule_set`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `delflag` | delflag | `integer` | - | 否 | delflag |
| 3 | `creater` | 创建人 | `integer` | - | 否 | 创建人 |
| 4 | `create_time` | 创建时间 | `varchar2` | 100 | 否 | 创建时间 |
| 5 | `last_modifier` | 最后修改人 | `integer` | - | 否 | 最后修改人 |
| 6 | `last_modification_time` | 最后修改时间 | `varchar2` | 100 | 否 | 最后修改时间 |
| 7 | `sn` | 排序标识 | `integer` | - | 否 | 排序标识 |
| 8 | `field001` | 排班开始日期 | `varchar2` | 100 | 否 | 排班开始日期 |
| 9 | `field002` | 排班结束日期 | `varchar2` | 100 | 否 | 排班结束日期 |
| 10 | `field003` | 班次 | `integer` | - | 否 | 班次 |
| 11 | `field004` | 所属分部 | `integer` | - | 否 | 所属分部 |

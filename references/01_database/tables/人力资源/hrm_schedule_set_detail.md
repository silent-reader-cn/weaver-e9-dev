# 泛微OA 数据表: `hrm_schedule_set_detail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_schedule_set_detail`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `delflag` | delflag | `integer` | - | 否 | delflag |
| 3 | `field001` | 班次 | `varchar2` | 100 | 否 | 班次 |
| 4 | `field002` | 人员 | `integer` | - | 否 | 人员 |
| 5 | `field003` | 日期 | `varchar2` | 100 | 否 | 日期 |
| 6 | `field004` | 星期 | `integer` | - | 否 | 星期 |
| 7 | `field005` | 工作时间 | `varchar2` | 100 | 否 | 工作时间 |
| 8 | `setid` | 设置人 | `integer` | - | 是 | 设置人 |

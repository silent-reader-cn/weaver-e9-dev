# 泛微OA 数据表: `hrm_usb_auto_date`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_usb_auto_date`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `user_id` | 用户id | `integer` | - | 否 | 用户id |
| 3 | `need_auto` | 是否使用 | `integer` | - | 否 | 0未使用，1使用 |
| 4 | `enable_date` | 生效日期 | `varchar2` | 1000 | 是 | 生效日期 |
| 5 | `enable_usb_type` | usb类型 | `integer` | - | 否 | usb类型 |
| 6 | `delflag` | 是否删除 | `integer` | - | 否 | 1为删除 |

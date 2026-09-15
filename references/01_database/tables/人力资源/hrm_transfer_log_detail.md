# 泛微OA 数据表: `hrm_transfer_log_detail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_transfer_log_detail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `log_id` | 日志id | `integer` | - | 否 | 日志id |
| 3 | `code_name` | 权限代码 | `varchar2` | 400 | 是 | 权限代码 |
| 4 | `p_num` | 关联数量 | `integer` | - | 否 | 关联数量 |
| 5 | `is_all` | 是否所有 | `integer` | - | 否 | 是否所有 |
| 6 | `id_str` | id字符串 | `varchar2` | 4000 | 是 | id字符串 |
| 7 | `p_time` | 操作时间 | `integer` | - | 否 | 操作时间 |

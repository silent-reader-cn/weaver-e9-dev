# 泛微OA 数据表: `mobilemode_api_server_param`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemode_api_server_param`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 32 | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `position` | 参数位置 | `varchar2` | 400 | 是 | - |
| 4 | `front_parameter_id` | 对应前端参数 | `varchar2` | 256 | 是 | - |
| 5 | `api_id` | 接口ID | `varchar2` | 256 | 是 | 对应接口表id，外键 |
| 6 | `show_order` | 显示顺序 | `integer` | - | 是 | 显示顺序 |

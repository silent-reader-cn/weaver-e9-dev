# 泛微OA 数据表: `mobilemode_api_range`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemode_api_range`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 32 | 否 | - |
| 2 | `type` | 类型 | `varchar2` | 1000 | 是 | 类型 |
| 3 | `value` | 值 | `varchar2` | 1000 | 是 | 类型值 |
| 4 | `api_id` | 接口ID | `varchar2` | 256 | 是 | 对应接口表id，外键 |
| 5 | `show_order` | 显示顺序 | `integer` | - | 是 | 显示顺序 |

# 泛微OA 数据表: `mobilemode_api_front_param`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemode_api_front_param`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 32 | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `type` | 类型 | `varchar2` | 1000 | 是 | 类型 |
| 4 | `required` | 是否必填 | `varchar2` | 400 | 是 | 是否必填 |
| 5 | `default_value` | 默认值 | `varchar2` | 1000 | 是 | 默认值 |
| 6 | `remark` | 备注 | `varchar2` | 2000 | 是 | 备注 |
| 7 | `api_id` | 接口ID | `varchar2` | 256 | 是 | 对应接口表id，外键 |
| 8 | `show_order` | 显示顺序 | `integer` | - | 是 | 显示顺序 |

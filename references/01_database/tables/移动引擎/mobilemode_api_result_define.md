# 泛微OA 数据表: `mobilemode_api_result_define`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemode_api_result_define`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 32 | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `remark` | 备注 | `varchar2` | 2000 | 是 | 备注 |
| 4 | `type` | 类型 | `varchar2` | 1000 | 是 | 类型 |
| 5 | `api_id` | 接口ID | `varchar2` | 256 | 是 | 对应接口表id，外键 |
| 6 | `show_order` | 显示顺序 | `integer` | - | 是 | 显示顺序 |

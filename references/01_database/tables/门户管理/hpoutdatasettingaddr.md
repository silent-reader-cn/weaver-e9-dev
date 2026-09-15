# 泛微OA 数据表: `hpoutdatasettingaddr`

- **所属模块**: `门户管理`
- **数据库表名**: `hpoutdatasettingaddr`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `eid` | 元素id | `integer` | - | 否 | - |
| 3 | `tabid` | tab页id | `integer` | - | 是 | - |
| 4 | `sourceid` | 数据来源id | `integer` | - | 是 | - |
| 5 | `address` | 集成登录设置 | `varchar2` | 1000 | 是 | - |
| 6 | `pos` | 顺序 | `integer` | - | 是 | - |

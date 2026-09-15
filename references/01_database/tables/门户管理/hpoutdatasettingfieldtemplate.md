# 泛微OA 数据表: `hpoutdatasettingfieldtemplate`

- **所属模块**: `门户管理`
- **数据库表名**: `hpoutdatasettingfieldtemplate`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `eid` | 元素id | `integer` | - | 是 | - |
| 3 | `tabid` | tab页id | `integer` | - | 是 | - |
| 4 | `showfield` | 显示字段id | `varchar2` | 1000 | 是 | - |
| 5 | `showfieldname` | 显示字段名 | `varchar2` | 1000 | 是 | - |
| 6 | `isshowname` | 是否显示标题 | `char` | 50 | 是 | - |
| 7 | `transql` | 转换方法 | `varchar2` | 1000 | 是 | - |
| 8 | `mainid` | mainid | `integer` | - | 是 | - |

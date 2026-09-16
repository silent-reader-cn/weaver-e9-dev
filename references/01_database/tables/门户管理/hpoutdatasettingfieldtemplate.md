# 泛微OA 数据表: `hpoutdatasettingfieldtemplate`

- **中文名称**: 门户外部数据元素自定义方式显示字段配置信息模板表
- **所属模块**: `门户管理`
- **数据库表名**: `hpoutdatasettingfieldtemplate`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `eid` | 元素id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `tabid` | tab页id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `showfield` | 显示字段id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `showfieldname` | 显示字段名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `isshowname` | 是否显示标题 | `char` | 50 | 是 | 否 | 否 | - | - | - |
| 7 | `transql` | 转换方法 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `mainid` | mainid | `integer` | - | 是 | 否 | 否 | - | - | - |

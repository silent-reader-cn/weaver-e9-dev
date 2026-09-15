# 泛微OA 数据表: `mode_templateinfo`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_templateinfo`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `customid` | 查询页id | `integer` | - | 是 | 查询的id |
| 3 | `templatename` | 模板名称 | `varchar2` | 800 | 是 | 模板名称 |
| 4 | `templatetype` | 模板类型 | `char` | 1 | 是 | 模板类型 |
| 5 | `displayorder` | 排序 | `integer` | - | 是 | 用于查询模板排序 |
| 6 | `isdefault` | 是否默认 | `integer` | - | 是 | - |
| 7 | `createrid` | 创建者 | `integer` | - | 是 | 创建者 |
| 8 | `createdate` | 创建时间 | `varchar2` | 400 | 是 | 创建时间 |
| 9 | `sourcetype` | 来源类型 | `char` | 1 | 是 | 来源类型 |

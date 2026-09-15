# 泛微OA 数据表: `datasearchparam`

- **所属模块**: `集成模块`
- **数据库表名**: `datasearchparam`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 自增长主键 |
| 2 | `mainid` | 浏览框基本信息id | `integer` | - | 是 | 浏览框基本信息id |
| 3 | `fieldname` | 字段名称 | `varchar2` | 800 | 是 | 字段名称 |
| 4 | `searchname` | 查询字段显示名称 | `varchar2` | 800 | 是 | 查询字段显示名称 |
| 5 | `fieldtype` | 字段类型 | `char` | 1 | 是 | 字段类型1 数字；2 文本 |
| 6 | `wokflowfieldname` | 联动流程字段 | `varchar2` | 1000 | 是 | 联动流程字段 |

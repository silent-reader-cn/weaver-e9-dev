# 泛微OA 数据表: `docseccategorycussearch`

- **中文名称**: 文档目录自定义列表设置表
- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorycussearch`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `viewindex` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `visible` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `seccategoryid` | 文档目录id | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 5 | `docpropertyid` | 文档属性id | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 6 | `docseccategorytemplateid` | 文档目录模板id | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 7 | `iscond` | 是否查询条件 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 8 | `condcolumnwidth` | 查询条件宽度 | `integer` | - | 是 | 否 | 否 | - | 1 | 1：半行 2：整行 |

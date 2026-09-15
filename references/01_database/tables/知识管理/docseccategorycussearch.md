# 泛微OA 数据表: `docseccategorycussearch`

- **所属模块**: `知识管理`
- **数据库表名**: `docseccategorycussearch`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `viewindex` | 显示顺序 | `integer` | - | 是 | - |
| 3 | `visible` | 是否启用 | `integer` | - | 是 | - |
| 4 | `seccategoryid` | 文档目录id | `integer` | - | 否 | - |
| 5 | `docpropertyid` | 文档属性id | `integer` | - | 否 | - |
| 6 | `docseccategorytemplateid` | 文档目录模板id | `integer` | - | 否 | - |
| 7 | `iscond` | 是否查询条件 | `char` | 1 | 是 | - |
| 8 | `condcolumnwidth` | 查询条件宽度 | `integer` | - | 是 | 1：半行 2：整行 |

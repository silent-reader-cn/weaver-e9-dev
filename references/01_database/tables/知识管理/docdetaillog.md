# 泛微OA 数据表: `docdetaillog`

- **所属模块**: `知识管理`
- **数据库表名**: `docdetaillog`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `docsubject` | 文档主题 | `varchar2` | 1000 | 是 | - |
| 4 | `doccreater` | 文档创建者 | `integer` | - | 是 | - |
| 5 | `operatetype` | 操作的类型 | `varchar2` | 16 | 是 | - |

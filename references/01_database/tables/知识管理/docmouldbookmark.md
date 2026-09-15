# 泛微OA 数据表: `docmouldbookmark`

- **所属模块**: `知识管理`
- **数据库表名**: `docmouldbookmark`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `mouldid` | 模板id | `integer` | - | 是 | - |
| 4 | `bookmarkid` | 书签id | `integer` | - | 是 | - |
| 5 | `bookmarkvalue` | 书签值 | `varchar2` | 4000 | 是 | - |

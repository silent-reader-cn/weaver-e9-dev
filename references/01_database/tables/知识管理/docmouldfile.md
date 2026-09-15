# 泛微OA 数据表: `docmouldfile`

- **所属模块**: `知识管理`
- **数据库表名**: `docmouldfile`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 文档模板id | `integer` | - | 否 | - |
| 2 | `mouldname` | 文档模板描述 | `varchar2` | 1000 | 是 | - |
| 3 | `mouldtext` | 文档模板html | `clob` | 4000 | 是 | - |
| 4 | `mouldtype` | 模板文档类型 | `integer` | - | 是 | - |

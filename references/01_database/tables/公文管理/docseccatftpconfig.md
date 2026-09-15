# 泛微OA 数据表: `docseccatftpconfig`

- **所属模块**: `公文管理`
- **数据库表名**: `docseccatftpconfig`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 序号 |
| 2 | `seccategoryid` | 子目录id | `integer` | - | 是 | 子目录id |
| 3 | `isuseftp` | 是否启用 | `char` | 1 | 是 | 是否启用 1：是，0或其它为否 |
| 4 | `ftpconfigid` | ftp服务器配置id | `integer` | - | 是 | ftp服务器配置id |
| 5 | `refreshchildren` | 是否同步子目录 | `char` | 1 | 是 | 是否同步子目录 |

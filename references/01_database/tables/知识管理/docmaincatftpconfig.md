# 泛微OA 数据表: `docmaincatftpconfig`

- **所属模块**: `知识管理`
- **数据库表名**: `docmaincatftpconfig`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `maincategoryid` | 主目录id | `integer` | - | 是 | - |
| 3 | `refreshsubandsec` | 是否更新分目录和子目录设置 | `char` | 1 | 是 | 1：是，0或其它为 |
| 4 | `isuseftp` | 是否启用 | `char` | 1 | 是 | 1：是，0或其它为否 |
| 5 | `ftpconfigid` | ftp服务器配置id | `integer` | - | 是 | - |

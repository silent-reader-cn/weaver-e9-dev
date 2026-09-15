# 泛微OA 数据表: `docftpconfig`

- **所属模块**: `知识管理`
- **数据库表名**: `docftpconfig`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `ftpconfigname` | ftp服务器名称 | `varchar2` | 800 | 是 | - |
| 3 | `ftpconfigdesc` | ftp服务器描述 | `varchar2` | 1000 | 是 | - |
| 4 | `serverip` | ftp服务器地址 | `varchar2` | 1000 | 是 | - |
| 5 | `serverport` | ftp服务器端口号 | `varchar2` | 80 | 是 | - |
| 6 | `username` | ftp服务器用户名 | `varchar2` | 800 | 是 | - |
| 7 | `userpassword` | ftp服务器密码 | `varchar2` | 1000 | 是 | - |
| 8 | `defaultrootdir` | ftp服务器根目录 | `varchar2` | 1000 | 是 | - |
| 9 | `maxconncount` | ftp服务器最大连接数 | `integer` | - | 是 | - |
| 10 | `showorder` | 显示顺序 | `number` | (6,2) | 是 | - |

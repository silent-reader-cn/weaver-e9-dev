# 泛微OA 数据表: `docftpconfig`

- **中文名称**: FTP服务器设置表（E8已停用）
- **所属模块**: `知识管理`
- **数据库表名**: `docftpconfig`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `ftpconfigname` | ftp服务器名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 3 | `ftpconfigdesc` | ftp服务器描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `serverip` | ftp服务器地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `serverport` | ftp服务器端口号 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 6 | `username` | ftp服务器用户名 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 7 | `userpassword` | ftp服务器密码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `defaultrootdir` | ftp服务器根目录 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `maxconncount` | ftp服务器最大连接数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `showorder` | 显示顺序 | `number` | (6,2) | 是 | 否 | 否 | - | - | - |

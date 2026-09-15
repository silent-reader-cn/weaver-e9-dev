# 泛微OA 数据表: `docchangesetting`

- **所属模块**: `知识管理`
- **数据库表名**: `docchangesetting`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `autosend` | 是否自动发送 | `varchar2` | 8 | 是 | - |
| 2 | `autosendtime` | 自动发送间隔分钟 | `integer` | - | 是 | - |
| 3 | `autoreceive` | 是否自动发送 | `varchar2` | 8 | 是 | - |
| 4 | `autoreceivetime` | 自动接收间隔分钟 | `integer` | - | 是 | - |
| 5 | `serverurl` | FTP服务器地址 | `varchar2` | 1000 | 是 | - |
| 6 | `serverport` | FTP服务器端口 | `integer` | - | 是 | - |
| 7 | `serveruser` | FTP服务器用户名 | `varchar2` | 400 | 是 | - |
| 8 | `serverpwd` | FTP服务器密码 | `varchar2` | 800 | 是 | - |
| 9 | `changemode` | 交换方式 | `varchar2` | 8 | 是 | - |
| 10 | `pathcategory` | 文件目录 | `varchar2` | 1000 | 是 | - |
| 11 | `maincategory` | 主目录 | `integer` | - | 是 | - |
| 12 | `subcategory` | 子目录 | `integer` | - | 是 | - |
| 13 | `seccategory` | 二级目录 | `integer` | - | 是 | - |
| 14 | `ws_platform_url` | WebService地址 | `varchar2` | 1000 | 是 | - |
| 15 | `ws_loginid` | WebService登录名 | `varchar2` | 800 | 是 | - |
| 16 | `ws_password` | WebService登录密码 | `varchar2` | 1000 | 是 | - |
| 17 | `ws_access_syscode` | WebService访问编码 | `varchar2` | 800 | 是 | - |
| 18 | `ws_access_sysname` | WebService系统名称 | `varchar2` | 1000 | 是 | - |
| 19 | `ws_access_sysdesc` | WebService系统描述 | `varchar2` | 2000 | 是 | - |

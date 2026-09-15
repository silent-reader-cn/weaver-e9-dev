# 泛微OA 数据表: `exp_ftpdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_ftpdetail`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `name` | ftp方案名称 | `varchar2` | 1000 | 是 | - |
| 3 | `adress` | ftp服务器地址 | `varchar2` | 1000 | 是 | - |
| 4 | `port` | ftp端口 | `varchar2` | 160 | 是 | - |
| 5 | `path` | 文件保存路径 | `varchar2` | 800 | 是 | - |
| 6 | `ftpuser` | ftp登录帐号 | `varchar2` | 800 | 是 | - |
| 7 | `ftppwd` | ftp登录密码 | `varchar2` | 800 | 是 | - |
| 8 | `createdate` | 方案创建日期 | `varchar2` | 160 | 是 | - |
| 9 | `creator` | 方案创建人 | `integer` | - | 是 | - |

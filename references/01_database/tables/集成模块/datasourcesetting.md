# 泛微OA 数据表: `datasourcesetting`

- **所属模块**: `集成模块`
- **数据库表名**: `datasourcesetting`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `usepool` | 是否使用连接池 | `integer` | - | 是 | 是否使用连接池；0：不使用；1：使用。 |
| 2 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 3 | `pointid` | 数据源名称 | `varchar2` | 1000 | 是 | 数据源名称 |
| 4 | `classpath` | 数据源类路径 | `varchar2` | 1000 | 是 | 数据源类路径 |
| 5 | `type` | 数据库类型 | `varchar2` | 400 | 是 | 数据库类型 |
| 6 | `datasourcename` | 数据源名称 | `varchar2` | 1000 | 是 | 数据源名称 |
| 7 | `iscluster` | 是否集群 | `char` | 1 | 是 | 是否集群；0：否；1：是 |
| 8 | `typename` | 数据库类型 | `varchar2` | 1000 | 是 | 数据库类型 |
| 9 | `url` | 连接字段串 | `varchar2` | 2000 | 是 | 连接字段串 |
| 10 | `host` | 数据库地址 | `varchar2` | 1000 | 是 | 数据库地址 |
| 11 | `dbname` | 数据库名称 | `varchar2` | 1000 | 是 | 数据库名称 |
| 12 | `username` | 用户名 | `varchar2` | 1000 | 是 | 用户名 |
| 13 | `password` | 密码 | `varchar2` | 1000 | 是 | 密码 |
| 14 | `minconn` | 最小连接数 | `integer` | - | 是 | 最小连接数 |
| 15 | `maxconn` | 最大连接数 | `integer` | - | 是 | 最大连接数 |
| 16 | `iscode` | 是否加密 | `char` | 1 | 是 | 是否加密 |
| 17 | `sortid` | 排序号 | `integer` | - | 是 | 排序号；程序会自动算出最大值。 |
| 18 | `port` | 端口号 | `varchar2` | 1000 | 是 | 端口号 |

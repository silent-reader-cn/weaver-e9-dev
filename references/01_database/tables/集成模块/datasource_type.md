# 泛微OA 数据表: `datasource_type`

- **所属模块**: `集成模块`
- **数据库表名**: `datasource_type`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `dbtype` | 数据库类型 | `varchar2` | 400 | 是 | 数据库类型 |
| 3 | `dbname` | 数据库名称 | `varchar2` | 800 | 是 | 数据库名称 |
| 4 | `driverclass` | 数据库驱动程序 | `varchar2` | 1000 | 是 | 数据库驱动程序 |
| 5 | `driverurl` | 数据库驱动连接字符串 | `varchar2` | 1000 | 是 | 数据库驱动连接字符串 |
| 6 | `cancluster` | 是否允许集群 | `integer` | - | 是 | 是否允许集群 |
| 7 | `driverlevel` | 驱动级别 | `integer` | - | 是 | 驱动级别 |
| 8 | `sortid` | 排序号 | `integer` | - | 是 | 排序号 |
| 9 | `driverfilename` | 数据库驱动文件名 | `varchar2` | 1000 | 是 | 数据库驱动文件名 |
| 10 | `realname` | 真实名称 | `varchar2` | 1000 | 是 | 真实名称 |

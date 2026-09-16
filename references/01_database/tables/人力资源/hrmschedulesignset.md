# 泛微OA 数据表: `hrmschedulesignset`

- **中文名称**: 人力资源考勤自动同步设置表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmschedulesignset`
- **主键**: `datasourceid`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `datasourceid` | 来源id | `varchar2` | 50 | 否 | 否 | 否 | - | - | 来源id |
| 2 | `importtype` | 导入类型 | `char` | 1 | 是 | 否 | 否 | - | - | 导入类型 |
| 3 | `tablename` | 数据表名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 数据表名称 |
| 4 | `workcode` | 编号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 编号 |
| 5 | `lastname` | 用户名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 用户名 |
| 6 | `usertype` | 用户类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 用户类型 |
| 7 | `signtype` | 同步方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 同步方式 |
| 8 | `signdate` | 同步日期 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 同步日期 |
| 9 | `signtime` | 同步时间 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 同步时间 |
| 10 | `clientaddress` | 客户端地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 客户端地址 |
| 11 | `isincom` | isincom | `varchar2` | 1000 | 是 | 否 | 否 | - | - | isincom |

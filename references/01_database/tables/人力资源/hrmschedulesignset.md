# 泛微OA 数据表: `hrmschedulesignset`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmschedulesignset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `datasourceid` | 来源id | `varchar2` | 50 | 否 | 来源id |
| 2 | `importtype` | 导入类型 | `char` | 1 | 是 | 导入类型 |
| 3 | `tablename` | 数据表名称 | `varchar2` | 1000 | 是 | 数据表名称 |
| 4 | `workcode` | 编号 | `varchar2` | 1000 | 是 | 编号 |
| 5 | `lastname` | 用户名 | `varchar2` | 1000 | 是 | 用户名 |
| 6 | `usertype` | 用户类型 | `varchar2` | 1000 | 是 | 用户类型 |
| 7 | `signtype` | 同步方式 | `varchar2` | 1000 | 是 | 同步方式 |
| 8 | `signdate` | 同步日期 | `varchar2` | 1000 | 是 | 同步日期 |
| 9 | `signtime` | 同步时间 | `varchar2` | 1000 | 是 | 同步时间 |
| 10 | `clientaddress` | 客户端地址 | `varchar2` | 1000 | 是 | 客户端地址 |
| 11 | `isincom` | isincom | `varchar2` | 1000 | 是 | isincom |

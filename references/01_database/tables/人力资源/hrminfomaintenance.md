# 泛微OA 数据表: `hrminfomaintenance`

- **所属模块**: `人力资源`
- **数据库表名**: `hrminfomaintenance`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemname` | 入职维护项目名称 | `varchar2` | 800 | 是 | 入职维护项目名称 |
| 3 | `hrmid` | 入职维护项目负责人 | `integer` | - | 是 | 入职维护项目负责人 |
| 4 | `operateuserid` | 操作者用户id | `varchar2` | 400 | 是 | 操作者用户id |
| 5 | `clientaddress` | 客户端地址 | `varchar2` | 400 | 是 | 客户端地址 |
| 6 | `operatedate` | 操作日期 | `varchar2` | 400 | 是 | 操作日期 |
| 7 | `operatetime` | 操作时间 | `varchar2` | 400 | 是 | 操作时间 |
| 8 | `hrmids` | 维护人员ids | `varchar2` | 1000 | 是 | 维护人员ids |

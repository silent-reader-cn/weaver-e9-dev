# 泛微OA 数据表: `docprintlog`

- **所属模块**: `知识管理`
- **数据库表名**: `docprintlog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `printuserid` | 打印人员id | `integer` | - | 是 | - |
| 3 | `printdocid` | 打印文档id | `integer` | - | 是 | - |
| 4 | `printdate` | 打印日期 | `char` | 10 | 是 | - |
| 5 | `printtime` | 打印时间 | `char` | 8 | 是 | - |
| 6 | `printnum` | 打印份数 | `integer` | - | 是 | - |
| 7 | `clientaddress` | 客户端ip | `varchar2` | 120 | 是 | - |

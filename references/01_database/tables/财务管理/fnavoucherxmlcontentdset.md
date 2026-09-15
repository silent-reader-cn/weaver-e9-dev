# 泛微OA 数据表: `fnavoucherxmlcontentdset`

- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherxmlcontentdset`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | - |
| 3 | `fnavoucherxmlcontentid` | fnavoucherxmlcontent.id | `integer` | - | 是 | - |
| 4 | `dsetalias` | 数据集别名 | `varchar2` | 1000 | 是 | - |
| 5 | `inittiming` | 初始化时机 | `integer` | - | 是 | - |
| 6 | `fnadatasetid` | 数据集id | `integer` | - | 是 | - |
| 7 | `dsetmemo` | 数据集备注 | `varchar2` | 4000 | 是 | - |
| 8 | `orderid` | 排序id | `number` | (5,2) | 是 | - |
| 9 | `parameter` | 参数字符串 | `clob` | 4000 | 是 | - |

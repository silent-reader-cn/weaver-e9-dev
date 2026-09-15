# 泛微OA 数据表: `fnainitsetoplog`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainitsetoplog`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | oa用户id | `integer` | - | 是 | - |
| 2 | `ip` | ip地址 | `varchar2` | 800 | 是 | - |
| 3 | `fnabktbname` | 备份数据表名后缀 | `varchar2` | 400 | 是 | - |
| 4 | `subject` | 本次操作是否初始化：科目 | `integer` | - | 是 | - |
| 5 | `fcc` | 本次操作是否初始化：成本中心 | `integer` | - | 是 | - |
| 6 | `fnabudget` | 本次操作是否初始化：预算 | `integer` | - | 是 | - |
| 7 | `fnaexpense` | 本次操作是否初始化：费用 | `integer` | - | 是 | - |
| 8 | `fnaloan` | 本次操作是否初始化：借还款 | `integer` | - | 是 | - |
| 9 | `fnaadvance` | 本次操作是否初始化：预付款 | `integer` | - | 是 | - |
| 10 | `opdate` | 操作日期 | `char` | 10 | 是 | - |
| 11 | `optime` | 操作时间 | `char` | 8 | 是 | - |

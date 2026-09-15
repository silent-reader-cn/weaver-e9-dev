# 泛微OA 数据表: `fnasynchronized`

- **所属模块**: `财务管理`
- **数据库表名**: `fnasynchronized`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `lockstr` | 锁定字符串 | `varchar2` | 200 | 否 | - |
| 2 | `lockguid` | 锁定uuid | `varchar2` | 60 | 否 | - |
| 3 | `userid` | oa用户id | `integer` | - | 否 | - |
| 4 | `memo` | 备注 | `varchar2` | 4000 | 是 | - |
| 5 | `lockdate` | 锁定日期 | `char` | 10 | 否 | - |
| 6 | `locktime` | 锁定时间 | `char` | 8 | 否 | - |

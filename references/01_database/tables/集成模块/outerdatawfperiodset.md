# 泛微OA 数据表: `outerdatawfperiodset`

- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawfperiodset`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `periodvalue` | 分钟值 | `integer` | - | 是 | 无 |
| 2 | `scope` | 触发周期应用范围 | `integer` | - | 否 | -1为全局设置;其他为存储相对应的触发设置的ID的范围 |
| 3 | `type` | 周期类型 | `integer` | - | 是 | 0,不触发;1,按分钟;2,按小时;3,按每天;4,按每周;5,按每月; |
| 4 | `val2` | 小时值 | `integer` | - | 是 | 无 |
| 5 | `daytime` | 时间值 | `varchar2` | 50 | 是 | 无 |
| 6 | `weekday` | 每周N | `integer` | - | 是 | 无 |
| 7 | `weektime` | 每周N时间值 | `varchar2` | 50 | 是 | 无 |
| 8 | `monthseq` | 每月顺序/倒序标志 | `integer` | - | 是 | 1,顺序;2,倒序 |
| 9 | `monthday` | 每月第N天 | `integer` | - | 是 | 无 |
| 10 | `monthtime` | 每月N时间值 | `varchar2` | 50 | 是 | 无 |

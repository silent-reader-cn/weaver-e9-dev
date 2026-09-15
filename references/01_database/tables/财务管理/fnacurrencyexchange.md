# 泛微OA 数据表: `fnacurrencyexchange`

- **所属模块**: `财务管理`
- **数据库表名**: `fnacurrencyexchange`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `defcurrencyid` | 基准币种 | `integer` | - | 是 | - |
| 3 | `thecurrencyid` | 换算币种 | `integer` | - | 是 | - |
| 4 | `fnayear` | 会计年度 | `char` | 4 | 是 | - |
| 5 | `periodsid` | 会计期间 | `integer` | - | 是 | - |
| 6 | `fnayearperiodsid` | 供比较用,没有其它意义 | `char` | 6 | 是 | - |
| 7 | `avgexchangerate` | 平均汇率 | `varchar2` | 160 | 是 | - |
| 8 | `endexchangerage` | 期末汇率 | `varchar2` | 160 | 是 | - |

# 泛微OA 数据表: `fnacurrency`

- **所属模块**: `财务管理`
- **数据库表名**: `fnacurrency`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `currencyname` | 币种名称 | `varchar2` | 480 | 是 | - |
| 3 | `currencydesc` | 币种描述 | `varchar2` | 1000 | 是 | - |
| 4 | `activable` | 币种活跃性 | `char` | 1 | 是 | 0：不活跃,1：活跃 |
| 5 | `isdefault` | 是否默认币种 | `char` | 1 | 是 | 0：否,1：是 |

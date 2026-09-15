# 泛微OA 数据表: `lgccounttype`

- **所属模块**: `客户管理`
- **数据库表名**: `lgccounttype`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | id |
| 2 | `typename` | 类型名称 | `varchar2` | 1000 | 是 | 类型名称 |
| 3 | `typedesc` | 类型描述 | `varchar2` | 1000 | 是 | 类型描述 |
| 4 | `salesinid` | 销售收入科目 | `integer` | 0 | 是 | 销售收入科目 |
| 5 | `salescostid` | 销售收入成本 | `integer` | 0 | 是 | 销售收入成本 |
| 6 | `salestaxid` | 销项税科目 | `integer` | 0 | 是 | 销项税科目 |
| 7 | `purchasetaxid` | 进项税科目 | `integer` | 0 | 是 | 进项税科目 |
| 8 | `stockid` | 存货核算科目 | `integer` | 0 | 是 | 存货核算科目 |
| 9 | `stockdiffid` | 存货差异科目 | `integer` | 0 | 是 | 存货差异科目 |
| 10 | `producecostid` | 生产成本科目 | `integer` | 0 | 是 | 生产成本科目 |

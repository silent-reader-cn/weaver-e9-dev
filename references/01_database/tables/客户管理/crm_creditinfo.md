# 泛微OA 数据表: `crm_creditinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_creditinfo`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `fullname` | 等级名称 | `varchar2` | 1000 | 是 | 等级名称 |
| 3 | `creditamount` | 信用金额额度 | `number` | - | 是 | 信用金额额度 |
| 4 | `highamount` | 最高信用额度 | `number` | - | 是 | 最高信用额度 |
| 5 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |

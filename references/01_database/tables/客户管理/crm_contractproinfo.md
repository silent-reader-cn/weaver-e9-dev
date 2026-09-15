# 泛微OA 数据表: `crm_contractproinfo`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contractproinfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `proid` | 产品id | `integer` | - | 是 | 产品id |
| 3 | `factnum` | 实际交货数量 | `float` | 22 | 是 | 实际交货数量 |
| 4 | `factdate` | 实际交货日期 | `char` | 10 | 是 | 实际交货日期 |
| 5 | `formnum` | 单据号 | `varchar2` | 1000 | 是 | 单据号 |
| 6 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |

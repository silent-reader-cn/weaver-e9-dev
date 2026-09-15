# 泛微OA 数据表: `lgcassetrelationtype`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcassetrelationtype`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `typename` | 产品配置类型名称 | `varchar2` | 480 | 是 | 产品配置类型名称 |
| 3 | `typedesc` | 产品类型说明 | `varchar2` | 1000 | 是 | 产品类型说明 |
| 4 | `typekind` | 类型 | `char` | 1 | 是 | 类型 |
| 5 | `shopadvice` | 购物协议 | `char` | 1 | 是 | 购物协议 |
| 6 | `contractlimit` | 合同限制 | `char` | 1 | 是 | 合同限制 |

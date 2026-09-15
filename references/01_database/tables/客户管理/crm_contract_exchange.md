# 泛微OA 数据表: `crm_contract_exchange`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contract_exchange`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `contractid` | 合同id | `integer` | - | 是 | 合同id |
| 3 | `name` | 标题 | `varchar2` | 1000 | 是 | 标题 |
| 4 | `remark` | 备注 | `varchar2` | - | 是 | 备注 |
| 5 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |
| 6 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 7 | `createtime` | 创建时间 | `char` | 10 | 是 | 创建时间 |

# 泛微OA 数据表: `crm_customercontacter_mind`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customercontacter_mind`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `customerid` | 客户id | `varchar2` | 800 | 是 | 客户id |
| 3 | `contacterid` | 联系人id | `varchar2` | 800 | 是 | 联系人id |
| 4 | `parentid` | 父节点id | `varchar2` | 800 | 是 | 父节点id |
| 5 | `direction` | 说明 | `varchar2` | 80 | 是 | 说明 |

# 泛微OA 数据表: `crm_addresstype`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_addresstype`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `fullname` | 地址全称 | `varchar2` | 1000 | 是 | 地址全称 |
| 3 | `description` | 地址描述 | `varchar2` | 1000 | 是 | 地址描述 |
| 4 | `candelete` | 是否可以被删除 | `char` | 1 | 是 | n:不可删除 |
| 5 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |

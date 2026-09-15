# 泛微OA 数据表: `crm_viewlog`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_viewlog`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customerid` | 客户id | `integer` | 11 | 是 | 客户id |
| 2 | `type` | 查看客户信息 | `integer` | 11 | 是 | 客户修改信息、联系人信息、地址信息，CRM查看信息 |
| 3 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 4 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
| 5 | `modifier` | 修改者id | `integer` | 11 | 是 | 修改者id |
| 6 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |

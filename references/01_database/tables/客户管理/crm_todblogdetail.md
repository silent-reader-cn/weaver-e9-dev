# 泛微OA 数据表: `crm_todblogdetail`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_todblogdetail`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 3 | `logid` | 导入日志id | `integer` | - | 是 | 导入日志表 |
| 4 | `operationtype` | 操作类型 | `varchar2` | 10 | 是 | 更新，新建 |

# 泛微OA 数据表: `crm_seasapprovelog`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_seasapprovelog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `description` | 描述 | `varchar2` | 2000 | 是 | 描述 |
| 2 | `id` | id | `integer` | - | 否 | id |
| 3 | `seasid` | 公海id | `integer` | - | 是 | 公海id |
| 4 | `custoemrid` | 客户id | `integer` | - | 是 | 客户id |
| 5 | `operatetype` | 操作类型 | `integer` | - | 是 | 1：申领客户；2：客户审批；3：客户分配；4：加入公海； |
| 6 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建日期 |
| 7 | `createuser` | 创建者 | `integer` | - | 是 | 创建者 |

# 泛微OA 数据表: `crm_deliverytype`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_deliverytype`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 11 | 否 | id |
| 2 | `fullname` | 类型名称 | `varchar2` | 400 | 是 | 类型名称 |
| 3 | `description` | 类型描述 | `varchar2` | 1000 | 是 | 类型描述 |
| 4 | `sendtype` | 发货方法 | `varchar2` | 1000 | 是 | 发货方法 |
| 5 | `shipment` | 运货方法 | `varchar2` | 1000 | 是 | 运货方法 |
| 6 | `receive` | 收货方法 | `varchar2` | 1000 | 是 | 收货方法 |

# 泛微OA 数据表: `airinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `airinvoice`
- **文档收录字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `user_name` | 乘机人姓名 | `varchar2` | 200 | - | - |
| 4 | `user_id` | 身份证号 | `varchar2` | 200 | - | - |
| 5 | `agentcode` | 销售单位代号 | `varchar2` | 1000 | - | - |
| 6 | `issue_by` | 填开单位 | `varchar2` | 1000 | - | - |
| 7 | `fare` | 票价 | `varchar2` | 200 | - | - |
| 8 | `fuel_surcharge` | 燃油附加费 | `varchar2` | 200 | - | - |
| 9 | `caac_development_fund` | 民航发展基金 | `varchar2` | 200 | - | - |
| 10 | `insurance` | 保险费 | `varchar2` | 200 | - | - |

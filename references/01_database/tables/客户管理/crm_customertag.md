# 泛微OA 数据表: `crm_customertag`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customertag`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 11 | 否 | id |
| 2 | `customerid` | 客户id | `integer` | 11 | 是 | 客户id |
| 3 | `tag` | 标签名称 | `varchar2` | 800 | 是 | 标签名称 |
| 4 | `creater` | 创建人员 | `integer` | 11 | 是 | 创建人员 |
| 5 | `createdate` | 创建日志 | `char` | 10 | 是 | 创建日志 |
| 6 | `createtime` | 创建时间 | `char` | 8 | 是 | 创建时间 |

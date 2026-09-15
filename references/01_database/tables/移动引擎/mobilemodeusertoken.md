# 泛微OA 数据表: `mobilemodeusertoken`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemodeusertoken`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `varchar2` | 200 | 是 | 已加密的用户id |
| 3 | `token` | 令牌 | `varchar2` | 32 | 是 | 令牌 |

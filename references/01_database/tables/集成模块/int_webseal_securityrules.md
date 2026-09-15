# 泛微OA 数据表: `int_webseal_securityrules`

- **所属模块**: `集成模块`
- **数据库表名**: `int_webseal_securityrules`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `Id` | 标识 | `integer` | - | 否 | 标识 |
| 2 | `SecurityRule` | 过滤地址 | `varchar2` | 500 | 否 | 不被安全补丁包拦截的地址 |
| 3 | `RuleDescription` | 说明 | `varchar2` | 500 | 是 | 说明 |

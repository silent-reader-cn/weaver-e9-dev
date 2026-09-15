# 泛微OA 数据表: `wsregistemethodparam`

- **所属模块**: `集成模块`
- **数据库表名**: `wsregistemethodparam`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 自增长主键 |
| 2 | `methodid` | 方法主键id | `integer` | - | 是 | 关联wsregistemethod方法表中主键id字段 |
| 3 | `paramname` | 参数名称 | `varchar2` | 1000 | 是 | 参数名称 |
| 4 | `paramtype` | 参数类型 | `varchar2` | 1000 | 是 | 参数类型 |
| 5 | `isarray` | 是否数组 | `char` | 1 | 是 | 是否数组 |

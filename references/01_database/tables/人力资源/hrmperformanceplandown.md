# 泛微OA 数据表: `hrmperformanceplandown`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceplandown`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planid` | 计划id | `integer` | - | 是 | 计划id |
| 3 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 4 | `status` | 是否启用 | `char` | 1 | 是 | 0不启用，1启用 |
| 5 | `logs` | 日志 | `varchar2` | 1000 | 是 | 日志 |

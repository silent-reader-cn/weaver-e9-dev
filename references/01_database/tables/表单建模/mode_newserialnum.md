# 泛微OA 数据表: `mode_newserialnum`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_newserialnum`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `codemainid` | 编码id | `integer` | - | 是 | 编码id，对应modecode表中id |
| 3 | `condition` | 匹配条件 | `varchar2` | 1000 | 是 | - |
| 4 | `num` | 当前流水号 | `integer` | - | 是 | 流水号的值 |

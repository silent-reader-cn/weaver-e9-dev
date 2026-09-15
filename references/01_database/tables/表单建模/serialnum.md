# 泛微OA 数据表: `serialnum`

- **所属模块**: `表单建模`
- **数据库表名**: `serialnum`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `num` | 当前流水号 | `integer` | - | 是 | - |
| 3 | `codemainid` | 编码id | `integer` | - | 是 | 编码id，对应modecode表中id |
| 4 | `field1` | 编码字段1 | `varchar2` | 800 | 是 | - |
| 5 | `field2` | 编码字段2 | `varchar2` | 800 | 是 | - |
| 6 | `field3` | 编码字段3 | `varchar2` | 800 | 是 | - |
| 7 | `field4` | 日期字段1 | `varchar2` | 800 | 是 | - |
| 8 | `field5` | 日期字段2 | `varchar2` | 800 | 是 | - |
| 9 | `field6` | 日期字段3 | `varchar2` | 800 | 是 | - |

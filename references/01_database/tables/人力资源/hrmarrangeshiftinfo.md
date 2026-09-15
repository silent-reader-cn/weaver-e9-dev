# 泛微OA 数据表: `hrmarrangeshiftinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmarrangeshiftinfo`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `shiftdate` | 排班日志 | `char` | 10 | 是 | 排班日志 |
| 4 | `shiftid` | 排班id | `integer` | - | 是 | hrmarrangeshift表的id |

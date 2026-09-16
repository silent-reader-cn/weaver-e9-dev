# 泛微OA 数据表: `hrmarrangeshiftinfo`

- **中文名称**: 人力资源排班详情表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmarrangeshiftinfo`
- **主键**: `id`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 否 | 否 | - | - | 人员id |
| 3 | `shiftdate` | 排班日志 | `char` | 10 | 是 | 否 | 否 | - | - | 排班日志 |
| 4 | `shiftid` | 排班id | `integer` | - | 是 | 否 | 否 | - | - | hrmarrangeshift表的id |

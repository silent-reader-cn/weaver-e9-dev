# 泛微OA 数据表: `hrmschedulemonth`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmschedulemonth`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `hrmid` | 被考勤人id | `integer` | - | 是 | 被考勤人id（hrmresource表主键id） |
| 2 | `difftype` | 考勤种类 | `integer` | - | 是 | 考勤种类 |
| 3 | `hours` | 考勤时间 | `float` | 22 | 是 | 考勤时间 |
| 4 | `theyear` | 年度 | `char` | 4 | 是 | 年度 |
| 5 | `themonth` | 月度 | `char` | 2 | 是 | 月度 |

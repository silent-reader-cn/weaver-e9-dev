# 泛微OA 数据表: `hrmworktimecount`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmworktimecount`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `workdate` | 工作日期 | `char` | 7 | 是 | 工作日期 |
| 4 | `shiftid` | 排班信息id | `integer` | - | 是 | HrmArrangeShift表的id |
| 5 | `workcount` | 计算工作时间 | `integer` | - | 是 | 计算工作时间 |

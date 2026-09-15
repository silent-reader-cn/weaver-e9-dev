# 泛微OA 数据表: `kq_OvertimeRestTime`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_OvertimeRestTime`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键ID | `integer` | 11 | 否 | - |
| 2 | `ruleId` | 加班规则的ID | `integer` | 11 | 否 | - |
| 3 | `dayType` | 日期类型 | `integer` | 11 | 否 | 1--节假日、2--工作日、3--休息日 |
| 4 | `startType` | 开始时间的类型 | `integer` | 11 | 否 | 此字段已不再修改，固定为0 |
| 5 | `endType` | 结束时间的类型 | `integer` | 11 | 否 | 此字段已不再修改，固定为0 |
| 6 | `startTime` | 开始时间 | `char` | 5 | 否 | - |
| 7 | `endTime` | 结束时间 | `char` | 5 | 否 | - |

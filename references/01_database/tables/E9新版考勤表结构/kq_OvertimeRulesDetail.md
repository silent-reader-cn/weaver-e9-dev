# 泛微OA 数据表: `kq_OvertimeRulesDetail`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_OvertimeRulesDetail`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `Id` | 主键ID | `integer` | 11 | 否 | - |
| 2 | `ruleId` | 加班规则的ID | `integer` | 11 | 否 | 对应的是kq_OvertimeRules的主键ID |
| 3 | `dayType` | 日期类型 | `integer` | 11 | 否 | 1-节假日 2-工作日 3-休息日 |
| 4 | `overtimeEnable` | 是否允许加班 | `integer` | 11 | 否 | 0-不允许、1-允许 |
| 5 | `computingMode` | 加班方式计算 | `integer` | 11 | 否 | 1-需审批，以加班流程为准 2-需审批，以打卡为准，但是不能超过审批时长 3-无需审批，根据打卡时间计算加班时长 |
| 6 | `startTime` | 下班后多少分钟开始计算加班 | `integer` | 11 | 否 | - |
| 7 | `minimumLen` | 最小加班时长 | `integer` | 11 | 否 | - |
| 8 | `paidLeaveEnable` | 是否转为调休余额 | `integer` | 11 | 否 | 0-不允许 1-允许 |
| 9 | `lenOfOvertime` | 加班转调休比例中的加班时长 | `number` | 10,2 | 否 | - |
| 10 | `lenOfLeave` | 加班转调休比例中的调休时长 | `number` | 10,2 | 否 | - |
| 11 | `hasRestTime` | 是否需要排除休息时间 | `integer` | 11 | 否 | 0--不需要 1-需要 |

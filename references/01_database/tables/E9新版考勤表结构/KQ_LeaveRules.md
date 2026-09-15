# 泛微OA 数据表: `KQ_LeaveRules`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `KQ_LeaveRules`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键ID | `integer` | 11 | 否 | - |
| 2 | `leaveName` | 假期类型的名称 | `varchar2` | 200 | 否 | - |
| 3 | `scopeType` | 流程应用范围 | `integer` | 11 | 否 | 流程应用范围类型：0-总部、1-分部指的是哪些机构的人能够在请假流程中看到此假期类型 |
| 4 | `scopeValue` | 流程应用范围 | `varchar2` | 200 | 否 | 流程应用范围为分部时为分部ID |
| 5 | `leaveCode` | 假期类型 | `varchar2` | 200 | 否 | 此字段备用------------假期类型：annualLeave-年假paidCompassionateLeave-带薪事假paidSickLeave-带薪病假vacationLeave-调休compassionateLeave-事假sickLeave-病假maternityLeave-产假paternityLeave-陪产假marriageLeave-婚假funeralLeave-丧假breastfeedingLeave-哺乳假 |
| 6 | `minimumUnit` | 最小请假单位 | `integer` | 11 | 否 | 最小请假单位：1-按天请假2-按半天请假3-按小时请假4-按整天请假 |
| 7 | `proportion` | 转换比例 | `number` | 10,2 | 否 | 转换比例（1天=XX小时）注：用户更改了最小请假单位后，假期余额的单位也发生了变化，故需要做出转换 |
| 8 | `computingMode` | 计算请假时长方式 | `integer` | 11 | 否 | 计算请假时长方式：1-按工作日计算请假时长2-按自然日计算请假时长 |
| 9 | `hoursToDay` | 日折算时长 | `number` | 10,2 | 否 | 日折算时长注：当最小请假单位=1-按天请假、2-按半天请假并且计算请假时长方式=2-按自然日计算请假时长时有效 |
| 10 | `balanceEnable` | 启用假期余额 | `integer` | 11 | 否 | 启用假期余额：0-不启用1-启用 |
| 11 | `isEnable` | 是否启用此假期 | `integer` | 11 | 否 | 是否启用：0-未启用、1-启用 |
| 12 | `isDelete` | 是否已经删除 | `integer` | 11 | 否 | 是否已经删除：0-未删除1-已删除 |

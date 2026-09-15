# 泛微OA 数据表: `kq_MixedModeToLeave`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_MixedModeToLeave`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键 | `integer` | 11 | 否 | 主键 |
| 2 | `leaveRulesId` | 假期规则的ID | `integer` | 11 | 否 | 关联的假期规则的ID(kq_LeaveRulesDetail的ID) |
| 3 | `lowerLimit` | 工龄下限 | `integer` | 11 | 否 | 工龄下限 |
| 4 | `upperLimit` | 工龄上限 | `integer` | 11 | 否 | 工龄上限 |
| 5 | `lowerLimit2` | 司龄下限 | `integer` | 11 | 否 | 司龄下限 |
| 6 | `upperLimit2` | 司龄上限 | `integer` | 11 | 否 | 司龄上限 |
| 7 | `amount` | 法定年假天数/小时数 | `number` | 10,2 | 否 | 法定年假天数/小时数 |
| 8 | `amount2` | 福利年假天数/小时数 | `number` | 10,2 | 否 | 福利年假天数/小时数 |

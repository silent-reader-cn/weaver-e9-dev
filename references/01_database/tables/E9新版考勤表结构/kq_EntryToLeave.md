# 泛微OA 数据表: `kq_EntryToLeave`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_EntryToLeave`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键ID | `integer` | 11 | 否 | 主键 |
| 2 | `leaveRulesId` | 假期规则的ID | `integer` | 11 | 否 | 关联的假期规则的ID(kq_LeaveRulesDetail的ID) |
| 3 | `lowerLimit` | 下限 | `integer` | 11 | 否 | 司龄下限 |
| 4 | `upperLimit` | 上限 | `integer` | 11 | 否 | 司龄上限 |
| 5 | `amount` | 对应的天数/小时数 | `number` | 10,2 | 否 | 假期天数/小时数 |

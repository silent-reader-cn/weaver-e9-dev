# 泛微OA 数据表: `kq_balanceOfLeave`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_balanceOfLeave`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ID` | 主键 | `integer` | 11 | 否 | 主键 |
| 2 | `leaveRulesId` | 假期类型的ID | `integer` | 11 | 否 | 关联的假期类型的ID(kq_LeaveRules的ID) |
| 3 | `resourceId` | 人员ID | `integer` | 11 | 否 | 人员ID |
| 4 | `belongYear` | 所属年份 | `char` | 4 | 否 | 所属年份 |
| 5 | `baseAmount` | 假期余额基数 | `number` | 10,2 | 否 | 假期余额基数注：混合模式下为法定年假总数 |
| 6 | `usedAmount` | 已用假期余额 | `number` | 10,2 | 否 | 已使用假期余额数注：混合模式下为已使用法定年假数 |
| 7 | `extraAmount` | 额外假期余额 | `number` | 10,2 | 否 | 额外的假期余额数注：混合模式下为额外的法定年假数 |
| 8 | `baseAmount2` | 假期余额基数 | `number` | 10,2 | 否 | 福利年假总数注：仅混合模式下使用 |
| 9 | `usedAmount2` | 已用假期余额 | `number` | 10,2 | 否 | 已使用福利年假数注：仅混合模式下使用 |
| 10 | `extraAmount2` | 额外假期余额 | `number` | 10,2 | 否 | 额外的福利年假数注：仅混合模式下使用 |
| 11 | `status` | 假期余额是否有效 | `integer` | 11 | 否 | 此字段已无效--是否有效已经改为实时计算 |
| 12 | `expirationDate` | 失效日期 | `char` | 10 | 否 | 此字段已无效--失效日期已经改为实时计算 |

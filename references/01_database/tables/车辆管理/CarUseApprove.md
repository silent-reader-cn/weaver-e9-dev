# 泛微OA 数据表: `CarUseApprove`

- **所属模块**: `车辆管理`
- **数据库表名**: `CarUseApprove`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `carid` | 车辆信息 | `integer` | - | 否 | - |
| 3 | `driver` | 司机 | `integer` | - | 否 | - |
| 4 | `userid` | 使用人 | `integer` | - | 否 | - |
| 5 | `departmentid` | 公司 | `integer` | - | 否 | - |
| 6 | `applier` | 补充 | `integer` | - | 否 | - |
| 7 | `reason` | 用车缘由 | `varchar2` | 2000 | 否 | - |
| 8 | `mileage` | 使用公里 | `integer` | - | 否 | - |
| 9 | `startData` | 开始日期 | `varchar2` | 2000 | 否 | - |
| 10 | `startTime` | 开始时间 | `varchar2` | 2000 | 否 | - |
| 11 | `endData` | 结束日期 | `varchar2` | 2000 | 否 | - |
| 12 | `endTime` | 结束时间 | `varchar2` | 2000 | 否 | - |
| 13 | `requestid` | 流程id | `integer` | - | 否 | - |
| 14 | `remark` | 详细描述 | `varchar2` | 2000 | 否 | - |
| 15 | `cancel` | 取消 | `varchar2` | 2000 | 否 | - |
| 16 | `cancelData` | 取消日期 | `varchar2` | 2000 | 否 | - |
| 17 | `cancelTime` | 取消时间 | `varchar2` | 2000 | 否 | - |
| 18 | `manager` | 上级 | `integer` | - | 否 | - |
| 19 | `usefee` | 未使用 | `number` | - | 否 | - |
| 20 | `totalfee` | 总共未使用 | `number` | - | 否 | - |

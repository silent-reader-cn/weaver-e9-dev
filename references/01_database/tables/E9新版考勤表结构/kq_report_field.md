# 泛微OA 数据表: `kq_report_field`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_report_field`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `fieldname` | 字段名 | `varchar2` | 500 | 否 | - |
| 3 | `fieldlabel` | 字段显示名 | `integer` | - | 否 | - |
| 4 | `width` | 列宽 | `integer` | - | 否 | - |
| 5 | `unittype` | 单位 | `integer` | - | 否 | - |
| 6 | `parentid` | 上级字段名 | `varchar2` | 500 | 否 | - |
| 7 | `isDefinedColumn` | 是否可以定制显示 | `integer` | - | 否 | - |
| 8 | `defaultShow` | 是否默认显示 | `integer` | - | 否 | - |
| 9 | `isLeaveType` | 是否为请假类型 | `integer` | - | 否 | - |
| 10 | `reportType` | 报表类型 | `varchar2` | 50 | 否 | - |
| 11 | `isdataColumn` | 是否数据列 | `integer` | - | 否 | - |
| 12 | `showDetial` | 显示明细 | `integer` | - | 否 | - |

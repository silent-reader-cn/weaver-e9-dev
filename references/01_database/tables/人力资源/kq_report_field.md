# 泛微OA 数据表: `kq_report_field`

- **所属模块**: `人力资源`
- **数据库表名**: `kq_report_field`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | - | - |
| 2 | `fieldname` | 字段名 | `varchar2` | 500 | - | - |
| 3 | `fieldlabel` | 字段显示名 | `integer` | - | - | - |
| 4 | `width` | 列宽 | `integer` | - | - | - |
| 5 | `unittype` | 单位 | `integer` | - | - | - |
| 6 | `parentid` | 上级字段名 | `varchar2` | 500 | - | - |
| 7 | `isDefinedColumn` | 是否可以定制显示 | `integer` | - | - | - |
| 8 | `defaultShow` | 是否默认显示 | `integer` | - | - | - |
| 9 | `isLeaveType` | 是否为请假类型 | `integer` | - | - | - |
| 10 | `reportType` | 报表类型 | `varchar2` | 50 | - | - |
| 11 | `isdataColumn` | 是否数据列 | `integer` | - | - | - |
| 12 | `showDetial` | 显示明细 | `integer` | - | - | - |

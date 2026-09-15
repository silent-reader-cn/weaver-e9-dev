# 泛微OA 数据表: `kq_shiftschedule`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_shiftschedule`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `kqdate` | 考勤日期 | `varchar2` | 10 | 否 | - |
| 3 | `serialid` | 班次ID | `integer` | - | 否 | - |
| 4 | `resourceid` | 人员ID | `integer` | - | 否 | - |
| 5 | `groupid` | 考勤组ID | `integer` | - | 否 | - |
| 6 | `isdelete` | 是否删除 | `integer` | - | 否 | - |

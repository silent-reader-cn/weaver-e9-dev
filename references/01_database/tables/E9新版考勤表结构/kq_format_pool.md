# 泛微OA 数据表: `kq_format_pool`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_format_pool`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `resourceid` | 人员ID | `integer` | - | 否 | - |
| 3 | `kqdate` | 考勤日期 | `varchar2` | 10 | 否 | - |
| 4 | `status` | 状态 | `integer` | - | 否 | - |
| 5 | `created` | 创建时间 | `timestamp(6)` | - | 否 | - |

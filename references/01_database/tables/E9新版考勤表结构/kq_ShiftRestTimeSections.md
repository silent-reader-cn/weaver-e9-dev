# 泛微OA 数据表: `kq_ShiftRestTimeSections`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_ShiftRestTimeSections`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `serialid` | 外键 对应ShiftManagement | `integer` | - | 否 | - |
| 3 | `resttype` | 休息类型，开始(start)/结束(end) | `varchar2` | - | 否 | - |
| 4 | `across` | 指定时段是否跨天 1表示跨天 | `char` | - | 否 | - |
| 5 | `time` | 时间 | `varchar2` | - | 否 | - |
| 6 | `isdelete` | 删除标识1标识删除 | `char` | - | 否 | - |

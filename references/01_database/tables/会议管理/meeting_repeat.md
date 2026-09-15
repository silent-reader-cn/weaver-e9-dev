# 泛微OA 数据表: `meeting_repeat`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_repeat`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `meetingid` | 会议id | `integer` | - | 否 | - |
| 3 | `begindate` | 重复会议开始时间 | `varchar2` | 80 | 否 | - |
| 4 | `doneflag` | 结束标志 | `varchar2` | 8 | 是 | 无效 |

# 泛微OA 数据表: `meeting_view_status`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_view_status`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `meetingid` | 会议id | `integer` | - | 是 | - |
| 3 | `userid` | 人员id | `integer` | - | 是 | - |
| 4 | `usertype` | 人员类型 | `char` | 1 | 是 | 1：内部用户，2：外部用户 |
| 5 | `status` | 状态 | `char` | 1 | 是 | 0：未看，1：已看，2：取消 |

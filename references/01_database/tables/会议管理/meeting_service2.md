# 泛微OA 数据表: `meeting_service2`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_service2`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 会议服务id | `integer` | - | 否 | - |
| 2 | `meetingid` | 会议标识 | `integer` | - | 是 | - |
| 3 | `hrmid` | 会议负责人id | `integer` | - | 是 | - |
| 4 | `name` | 服务类型 | `varchar2` | 1000 | 是 | - |
| 5 | `desc_n` | 其他 | `varchar2` | 1000 | 是 | - |

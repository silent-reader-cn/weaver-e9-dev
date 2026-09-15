# 泛微OA 数据表: `meeting_service_new`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_service_new`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 2 | `meetingid` | 对应会议id | `integer` | 0 | 否 | 对应meeting表id |
| 3 | `items` | 选择的服务项目 | `varchar2` | 1000 | 是 | 服务项目ids |
| 4 | `hrmids` | 负责人 | `varchar2` | 1000 | 是 | 负责人ids |
| 5 | `otheritem` | 其他服务 | `varchar2` | 1000 | 是 | 其他服务 |

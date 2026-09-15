# 泛微OA 数据表: `meeting_service`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_service`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | 0 | 否 | ID |
| 2 | `meetingtype` | 服务类型 | `integer` | 0 | 是 | 服务类型 |
| 3 | `hrmid` | 负责人员id | `integer` | 0 | 是 | 负责人员id |
| 4 | `name` | 负责人员名称 | `varchar2` | 1000 | 是 | 负责人员名称 |
| 5 | `desc_n` | 服务项目 | `varchar2` | 1000 | 是 | 服务项目 |

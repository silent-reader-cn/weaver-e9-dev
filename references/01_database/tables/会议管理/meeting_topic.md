# 泛微OA 数据表: `meeting_topic`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_topic`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `meetingid` | 会议标识 | `integer` | - | 是 | - |
| 3 | `subject` | 议程主题 | `varchar2` | 1000 | 是 | - |
| 4 | `hrmid` | &nbsp; | `integer` | - | 是 | 单人力资源字段已废弃 |
| 5 | `isopen` | 是否公开 | `integer` | - | 是 | - |
| 6 | `hrmids` | 负责人 | `varchar2` | 1000 | 是 | - |
| 7 | `projid` | 相关项目id | `integer` | - | 是 | - |
| 8 | `crmid` | &nbsp; | `integer` | - | 是 | 单人力资源字段已废弃 |
| 9 | `crmids` | 相关客户id | `varchar2` | 4000 | 是 | - |

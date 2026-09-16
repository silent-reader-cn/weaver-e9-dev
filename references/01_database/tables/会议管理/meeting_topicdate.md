# 泛微OA 数据表: `meeting_topicdate`

- **中文名称**: 议程安排时间表
- **所属模块**: `会议管理`
- **数据库表名**: `meeting_topicdate`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 否 | 否 | - | - | 主键 |
| 2 | `meetingid` | 会议id | `integer` | 0 | 是 | 是 | 否 | meeting表id | - | 对应meeting表id |
| 3 | `topicid` | 议程id | `integer` | 0 | 是 | 是 | 否 | meeting_topic表id | - | 对应meeting_topic表id |
| 4 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 开始日期 |
| 5 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 开始时间 |
| 6 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 结束日期 |
| 7 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 结束时间 |

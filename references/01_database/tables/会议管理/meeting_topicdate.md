# 泛微OA 数据表: `meeting_topicdate`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_topicdate`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 2 | `meetingid` | 会议id | `integer` | 0 | 是 | 对应meeting表id |
| 3 | `topicid` | 议程id | `integer` | 0 | 是 | 对应meeting_topic表id |
| 4 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 开始日期 |
| 5 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | 开始时间 |
| 6 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 结束日期 |
| 7 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | 结束时间 |

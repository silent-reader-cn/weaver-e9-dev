# 泛微OA 数据表: `meeting_topicdoc`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_topicdoc`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 2 | `meetingid` | 会议id | `integer` | 0 | 是 | 对应meeting表id |
| 3 | `topicid` | 议程id | `integer` | 0 | 是 | 对应meeting_topic表id |
| 4 | `docid` | 文档id | `integer` | 0 | 是 | 对应docdetail表id |
| 5 | `hrmid` | 文档提交人id | `integer` | 0 | 是 | 对应hrmresource表id |

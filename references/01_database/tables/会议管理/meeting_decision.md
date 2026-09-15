# 泛微OA 数据表: `meeting_decision`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_decision`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `meetingid` | 会议id | `integer` | - | 是 | meeting表id |
| 3 | `requestid` | 会议决议通知流程请求id | `integer` | - | 是 | 会议决议通知流程请求id |
| 4 | `coding` | 决议编号 | `varchar2` | 800 | 是 | 决议编号 |
| 5 | `subject` | 决议相关项目 | `varchar2` | 1000 | 是 | 决议相关项目 |
| 6 | `hrmid01` | 决议执行人 | `varchar2` | 1000 | 是 | 决议执行人 |
| 7 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | 开始日期 |
| 8 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | 开始时间 |
| 9 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | 结束日期 |
| 10 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | 结束时间 |
| 11 | `hrmid02` | 决议检查人 | `varchar2` | 80 | 是 | 决议检查人 |

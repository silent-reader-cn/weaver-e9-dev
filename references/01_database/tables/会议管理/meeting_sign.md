# 泛微OA 数据表: `meeting_sign`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_sign`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `site` | 签到地点 | `varchar2` | 1000 | 是 | 签到地点 |
| 2 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 3 | `meetingid` | 会议ID | `integer` | - | 否 | 会议ID |
| 4 | `userid` | 参会人员ID | `integer` | - | 否 | 参会人员ID |
| 5 | `attendtype` | 参会人员类型 | `integer` | - | 否 | 0:非参会人员;1:参会人员 |
| 6 | `signtime` | 签到日期 | `varchar2` | 160 | 是 | 签到日期,日期格式yyyy-MM-dd HH:mm:ss |
| 7 | `signreson` | 参会说明 | `varchar2` | 1000 | 是 | 参会说明 |
| 8 | `flag` | 是否签到成功 | `integer` | - | 否 | 1：签到成功 |
| 9 | `longitude` | 经度 | `number` | (20,6) | 是 | 经度 |
| 10 | `latitude` | 纬度 | `number` | (20,6) | 是 | 纬度 |
| 11 | `signremark` | 签到日志 | `varchar2` | 1000 | 是 | 签到日志 |

# 泛微OA 数据表: `meeting_membercrm`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_membercrm`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 2 | `meetingid` | 会议id | `integer` | 0 | 是 | 会议id |
| 3 | `memberrecid` | 参会人员记录id | `integer` | 0 | 是 | 对应meeting_member2表id字段 |
| 4 | `name` | 姓名 | `varchar2` | 800 | 是 | 姓名 |
| 5 | `sex` | 性别 | `integer` | 0 | 是 | 性别 |
| 6 | `occupation` | 职务 | `varchar2` | 800 | 是 | 职务 |
| 7 | `tel` | 电话 | `varchar2` | 800 | 是 | 电话 |
| 8 | `handset` | 手机 | `varchar2` | 800 | 是 | 手机 |
| 9 | `desc_n` | 备注 | `varchar2` | 1000 | 是 | 备注 |

# 泛微OA 数据表: `meeting_member2`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_member2`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `meetingid` | 会议id | `integer` | - | 是 | - |
| 3 | `membertype` | 人员类型 | `integer` | - | 是 | 1：人力资源，2：客户，3：所有人，5：部门，6：分部，7：角色 |
| 4 | `memberid` | 参会人员id | `integer` | - | 是 | - |
| 5 | `membermanager` | 客户经理 | `integer` | - | 是 | - |
| 6 | `isattend` | 是否参加 | `varchar2` | 400 | 是 | 1:参加 2:不参加 |
| 7 | `begindate` | 开始日期 | `varchar2` | 80 | 是 | - |
| 8 | `begintime` | 开始时间 | `varchar2` | 64 | 是 | - |
| 9 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | - |
| 10 | `endtime` | 结束时间 | `varchar2` | 64 | 是 | - |
| 11 | `bookroom` | 预定房间 | `varchar2` | 400 | 是 | - |
| 12 | `roomstander` | 房间标准 | `varchar2` | 400 | 是 | - |
| 13 | `bookticket` | 预定车票 | `varchar2` | 400 | 是 | - |
| 14 | `ticketstander` | 交通工具 | `varchar2` | 400 | 是 | - |
| 15 | `othermember` | 其他人员 | `varchar2` | 1000 | 是 | - |
| 16 | `recremark` | 备注 | `varchar2` | 1000 | 是 | - |

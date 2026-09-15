# 泛微OA 数据表: `bill_meeting_dt2_service`

- **所属模块**: `会议管理`
- **数据库表名**: `bill_meeting_dt2_service`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `mainid` | 会议id | `integer` | - | 是 | 流程主表bill_meeting的id |
| 3 | `items` | 服务项目 | `varchar2` | 2000 | 是 | 服务项目ids |
| 4 | `otheritem` | 其他服务 | `varchar2` | 2000 | 是 | 其他服务 |
| 5 | `hrmids` | 负责人 | `clob` | 4000 | 是 | 负责人ids |

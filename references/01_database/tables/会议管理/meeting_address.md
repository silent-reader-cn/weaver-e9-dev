# 泛微OA 数据表: `meeting_address`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_address`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | 0 | 否 | 主键 |
| 2 | `meetingtype` | 会议类型 | `integer` | 0 | 是 | 会议类型 |
| 3 | `addressid` | 地点id | `integer` | 0 | 是 | 地点id |
| 4 | `desc_n` | 描述 | `varchar2` | 1000 | 是 | 描述 |

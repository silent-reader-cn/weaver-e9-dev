# 泛微OA 数据表: `meeting_remind`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_remind`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键 |
| 2 | `meeting` | 会议id | `integer` | - | 否 | meeting表id |
| 3 | `remindtime` | 提醒时间 | `varchar2` | 160 | 是 | 提醒时间 |
| 4 | `modetype` | 提醒模式 | `varchar2` | 800 | 是 | 针对meeting_remind_mode指定的type |

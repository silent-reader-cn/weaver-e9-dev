# 泛微OA 数据表: `meeting_remind_template`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_remind_template`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `type` | 提醒方式 | `integer` | - | 否 | 2:短信  3 邮件  4:预留的自定义开发  5:微信服务号 6:消息中心提醒 |
| 3 | `desc_n` | 模板描述 | `varchar2` | 1000 | 是 | - |
| 4 | `title` | 发送标题 | `varchar2` | 1000 | 是 | 暂时邮件使用,可以通过meeting_remind_type中hastitle来指定 |
| 5 | `body` | 发送主题消息模板 | `varchar2` | 2000 | 是 | 可以使用参数 |
| 6 | `modetype` | 提醒模式 | `varchar2` | 800 | 是 | 针对meeting_remind_mode的type类型 |

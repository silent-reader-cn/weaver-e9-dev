# 泛微OA 数据表: `sms_reminder_set`

- **所属模块**: `短信模块`
- **数据库表名**: `sms_reminder_set`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | 主键id |
| 2 | `prefix` | 提醒前缀 | `varchar2` | 1000 | 是 | &nbsp; |
| 3 | `prefixconnector` | 前缀连接符 | `varchar2` | 80 | 是 | &nbsp; |
| 4 | `suffix` | 提醒后缀 | `varchar2` | 1000 | 是 | &nbsp; |
| 5 | `suffixconnector` | 后缀连接符 | `varchar2` | 80 | 是 | &nbsp; |
| 6 | `type` | 提醒类型 | `varchar2` | 800 | 否 | all 表示通用 其他是各自模块指定 |
| 7 | `def` | 是否是默认 | `char` | 1 | 否 | 1 默认 |

# 泛微OA 数据表: `hrmbirthremindmsg`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmbirthremindmsg`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `title` | 提醒内容 | `varchar2` | 4000 | 是 | 提醒内容 |
| 3 | `resources` | 人员id字符串 | `varchar2` | 4000 | 是 | 人员id字符串 |
| 4 | `reminddate` | 提醒时间 | `char` | 10 | 是 | 提醒时间 |

# 泛微OA 数据表: `hrmperformancealert`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancealert`
- **字段总数**: `30`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `type_a` | 类型 | `char` | 1 | 是 | 0:开始 1：结束 |
| 3 | `yearcondition1` | 年度提醒开 | `integer` | - | 是 | 0:前 1：后 |
| 4 | `yearcondition2` | 年度提醒前后 | `integer` | - | 是 | 年度提醒前后 |
| 5 | `yearconcount` | 年度连接次数 | `integer` | - | 是 | 年度连接次数 |
| 6 | `yearalertcount` | 年度提醒次数 | `integer` | - | 是 | 年度提醒次数 |
| 7 | `yearalertunit` | 年度提醒单位 | `char` | 1 | 是 | 年度提醒单位 |
| 8 | `yearfrequency` | 年度提醒频率 | `integer` | - | 是 | 年度提醒频率 |
| 9 | `yearinterval` | 年度提醒间隔时间 | `integer` | - | 是 | 年度提醒间隔时间 |
| 10 | `monthcondition1` | 每月提醒开始 | `integer` | - | 是 | 0:开始 1：结束 |
| 11 | `monthcondition2` | 每月提醒前后 | `integer` | - | 是 | 0:前 1：后 |
| 12 | `monthconcount` | 每月连接次数 | `integer` | - | 是 | 每月连接次数 |
| 13 | `monthalertcount` | 每月提醒次数 | `integer` | - | 是 | 每月提醒次数 |
| 14 | `monthalertunit` | 每月提醒单位 | `char` | 1 | 是 | 每月提醒单位 |
| 15 | `monthfrequency` | 每月提醒频率 | `integer` | - | 是 | 每月提醒频率 |
| 16 | `monthinterval` | 每月提醒间隔时间 | `integer` | - | 是 | 每月提醒间隔时间 |
| 17 | `quartercondition1` | 季度提醒开始 | `integer` | - | 是 | 0:开始 1：结束 |
| 18 | `quartercondition2` | 季度提醒前后 | `integer` | - | 是 | 0:前 1：后 |
| 19 | `quarterconcount` | 季度连接次数 | `integer` | - | 是 | 季度连接次数 |
| 20 | `quarteralertcount` | 季度提醒次数 | `integer` | - | 是 | 季度提醒次数 |
| 21 | `quarteralertunit` | 季度提醒单位 | `char` | 1 | 是 | 季度提醒单位 |
| 22 | `quarterfrequency` | 季度提醒频率 | `integer` | - | 是 | 季度提醒频率 |
| 23 | `quarterinterval` | 季度提醒间隔时间 | `integer` | - | 是 | 季度提醒间隔时间 |
| 24 | `weekcondition1` | 每周提醒开始 | `integer` | - | 是 | 每周提醒开始 |
| 25 | `weekcondition2` | 每周提醒前后 | `integer` | - | 是 | 每周提醒前后 |
| 26 | `weekconcount` | 每周连接次数 | `integer` | - | 是 | 每周连接次数 |
| 27 | `weekalertcount` | 每周提醒次数 | `integer` | - | 是 | 每周提醒次数 |
| 28 | `weekalertunit` | 每周提醒单位 | `char` | 1 | 是 | 每周提醒单位 |
| 29 | `weekfrequency` | 每周提醒频率 | `integer` | - | 是 | 每周提醒频率 |
| 30 | `weekinterval` | 每周提醒间隔时间 | `integer` | - | 是 | 每周提醒间隔时间 |

# 泛微OA 数据表: `hrmremindmsg`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmremindmsg`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `remindtype` | 提醒类型 | `integer` | - | 是 | 提醒类型 |
| 3 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 4 | `reminddate` | 提醒日期 | `char` | 10 | 是 | 提醒日期 |
| 5 | `relatedid` | 相关id | `integer` | - | 是 | 无确定含意。如果是合同到期提醒则为合同id |

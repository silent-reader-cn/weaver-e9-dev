# 泛微OA 数据表: `social_sysremindtype`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_sysremindtype`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `remindtype` | 提醒类型id | `integer` | - | 否 | 提醒类型id |
| 3 | `remindname` | 内部提醒点击时打开的链接 | `varchar2` | 800 | 否 | 内部提醒点击时打开的链接 |
| 4 | `surl` | 内部提醒点击时打开的链接 | `varchar2` | 1000 | 是 | 内部提醒点击时打开的链接（外部提醒此栏为空） |

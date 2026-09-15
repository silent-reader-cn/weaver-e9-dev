# 泛微OA 数据表: `hrmmessagermsg`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmmessagermsg`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `jidcurrent` | 发送者 | `varchar2` | 50 | 否 | 发送者 |
| 3 | `sendto` | 接收人 | `varchar2` | 400 | 否 | 接收人 |
| 4 | `msg` | 信息 | `varchar2` | 1000 | 是 | 信息 |
| 5 | `strtime` | 发送时间 | `varchar2` | 176 | 否 | 发送时间 |

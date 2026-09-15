# 泛微OA 数据表: `mailreceiveremind`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailreceiveremind`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `name` | 提醒名称 | `varchar2` | 800 | 否 | - |
| 3 | `enable` | 是否启用 | `integer` | - | 否 | 1：启用 |
| 4 | `content` | 提醒内容 | `varchar2` | 4000 | 否 | - |
| 5 | `labelid` | 提醒名称多语言标签 | `varchar2` | 160 | 是 | - |

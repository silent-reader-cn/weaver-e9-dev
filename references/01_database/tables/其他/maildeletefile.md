# 泛微OA 数据表: `maildeletefile`

- **所属模块**: `其他`
- **数据库表名**: `maildeletefile`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | 操作人id | `integer` | - | 是 | - |
| 2 | `optdate` | 操作时间 | `varchar2` | 240 | 是 | - |
| 3 | `deletedate` | 删除时间 | `varchar2` | 240 | 是 | - |
| 4 | `mailid` | 所属邮件id | `varchar2` | 240 | 是 | - |
| 5 | `operation` | 操作类型 | `varchar2` | 2 | 是 | - |
| 6 | `id` | 主键 | `integer` | - | 否 | - |
| 7 | `mailfileid` | 邮件附件id | `integer` | - | 否 | - |
| 8 | `filerealpath` | 邮件附件存储路径 | `varchar2` | 1000 | 是 | - |
| 9 | `mdf_uuid` | 邮件附件唯一标志uuid | `varchar2` | 50 | 是 | - |

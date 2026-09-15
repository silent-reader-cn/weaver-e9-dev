# 泛微OA 数据表: `meeting_formfield`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_formfield`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 主键 | `integer` | - | 否 | 不自动增长,通过程序取 |
| 2 | `fielddbtype` | 对应数据库的类型 | `varchar2` | 320 | 是 | - |
| 3 | `fieldname` | 数据库字段名称 | `varchar2` | 240 | 是 | - |
| 4 | `sysfieldlabel` | 字段系统标签 | `varchar2` | 800 | 是 | 用于恢复标签 |
| 5 | `fieldlabel` | 字段标签 | `varchar2` | 800 | 是 | - |
| 6 | `fieldhtmltype` | 字段对应html显示类型 | `char` | 1 | 是 | - |

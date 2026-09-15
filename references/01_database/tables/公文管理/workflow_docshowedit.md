# 泛微OA 数据表: `workflow_docshowedit`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_docshowedit`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `flowid` | 流程id | `integer` | - | 是 | - |
| 3 | `selectitemid` | 选择框类型字段id | `integer` | - | 是 | - |
| 4 | `seccategoryid` | 子目录id | `varchar2` | 1000 | 是 | - |
| 5 | `modulid` | 书签id | `integer` | - | 是 | - |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 7 | `docmouldid` | 文档模板id | `integer` | - | 是 | - |
| 8 | `isdefault` | 是否是默认设置 | `char` | 1 | 是 | - |
| 9 | `dateshowtype` | 日期显示类型 | `char` | 1 | 是 | - |

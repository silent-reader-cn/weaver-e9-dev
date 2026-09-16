# 泛微OA 数据表: `workflow_docshowedit`

- **中文名称**: 流程表单字段与编辑模板书签对应关系表
- **所属模块**: `公文管理`
- **数据库表名**: `workflow_docshowedit`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `flowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `selectitemid` | 选择框类型字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `seccategoryid` | 子目录id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `modulid` | 书签id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `docmouldid` | 文档模板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `isdefault` | 是否是默认设置 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `dateshowtype` | 日期显示类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |

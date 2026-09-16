# 泛微OA 数据表: `docsenddocdetail`

- **中文名称**: 废弃
- **所属模块**: `知识管理`
- **数据库表名**: `docsenddocdetail`
- **主键**: `id`
- **字段数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `subject` | 主题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `docids` | 文档id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `dockind` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `docinstancylevel` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `docsecretlevel` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `docnumber_1` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `docnumberyear_1` | 无 | `char` | 5 | 是 | 否 | 否 | - | - | - |
| 9 | `docnumberissue_1` | 无 | `char` | 5 | 是 | 否 | 否 | - | - | - |
| 10 | `docnumber_2` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `docnumberyear_2` | 无 | `char` | 5 | 是 | 否 | 否 | - | - | - |
| 12 | `docnumberissue_2` | 无 | `char` | 5 | 是 | 否 | 否 | - | - | - |
| 13 | `senddate` | 无 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 14 | `senddepartment` | 无 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 15 | `department_1` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `department_2` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `department_3` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `department_4` | 无 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `signer` | 无 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `signdate` | 无 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `requestlog` | 无 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 22 | `status` | 无 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `createdate` | 无 | `char` | 10 | 是 | 否 | 否 | - | - | - |

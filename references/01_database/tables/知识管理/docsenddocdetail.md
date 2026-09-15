# 泛微OA 数据表: `docsenddocdetail`

- **所属模块**: `知识管理`
- **数据库表名**: `docsenddocdetail`
- **字段总数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `subject` | 主题 | `varchar2` | 1000 | 是 | - |
| 3 | `docids` | 文档id | `varchar2` | 800 | 是 | - |
| 4 | `dockind` | 无 | `varchar2` | 1000 | 是 | - |
| 5 | `docinstancylevel` | 无 | `varchar2` | 1000 | 是 | - |
| 6 | `docsecretlevel` | 无 | `varchar2` | 1000 | 是 | - |
| 7 | `docnumber_1` | 无 | `varchar2` | 1000 | 是 | - |
| 8 | `docnumberyear_1` | 无 | `char` | 5 | 是 | - |
| 9 | `docnumberissue_1` | 无 | `char` | 5 | 是 | - |
| 10 | `docnumber_2` | 无 | `varchar2` | 1000 | 是 | - |
| 11 | `docnumberyear_2` | 无 | `char` | 5 | 是 | - |
| 12 | `docnumberissue_2` | 无 | `char` | 5 | 是 | - |
| 13 | `senddate` | 无 | `char` | 10 | 是 | - |
| 14 | `senddepartment` | 无 | `varchar2` | 800 | 是 | - |
| 15 | `department_1` | 无 | `varchar2` | 1000 | 是 | - |
| 16 | `department_2` | 无 | `varchar2` | 1000 | 是 | - |
| 17 | `department_3` | 无 | `varchar2` | 1000 | 是 | - |
| 18 | `department_4` | 无 | `varchar2` | 1000 | 是 | - |
| 19 | `signer` | 无 | `integer` | - | 是 | - |
| 20 | `signdate` | 无 | `char` | 10 | 是 | - |
| 21 | `requestlog` | 无 | `varchar2` | 4000 | 是 | - |
| 22 | `status` | 无 | `char` | 1 | 是 | - |
| 23 | `createdate` | 无 | `char` | 10 | 是 | - |

# 泛微OA 数据表: `workflowtofinanceurlold`

- **中文名称**: 废弃表
- **所属模块**: `工作流程`
- **数据库表名**: `workflowtofinanceurlold`
- **主键**: `id`
- **字段数**: `12`

> 说明：废弃表不再使用

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `guid1` | guid1 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 3 | `sendurl` | sendurl | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `requestid` | requestid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `requestids` | requestids | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `fnavoucherxmlid` | fnavoucherxmlid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `xmlsend` | xmlsend | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `xmlreceive` | xmlreceive | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `xmlobjsend` | xmlobjsend | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 10 | `xmlobjreceive` | xmlobjreceive | `blob` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `createdate` | createdate | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `createtime` | createtime | `char` | 8 | 是 | 否 | 否 | - | - | - |

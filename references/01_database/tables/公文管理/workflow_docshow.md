# 泛微OA 数据表: `workflow_docshow`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_docshow`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `flowid` | 流程id | `integer` | - | 是 | - |
| 2 | `selectitemid` | 选择框选择项id | `integer` | - | 是 | - |
| 3 | `seccategoryid` | 二级目录id | `varchar2` | 1000 | 是 | - |
| 4 | `modulid` | 显示模版标签id | `integer` | - | 是 | - |
| 5 | `fieldid` | 表单字段id | `integer` | - | 是 | - |
| 6 | `docmouldid` | 文档模版id | `integer` | - | 是 | - |
| 7 | `isdefault` | 是否默认 | `char` | 1 | 否 | 1：是，0或其他为否 |
| 8 | `dateshowtype` | 日期显示类型 | `char` | 1 | 是 | 1：大写，2：小写，0：其它 |

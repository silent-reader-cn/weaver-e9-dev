# 泛微OA 数据表: `workflow_selectitemobj`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_selectitemobj`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 3 | `isbill` | 是否为单据 | `integer` | - | 是 | - |
| 4 | `selectvalue` | 可选择的值 | `integer` | - | 是 | - |
| 5 | `objid` | 对象id | `integer` | - | 是 | - |
| 6 | `objtype` | 对象类型 | `char` | 1 | 是 | - |
| 7 | `docpath` | 文档路径 | `varchar2` | 1000 | 是 | - |
| 8 | `doccategory` | 文档分类 | `varchar2` | 1000 | 是 | - |

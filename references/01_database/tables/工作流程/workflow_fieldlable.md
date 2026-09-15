# 泛微OA 数据表: `workflow_fieldlable`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fieldlable`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formid` | 表单id | `integer` | - | 否 | - |
| 2 | `fieldid` | 表单字段id | `integer` | - | 否 | - |
| 3 | `fieldlable` | 表单字段显示名 | `varchar2` | 800 | 是 | - |
| 4 | `langurageid` | 显示语言 | `integer` | - | 是 | - |
| 5 | `isdefault` | 该语言是否为默认语言 | `char` | 1 | 是 | - |

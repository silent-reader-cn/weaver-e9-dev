# 泛微OA 数据表: `workflow_datainput_table`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_datainput_table`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `datainputid` | 触发表id | `integer` | - | 是 | - |
| 3 | `tablename` | 关联数据表名 | `varchar2` | 320 | 是 | - |
| 4 | `alias` | 关联数据表名-别名 | `varchar2` | 80 | 是 | - |
| 5 | `formid` | 表单id | `varchar2` | 800 | 是 | - |

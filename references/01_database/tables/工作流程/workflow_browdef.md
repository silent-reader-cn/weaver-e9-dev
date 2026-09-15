# 泛微OA 数据表: `workflow_browdef`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browdef`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `workflowid` | 流程id | `number` | (38,0) | 否 | - |
| 2 | `fieldid` | 字段id | `number` | (38,0) | 否 | - |
| 3 | `viewtype` | 字段种类 | `number` | (38,0) | 否 | 0表示主字段；1表示明细字段 |
| 4 | `fieldtype` | 字段类型 | `number` | (38,0) | 否 | - |
| 5 | `title` | 标题 | `varchar2` | 1000 | 否 | - |

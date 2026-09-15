# 泛微OA 数据表: `workflow_textinfo`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_textinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `x` | x坐标 | `varchar2` | 10 | 是 | - |
| 4 | `y` | y坐标 | `varchar2` | 10 | 是 | - |
| 5 | `width` | 宽度 | `varchar2` | 10 | 是 | - |
| 6 | `height` | 高度 | `varchar2` | 10 | 是 | - |
| 7 | `textvalue` | 数据值 | `varchar2` | 4000 | 是 | - |

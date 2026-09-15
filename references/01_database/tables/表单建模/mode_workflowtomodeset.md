# 泛微OA 数据表: `mode_workflowtomodeset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_workflowtomodeset`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `conditionsql` | 触发sql | `varchar2` | 4000 | 是 | - |
| 2 | `conditiontext` | 触发内容 | `varchar2` | 4000 | 是 | - |
| 3 | `uuid` | uuid | `varchar2` | 800 | 是 | - |
| 4 | `remark` | 备注 | `varchar2` | 1000 | 是 | - |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 7 | `workflowid` | 流程类型 | `integer` | - | 是 | 工作流程id，对应workflow_base表的id |
| 8 | `modecreater` | 模块创建人 | `integer` | - | 是 | - |

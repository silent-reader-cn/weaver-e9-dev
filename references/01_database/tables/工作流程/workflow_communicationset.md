# 泛微OA 数据表: `workflow_communicationset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationset`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `doc` | 相关文档 | `integer` | - | 是 | - |
| 2 | `wf` | 相关流程 | `integer` | - | 是 | - |
| 3 | `custom` | 相关客户 | `integer` | - | 是 | - |
| 4 | `project` | 相关项目 | `integer` | - | 是 | - |
| 5 | `task` | 相关日无 | `integer` | - | 是 | - |
| 6 | `acc` | 相关附件 | `integer` | - | 是 | - |
| 7 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 8 | `acccatelog` | 附件上传目录 | `varchar2` | 100 | 是 | - |

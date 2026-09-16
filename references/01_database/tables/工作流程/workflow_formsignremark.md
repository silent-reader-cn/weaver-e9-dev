# 泛微OA 数据表: `workflow_formsignremark`

- **中文名称**: 工作流程表单签章记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formsignremark`
- **主键**: `id`
- **字段数**: `4`

> 说明：工作流程表单签章记录

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestlogid` | 日志id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_requestlog表的requestlogid |
| 3 | `imagefileid` | 图片id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `remark` | 表单签章数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

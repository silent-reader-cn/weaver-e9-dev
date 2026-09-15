# 泛微OA 数据表: `exp_workflowxml`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_workflowxml`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `rgworkflowid` | 注册流程列表里的id | `integer` | - | 是 | exp_workflowDetail表里的id |
| 3 | `xmltext` | xml格式内容 | `clob` | 4000 | 是 | - |

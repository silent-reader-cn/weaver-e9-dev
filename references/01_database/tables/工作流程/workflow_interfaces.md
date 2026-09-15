# 泛微OA 数据表: `workflow_interfaces`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_interfaces`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 否 | - |
| 3 | `deploy_status` | 部署状态 | `varchar2` | 8 | 是 | - |
| 4 | `memo` | 备注 | `varchar2` | 1000 | 是 | - |
| 5 | `closed` | 关闭 | `varchar2` | 8 | 是 | - |

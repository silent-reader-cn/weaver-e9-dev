# 泛微OA 数据表: `workflow_interfaces`

- **中文名称**: 流程接口表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_interfaces`
- **主键**: `id`
- **字段数**: `5`

> 说明：admincenter/interfaces/interfaceList.jsp 使用

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `name` | 名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 3 | `deploy_status` | 部署状态 | `varchar2` | 8 | 是 | 否 | 否 | - | 0 | - |
| 4 | `memo` | 备注 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `closed` | 关闭 | `varchar2` | 8 | 是 | 否 | 否 | - | 0 | - |

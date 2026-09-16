# 泛微OA 数据表: `workflow_agenttemplate`

- **中文名称**: 流程代理模板设置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agenttemplate`
- **主键**: `id`
- **字段数**: `11`

> 说明：流程代理模板设置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `name` | 名字 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `beagenterid` | 被代理人id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `agenterid` | 代理人id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `userselect` | userselect | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `rangeselect` | rangeselect | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `workflowrange` | 流程范围 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 8 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `iscreateagenter` | 是否代理创建 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 10 | `isproxydeal` | 是否代理明细 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |
| 11 | `ispending` | 是否代理处理中的流程 | `char` | 1 | 是 | 否 | 否 | - | 0 | - |

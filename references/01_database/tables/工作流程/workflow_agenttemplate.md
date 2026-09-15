# 泛微OA 数据表: `workflow_agenttemplate`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_agenttemplate`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `name` | 名字 | `varchar2` | 1000 | 是 | - |
| 3 | `beagenterid` | 被代理人id | `integer` | - | 否 | - |
| 4 | `agenterid` | 代理人id | `integer` | - | 否 | - |
| 5 | `userselect` | userselect | `varchar2` | 400 | 是 | - |
| 6 | `rangeselect` | rangeselect | `char` | 1 | 是 | - |
| 7 | `workflowrange` | 流程范围 | `varchar2` | 4000 | 是 | - |
| 8 | `creater` | 创建人 | `integer` | - | 是 | - |
| 9 | `iscreateagenter` | 是否代理创建 | `char` | 1 | 是 | - |
| 10 | `isproxydeal` | 是否代理明细 | `char` | 1 | 是 | - |
| 11 | `ispending` | 是否代理处理中的流程 | `char` | 1 | 是 | - |

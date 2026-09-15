# 泛微OA 数据表: `dmlactionset`

- **所属模块**: `集成模块`
- **数据库表名**: `dmlactionset`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `dmlactionname` | 名称 | `varchar2` | 1000 | 否 | - |
| 3 | `dmlorder` | 执行顺序 | `integer` | - | 是 | - |
| 4 | `workflowid` | 流程类型id | `integer` | - | 是 | - |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 6 | `ispreoperator` | ispreoperator | `char` | 1 | 是 | - |
| 7 | `nodelinkid` | nodelinkid | `integer` | - | 是 | - |
| 8 | `datasourceid` | 数据源 | `varchar2` | 1000 | 是 | 数据源id |
| 9 | `dmltype` | dml类型 | `varchar2` | 80 | 是 | - |

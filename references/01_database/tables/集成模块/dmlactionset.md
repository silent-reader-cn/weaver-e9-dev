# 泛微OA 数据表: `dmlactionset`

- **中文名称**: nset(DML接口动作基本信息
- **所属模块**: `集成模块`
- **数据库表名**: `dmlactionset`
- **主键**: `id`
- **字段数**: `10`

> 说明：dmlactionset

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `dmlactionname` | 名称 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | - |
| 3 | `dmlorder` | 执行顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `workflowid` | 流程类型id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `ispreoperator` | ispreoperator | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `nodelinkid` | nodelinkid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `datasourceid` | 数据源 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 数据源id |
| 9 | `dmltype` | dml类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | insert：insert操作<br>update：update操作<br>delete：delete操作 |
| 10 | `typename` | typename | `char` | 1 | 是 | 否 | 否 | - | - | - |

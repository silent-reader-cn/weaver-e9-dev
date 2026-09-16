# 泛微OA 数据表: `mode_workflowtomodesetopt`

- **中文名称**: 流程转数据子表操作设置
- **所属模块**: `表单建模`
- **数据库表名**: `mode_workflowtomodesetopt`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `mainid` | 流程转数据主id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_workflowtomodeset表的id |
| 3 | `detailtablename` | 明细表表名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `opttype` | 明细表操作类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | 1：默认<br>2：追加<br>3：更新<br>4：更新(追加)<br>5：覆盖 |
| 5 | `updatecondition` | 明细表更新条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `wherecondition` | 更新条件 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

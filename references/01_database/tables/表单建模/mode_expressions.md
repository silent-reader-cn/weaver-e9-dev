# 泛微OA 数据表: `mode_expressions`

- **中文名称**: 权限条件关系表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_expressions`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `searchtransmethodid` | 查询id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `rightid` | 权限设置id | `integer` | - | 是 | 否 | 否 | - | - | 对应moderightinfo表中的id |
| 4 | `relation` | 关系 | `integer` | - | 是 | 否 | 否 | - | - | 0：or的关系<br>1：and的关系 |
| 5 | `expids` | 包含的下级ids | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 对应本表中的id，多个下级id用逗号隔开 |
| 6 | `expbaseid` | 权限条件关系详细id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_expressionbase表中的id |
| 7 | `workflowtomodeid` | 流程节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `triggerworkflowsetid` | 触发节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `uuid` | uuid | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 10 | `remindid` | 提醒id | `integer` | - | 是 | 否 | 否 | - | - | - |

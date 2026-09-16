# 泛微OA 数据表: `mode_dmlactionfieldmap`

- **中文名称**: DML配置字段映射表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_dmlactionfieldmap`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `actionsqlsetid` | dml接口动作详细信息id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_dmlactionsqlset表的id |
| 3 | `maptype` | 操作类型 | `char` | 1 | 是 | 否 | 否 | - | - | 0：赋值设置<br>1：触发条件设置 |
| 4 | `fieldname` | 字段名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 数据库对应的字段名 |
| 5 | `fieldvalue` | 同步对应字段/条件对应字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 同步对应字段/条件对应字段，数据库对应的字段名 |
| 6 | `fieldtype` | 字段类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 字段类型，和workflow_billfield表中的fielddbtype存储的值相同。 |

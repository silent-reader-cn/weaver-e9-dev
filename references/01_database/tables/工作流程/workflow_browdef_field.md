# 泛微OA 数据表: `workflow_browdef_field`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browdef_field`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `configid` | 配置id | `number` | (38,0) | 否 | - |
| 2 | `workflowid` | 流程id | `number` | (38,0) | 否 | - |
| 3 | `fieldid` | 字段id | `number` | (38,0) | 否 | - |
| 4 | `viewtype` | 字段种类 | `number` | (38,0) | 否 | 0表示主字段；1表示明细字段 |
| 5 | `showorder` | 显示顺序 | `varchar2` | 800 | 否 | - |
| 6 | `hide` | 隐藏 | `char` | 1 | 是 | - |
| 7 | `readonly` | 只读 | `char` | 1 | 是 | - |
| 8 | `canselectvalues` | 可以选择的值 | `varchar2` | 1000 | 是 | - |
| 9 | `valuetype` | 值的类型 | `varchar2` | 1000 | 是 | - |
| 10 | `value` | 值 | `varchar2` | 1000 | 是 | - |

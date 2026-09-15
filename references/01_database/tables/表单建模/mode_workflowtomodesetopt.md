# 泛微OA 数据表: `mode_workflowtomodesetopt`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_workflowtomodesetopt`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `mainid` | 流程转数据主id | `integer` | - | 是 | 对应mode_workflowtomodeset表的id |
| 3 | `detailtablename` | 明细表表名 | `varchar2` | 1000 | 是 | - |
| 4 | `opttype` | 明细表操作类型 | `varchar2` | 8 | 是 | - |

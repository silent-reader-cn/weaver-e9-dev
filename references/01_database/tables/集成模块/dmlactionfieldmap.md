# 泛微OA 数据表: `dmlactionfieldmap`

- **所属模块**: `集成模块`
- **数据库表名**: `dmlactionfieldmap`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `actionsqlsetid` | dml接口动作详细信息id | `integer` | - | 是 | 对应mode_dmlactionsqlset表的id |
| 3 | `maptype` | 操作类型 | `char` | 1 | 是 | - |

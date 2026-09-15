# 泛微OA 数据表: `mode_deletelogdetail`

- **所属模块**: `其他`
- **数据库表名**: `mode_deletelogdetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `logid` | 日志id | `integer` | - | 是 | - |
| 3 | `itemtype` | 相关类型 | `varchar2` | 160 | 是 | - |
| 4 | `itemid` | 相关id | `integer` | - | 是 | - |
| 5 | `itemname` | 相关名称 | `varchar2` | 1000 | 是 | - |
| 6 | `itemrelatedtablename` | 相关关系与表名称 | `varchar2` | 1000 | 是 | - |

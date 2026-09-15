# 泛微OA 数据表: `actionsettingdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `actionsettingdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 无 |
| 2 | `actionid` | 接口动作名称 | `integer` | - | 是 | 无 |
| 3 | `attrname` | 参数名称 | `varchar2` | 1000 | 是 | 无 |
| 4 | `attrvalue` | 参数值 | `varchar2` | 1000 | 是 | 无 |
| 5 | `isdatasource` | 是否是数据源 | `char` | 1 | 是 | 无 |

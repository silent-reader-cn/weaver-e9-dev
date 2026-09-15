# 泛微OA 数据表: `schedulesettingdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `schedulesettingdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `scheduledbid` | 计划任务id | `integer` | - | 是 | 计划任务id |
| 3 | `attrname` | 参数名称 | `varchar2` | 1000 | 是 | 参数名称 |
| 4 | `attrvalue` | 参数值 | `varchar2` | 1000 | 是 | 参数值 |
| 5 | `isdatasource` | 是否数据源 | `integer` | - | 是 | 是否数据源；0：否；1：是； |

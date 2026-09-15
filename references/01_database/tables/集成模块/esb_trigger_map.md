# 泛微OA 数据表: `esb_trigger_map`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_trigger_map`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布服务标识 | `varchar2` | 800 | 是 | 发布服务标识 |
| 2 | `triggerid` | 服务方式标识 | `varchar2` | 800 | 是 | 服务方式标识 |
| 3 | `paramkey` | 参数名 | `varchar2` | 800 | 是 | 参数名 |
| 4 | `fieldvalue` | 参数值 | `varchar2` | 800 | 是 | 参数值 |
| 5 | `fieldtype` | 参数类型 | `integer` | - | 是 | 参数类型 |

# 泛微OA 数据表: `outerdatawfdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawfdetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `outermaintable` | 外部主表名称 | `varchar2` | 1000 | 是 | 外部主表名称 |
| 2 | `mainid` | 主键列名称 | `integer` | - | 是 | 主键列名称 |
| 3 | `workflowid` | 流程id | `integer` | - | 是 | 流程id |
| 4 | `requestid` | 请求id | `integer` | - | 是 | 请求id |
| 5 | `keyfieldvalue` | 外部关键字段值 | `varchar2` | 1000 | 是 | 外部关键字段值 |
| 6 | `ftriggerflag` | 触发标识 | `char` | 1 | 是 | 触发标识 |

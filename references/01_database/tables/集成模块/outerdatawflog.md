# 泛微OA 数据表: `outerdatawflog`

- **中文名称**: 外部流程触发日志记录表
- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawflog`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 否 | 是 | - | - | 自增长主键 |
| 2 | `outerdatawfid` | outerdatawset表id | `integer` | - | 是 | 否 | 否 | - | - | outerdatawset表id |
| 3 | `outkey` | 外部主键 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 外部主键 |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | 否 | 否 | - | - | 流程id |
| 5 | `requestid` | 生成流程的唯一标识 | `integer` | - | 是 | 否 | 否 | - | - | 生成流程的唯一标识 |
| 6 | `triggerflag` | 触发标识 | `integer` | - | 是 | 否 | 否 | - | - | 触发标识 |
| 7 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 创建日期 |
| 8 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 创建时间 |

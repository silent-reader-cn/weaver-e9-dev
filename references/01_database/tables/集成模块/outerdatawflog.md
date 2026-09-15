# 泛微OA 数据表: `outerdatawflog`

- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawflog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 自增长主键 |
| 2 | `outerdatawfid` | outerdatawset表id | `integer` | - | 是 | outerdatawset表id |
| 3 | `outkey` | 外部主键 | `varchar2` | 800 | 是 | 外部主键 |
| 4 | `workflowid` | 流程id | `integer` | - | 是 | 流程id |
| 5 | `requestid` | 生成流程的唯一标识 | `integer` | - | 是 | 生成流程的唯一标识 |
| 6 | `triggerflag` | 触发标识 | `integer` | - | 是 | 触发标识 |
| 7 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 8 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |

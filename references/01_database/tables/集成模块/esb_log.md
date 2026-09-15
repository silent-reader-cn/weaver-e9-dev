# 泛微OA 数据表: `esb_log`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_log`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布标识 | `varchar2` | 800 | 是 | 发布标识 |
| 2 | `triggerid` | 触发标识 | `varchar2` | 800 | 是 | 触发标识 |
| 3 | `runtime` | 运行时间 | `integer` | - | 是 | 运行时间 |
| 4 | `starttime` | 开始时间 | `varchar2` | 160 | 是 | 开始时间 |
| 5 | `endtime` | 结束时间 | `varchar2` | 160 | 是 | 结束时间 |
| 6 | `runstate` | 执行状态 | `char` | 1 | 是 | 执行状态（1:成功，0:失败） |
| 7 | `description` | 说明 | `clob` | 4000 | 是 | 记录报文信息 |
| 8 | `triggerkey` | 触发关键词 | `varchar2` | 800 | 是 | 触发关键词 |
| 9 | `batchkey` | 批次号 | `varchar2` | 240 | 是 | 批次号 |

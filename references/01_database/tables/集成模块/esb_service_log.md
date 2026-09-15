# 泛微OA 数据表: `esb_service_log`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_service_log`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布服务标识 | `varchar2` | 800 | 是 | 发布服务标识 |
| 2 | `serviceid` | 注册服务标识 | `varchar2` | 800 | 是 | 注册服务标识 |
| 3 | `resourceid` | 资源标识 | `varchar2` | 800 | 是 | 资源标识 |
| 4 | `triggerid` | 触发标识 | `varchar2` | 800 | 是 | 触发标识 |
| 5 | `runtime` | 运行时间 | `integer` | - | 是 | 运行时间 |
| 6 | `starttime` | 开始时间 | `varchar2` | 160 | 是 | 开始时间 |
| 7 | `endtime` | 结束时间 | `varchar2` | 160 | 是 | 结束时间 |
| 8 | `runstate` | 运行状态 | `char` | 1 | 是 | 运行状态（1:成功，0:失败） |
| 9 | `description` | 说明 | `clob` | 4000 | 是 | 返回报文信息 |
| 10 | `triggerkey` | 触发关键词 | `varchar2` | 800 | 是 | 触发关键词 |
| 11 | `batchkey` | 批次号 | `varchar2` | 240 | 是 | 批次号 |
| 12 | `params` | 请求参数 | `clob` | 4000 | 是 | 请求参数报文 |

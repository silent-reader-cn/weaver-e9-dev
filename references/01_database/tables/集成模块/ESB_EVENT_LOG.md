# 泛微OA 数据表: `ESB_EVENT_LOG`

- **所属模块**: `集成模块`
- **数据库表名**: `ESB_EVENT_LOG`
- **文档收录字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `batchkey` | 批次号 | `varchar2` | 240 | - | - |
| 2 | `eventid` | 事件标识 | `varchar2` | 100 | - | - |
| 3 | `eventtime` | 触发时间 | `varchar2` | 100 | - | - |
| 4 | `eventsate` | 触发状态 | `varchar2` | 100 | - | - |
| 5 | `requestParams` | 触发数据 | `clob` | - | - | - |
| 6 | `responseParams` | 响应数据 | `clob` | - | - | - |
| 7 | `clientIp` | 触发客户端IP | `varchar2` | 100 | - | - |

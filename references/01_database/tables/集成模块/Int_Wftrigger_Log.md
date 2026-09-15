# 泛微OA 数据表: `Int_Wftrigger_Log`

- **所属模块**: `集成模块`
- **数据库表名**: `Int_Wftrigger_Log`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 无 |
| 2 | `trgid` | 触发设置标识 | `integer` | - | 是 | 无 |
| 3 | `wfid` | 流程标识 | `integer` | - | 是 | 无 |
| 4 | `requestid` | 触发出来的流程请求标识 | `integer` | - | 是 | 无 |
| 5 | `requestname` | 触发出来的流程请求标题 | `varchar2` | 500 | 是 | 无 |
| 6 | `opttime` | 操作时间 | `varchar2` | 100 | 是 | 无 |
| 7 | `result` | 触发结果 | `integer` | - | 是 | 1,成功;0,失败 |
| 8 | `clientip` | 客户端IP | `varchar2` | 100 | 是 | 无 |
| 9 | `serverip` | 服务端IP | `varchar2` | 100 | 是 | 无 |
| 10 | `summary` | 触发结果简要信息 | `varchar2` | 2000 | 是 | 无 |
| 11 | `fail_summary` | 触发失败原因信息 | `varchar2` | 2000 | 是 | 无 |

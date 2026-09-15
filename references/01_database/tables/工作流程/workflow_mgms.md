# 泛微OA 数据表: `workflow_mgms`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_mgms`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | - |
| 4 | `receivedate` | 接收日期 | `varchar2` | 80 | 是 | - |
| 5 | `receivetime` | 接收时间 | `varchar2` | 80 | 是 | - |
| 6 | `sendtime` | 发送时间 | `varchar2` | 160 | 是 | - |
| 7 | `transactionid` | 处理id | `varchar2` | 1000 | 是 | - |
| 8 | `previoustrsid` | 上次流水号记录 | `varchar2` | 1000 | 是 | - |
| 9 | `status` | 状态 | `varchar2` | 8 | 是 | - |
| 10 | `processtrsid` | 进行中的流水号记录 | `varchar2` | 1000 | 是 | 流水号 |

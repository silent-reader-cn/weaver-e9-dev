# 泛微OA 数据表: `workflow_requestoperatelog`

- **中文名称**: 流程操作记录日志主表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestoperatelog`
- **主键**: `id`
- **字段数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `detailinfo` | 明细JSON数据 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `retype` | 操作类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `reoperatorid` | 被代理人ID | `varchar2` | 20 | 是 | 否 | 否 | - | - | - |
| 4 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `nodeid` | 节点id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isremark` | 操作状态 | `integer` | - | 是 | 否 | 否 | - | - | 与workflow_currentoperator表中的isremark是不同的 |
| 8 | `operatorid` | 操作人id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `operatortype` | 操作人类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 11 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 12 | `operatetype` | 操作类型 | `varchar2` | 200 | 是 | 否 | 否 | - | - | 提交 submit, 1<br>退回 reject，2<br>干预 intervenor，3<br>转办 trans，4<br>意见征询 take，5<br>转发 forward，-2<br>强制归档 forceover，9 |
| 13 | `operatename` | 操作类型中文名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `operatecode` | 操作类型代码 | `integer` | - | 是 | 否 | 否 | - | - | 1：提交 submit<br>2：退回 reject<br>3：干预 intervenor<br>4：转办 trans<br>5：意见征询 take<br>-2：转发 forward<br>9：强制归档 forceover |
| 15 | `isinvalid` | 是否执行了强制收回 | `char` | 1 | 是 | 否 | 否 | - | - | 1：无效操作，操作被强制收回<br>其他：有效的操作 |
| 16 | `invalidid` | 执行强制收回的用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `invaliddate` | 强制收回操作日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 18 | `invalidtime` | 强制收回操作时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |

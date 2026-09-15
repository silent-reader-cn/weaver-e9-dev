# 泛微OA 数据表: `ofs_log`

- **所属模块**: `其他`
- **数据库表名**: `ofs_log`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `logid` | 自增长序列 | `integer` | - | 否 | 自增长序列 |
| 2 | `sysid` | 异构系统id | `integer` | - | 否 | 异构系统id |
| 3 | `datatype` | 数据类型 | `varchar2` | 80 | 是 | OtherSys：异构系统 WfType：流程类型 WfData：流程数据 SetParam：参数设置 |
| 4 | `opertype` | 操作类型 | `varchar2` | 80 | 是 | AutoNew：自动创建 New：新建 AutoEdit：自动更新 Edit：编辑 Del：删除 Check：检测 Set：设置 |
| 5 | `operresult` | 操作结果 | `integer` | - | 是 | 1：成功 0：失败 |
| 6 | `failremark` | 失败说明 | `varchar2` | 1000 | 是 | 失败说明 |
| 7 | `syscode` | 异构系统标识 | `varchar2` | 1000 | 是 | 异构系统标识 |
| 8 | `flowid` | 异构系统的流程任务id | `varchar2` | 1000 | 是 | 异构系统的流程任务id |
| 9 | `requestname` | 异构系统的流程标题 | `varchar2` | 1000 | 是 | 异构系统的流程标题 |
| 10 | `workflowname` | 异构系统流程类型名称 | `varchar2` | 1000 | 是 | 异构系统流程类型名称 |
| 11 | `nodename` | 节点名称 | `varchar2` | 1000 | 是 | 节点名称 |
| 12 | `isremark` | 流程处理状态 | `integer` | - | 是 | 0：待办，初始状态 2：已办 4：办结（归档） |
| 13 | `pcurl` | 异构系统PC端访问路径 | `varchar2` | 2000 | 是 | 异构系统PC端访问路径 |
| 14 | `appurl` | 异构系统移动端访问路径 | `varchar2` | 2000 | 是 | 异构系统移动端访问路径 |
| 15 | `creator` | 创建人 | `varchar2` | 1000 | 是 | 创建人原始数据 |
| 16 | `creatorid` | 创建人id | `integer` | - | 是 | 创建人id |
| 17 | `createdate` | 创建日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 创建日期，格式：yyyy-MM-dd |
| 18 | `createtime` | 创建时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 创建时间，格式：hh24:mm:ss |
| 19 | `receiver` | 接收人（原值） | `varchar2` | 1000 | 是 | 接收人（原值） |
| 20 | `userid` | 接收人（OAid） | `integer` | - | 是 | 接收人（OAid） |
| 21 | `receivedate` | 消息接收的日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 消息接收的日期，格式：yyyy-MM-dd |
| 22 | `receivetime` | 消息接收的时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 消息接收的时间，格式：hh24:mm:ss |
| 23 | `dataid` | 流程类型id | `integer` | - | 是 | dataType =WfType，对应Ofs_workflow表的id； dataType = WfData，对应Ofs_todo_data表的id； |
| 24 | `operatedate` | 操作的日期，格式：yyyy-MM-dd | `char` | 10 | 是 | 操作的日期，格式：yyyy-MM-dd |
| 25 | `operatetime` | 操作的时间，格式：hh24:mm:ss | `char` | 8 | 是 | 操作的时间，格式：hh24:mm:ss |

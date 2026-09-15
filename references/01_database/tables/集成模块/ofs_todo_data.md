# 泛微OA 数据表: `ofs_todo_data`

- **所属模块**: `集成模块`
- **数据库表名**: `ofs_todo_data`
- **字段总数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `receivets` | 时间戳 | `varchar2` | 800 | 是 | 时间戳 |
| 2 | `pcurlsrc` | 异构系统pc访问地址 | `varchar2` | 2000 | 是 | 异构系统pc访问地址，没有中转页面为空 |
| 3 | `appurlsrc` | 异构系统移动端访问地址 | `varchar2` | 2000 | 是 | 异构系统移动端访问地址，没有中转页面为空 |
| 4 | `isremark` | 流程处理状态 | `char` | 1 | 是 | 0：待办，初始状态 2：已办 4：办结（归档） |
| 5 | `id` | 自增长序列 | `integer` | - | 否 | 自增长序列 |
| 6 | `syscode` | 异构系统标识 | `varchar2` | 1000 | 是 | 异构系统标识 |
| 7 | `sysid` | 异构系统id | `integer` | - | 否 | 异构系统id |
| 8 | `flowid` | 异构系统的流程实例id | `varchar2` | 1000 | 是 | 异构系统的流程实例id |
| 9 | `flowguid` | 异构系统的流程GUID | `varchar2` | 1000 | 是 | 异构系统的流程GUID（syscode + workflowid + flowid + receiver） 分隔符用+ |
| 10 | `requestid` | 逻辑自增长序列（负增长） | `integer` | - | 否 | 逻辑自增长序列（负增长） |
| 11 | `requestname` | 异构系统的流程标题 | `varchar2` | 1000 | 是 | 异构系统的流程标题 |
| 12 | `workflowname` | 异构系统流程类型名称 | `varchar2` | 1000 | 是 | 异构系统流程类型名称 |
| 13 | `workflowid` | 异构系统流程类型id | `integer` | - | 是 | 异构系统流程类型id |
| 14 | `nodename` | 异构系统的步骤（节点）名称 | `varchar2` | 1000 | 是 | 异构系统的步骤（节点）名称 |
| 15 | `viewtype` | 流程查看状态 | `integer` | - | 是 | 流程查看状态 0：接收到流程且未查看过，显示红色new标记； -2：已查看过流程，不显示任何new标记； |
| 16 | `islasttimes` | 是否最后一次操作 | `integer` | - | 是 | 0：操作人在流程中多次出现，且本条记录不是操作人最后一次操作所用的纪录； 1：操作人在流程中出现一次；或操作人在流程中多次出现，且本条记录是操作人最后一次操作所用的纪录； |
| 17 | `iscomplete` | 是否归档 | `integer` | - | 是 | 0:未归档， 1:归档 |
| 18 | `pcurl` | 异构系统pc访问地址 | `varchar2` | 2000 | 是 | 异构系统pc访问地址，有中转页面配置的情况下是中转页面地址 |
| 19 | `appurl` | 异构系统移动端访问地址 | `varchar2` | 2000 | 是 | 异构系统移动端访问地址，有中转页面配置的情况下是中转页面地址 |
| 20 | `creator` | 创建人 | `varchar2` | 1000 | 是 | 创建人（原值） |
| 21 | `creatorid` | 创建人id | `integer` | - | 是 | 创建人id（OAid） |
| 22 | `createdate` | 流程创建的日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 流程创建的日期，格式：yyyy-MM-dd |
| 23 | `createtime` | 流程创建的时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 流程创建的时间，格式：hh24:mm:ss |
| 24 | `receiver` | 接收人（原值） | `varchar2` | 1000 | 是 | 接收人（原值） |
| 25 | `userid` | 接收人（OAid） | `integer` | - | 是 | 接收人（OAid） |
| 26 | `receivedate` | 消息接收的日期，格式：yyyy-MM-dd | `varchar2` | 80 | 是 | 消息接收的日期，格式：yyyy-MM-dd |
| 27 | `receivetime` | 消息接收的时间，格式：hh24:mm:ss | `varchar2` | 80 | 是 | 消息接收的时间，格式：hh24:mm:ss |
| 28 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | 操作日期 未查看时为空； 查看后记录第一次查看时间； 操作后记录操作时间；格式：yyyy-MM-dd |
| 29 | `operatetime` | 操作时间 | `varchar2` | 64 | 是 | 未查看时为空； 查看后记录第一次查看时间； 操作后记录操作时间；格式：hh24:mm:ss |

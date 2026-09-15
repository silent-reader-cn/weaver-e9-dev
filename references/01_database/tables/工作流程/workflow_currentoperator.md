# 泛微OA 数据表: `workflow_currentoperator`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_currentoperator`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isprocessing` | 流程异步处理状态 | `char` | 1 | 是 | - |
| 2 | `processuser` | 实际操作人 | `integer` | - | 是 | - |
| 3 | `autodate` | 无 | `varchar2` | 1000 | 是 | - |
| 4 | `autodatetime` | 无 | `varchar2` | 1000 | 是 | - |
| 5 | `isbereject` | 是否退回 | `char` | 1 | 是 | - |
| 6 | `isreject` | 是否为退回前的节点操作人 | `char` | 1 | 是 | 用于分叉流转日志显示（1：是，0或其它：否） |
| 7 | `needwfback` | 需反馈 | `char` | 1 | 是 | - |
| 8 | `lastisremark` | 用于保存流程暂停、撤销时，流程操作者isremark的值 | `char` | 1 | 是 | - |
| 9 | `isreminded_csh` | 是否超时后提醒 | `char` | 1 | 是 | - |
| 10 | `wfreminduser_csh` | 流程超时后提醒用户 | `varchar2` | 4000 | 是 | - |
| 11 | `wfusertypes_csh` | 超时后的流程用户类型 | `varchar2` | 4000 | 是 | - |
| 12 | `handleforwardid` | 用于保存流程转办记录id | `integer` | - | 是 | - |
| 13 | `takisremark` | 用于记录意见征询标识 | `integer` | - | 是 | - |

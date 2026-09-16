# 泛微OA 数据表: `workflow_forward`

- **中文名称**: 工作流转发记录表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_forward`
- **主键**: `无`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `forwardid` | 转发人 | `integer` | - | 是 | 否 | 否 | - | - | workflow―_currentoprator表的id |
| 3 | `beforwardid` | 被转发人 | `integer` | - | 是 | 否 | 否 | - | - | workflow―_currentoprator表的id |
| 4 | `ispendingforward` | 是否允许待办事宜转发 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 5 | `iswaitforwardopinion` | 是否等待被转发人意见 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 6 | `isbeforward` | 被转发人是否可转发 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 7 | `issubmitedopinion` | 提交后被转发人是否可提交意见 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 8 | `issubmitforward` | 是否允许已办及办结事宜转发 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 9 | `isbeforwardsubmit` | 被转发人可提交意见（转发人提交前被转发人可提交意见，否则只能查看，查看后就到已办或者办结中） | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 10 | `isbeforwardmodify` | 转办 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 11 | `isbeforwardpending` | 转发人提交后被转发人未查看停留在待办 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是 |
| 12 | `isbeforwardtodo` | 待办可转发 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `isbeforwardalready` | 已办被转发人可转发 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `isalreadyforward` | 已办转发 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `isbeforwardsubmitalready` | 允许已办被转发人可提交意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 16 | `isbeforwardsubmitnotaries` | 允许办结被转发人可提交意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 17 | `isfromwfremark` | 待办提交后被转发人是否可提交意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |

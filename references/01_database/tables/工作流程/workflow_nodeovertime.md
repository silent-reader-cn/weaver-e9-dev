# 泛微OA 数据表: `workflow_nodeovertime`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_nodeovertime`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | - | 主键id |
| 2 | `workflowid` | 路径id | `integer` | - | - | - |
| 3 | `nodeid` | 节点id | `integer` | - | - | - |
| 4 | `requestid` | 流程请求id | `integer` | - | - | 前端设置超时，存储相应的请求id，后端超时设置requestid为null |
| 5 | `selectnodepass` | 超时时间设置方式 | `char` | - | - | 1：指定时间超时；2：指定表单字段 |
| 6 | `nodepasshour` | 指定时间超时设置-小时 | `integer` | - | - | - |
| 7 | `nodepassminute` | 指定时间超时设置-分钟 | `integer` | - | - | - |
| 8 | `dateField` | 指定表单字段超时-日期字段 | `varchar2` | - | - | - |
| 9 | `timeField` | 指定表单字段超时-时间字段 | `varchar2` | - | - | - |
| 10 | `isautoflow` | 是否启动超时处理 | `integer` | - | - | 0：不启动超时处理；1：启动超时处理 |
| 11 | `flownextoperator` | 超时处理方式 | `integer` | - | - | 0：指定干预对象；1：自动流转到下一操作者；3：退回到指定节点；4：提交到指定节点 |
| 12 | `fieldType` | 指定表单字段超时-类型 | `integer` | - | - | 1：表示固定时间超时，否则表单字段超时 |
| 13 | `fixtime` | 固定时间 | `varchar2` | - | - | 超时时间设置指定的固定时间 |
| 14 | `flowobjectids` | 指定对象 | `varchar2` | - | - | 处理方式为指定干预对象时，这个字段的值为指定干预对象的id；指定退回节点，这个字段存的值为退回节点id；提交到指定节点，存的是指定的退回节点id |
| 15 | `ProcessorOpinion` | 签字意见 | `varchar2` | - | - | 自定义的超时处理签字意见 |

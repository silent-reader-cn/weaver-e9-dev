# 泛微OA 数据表: `workflow_subwfset`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_subwfset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `issplitdetail` | 明细拆分触发 | `char` | 1 | 是 | - |
| 2 | `id` | 子流程设置表id | `integer` | - | 否 | 由sequenceindex表得到，对应的indexdesc为workflow_subwfsetid |
| 3 | `mainworkflowid` | 主流程id | `integer` | - | 是 | - |
| 4 | `subworkflowid` | 子流程id | `integer` | - | 是 | - |
| 5 | `triggernodeid` | 触发节点id | `integer` | - | 是 | - |
| 6 | `triggertime` | 触发时间 | `char` | 1 | 是 | 1:到达节点,2:离开节点 |
| 7 | `subwfcreatortype` | 子流程创建人类型 | `char` | 1 | 是 | 1:主流程当前操作人,2:主流程创建人,3:主流程单人力资源字段 |
| 8 | `subwfcreatorfieldid` | 主流程单人力资源字段id或多人力资源字段id或收文单位字段id | `integer` | - | 是 | - |
| 9 | `isread` | 流程之间的意见是否可相互查看 | `integer` | - | 是 | 0否，1是 |
| 10 | `triggertype` | 触发类型 | `char` | 1 | 是 | 1：自动触发，2：手动触发 |
| 11 | `triggeroperation` | 触发操作 | `char` | 1 | 是 | - |

# 泛微OA 数据表: `workflow_addinoperate`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_addinoperate`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `operateorder` | 顺序 | `integer` | - | 是 | - |
| 2 | `isdisable` | 是否启用 | `integer` | - | 是 | - |
| 3 | `drawbackflag` | 退回触发 | `integer` | - | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `objid` | 节点或出口id | `integer` | - | 是 | 当isnode为1时为节点的id；当为0时为出口的id |
| 6 | `isnode` | 是否为节点附加条件还是出口附加条件 | `integer` | - | 是 | 1：节点 0：出口 |
| 7 | `workflowid` | 工作流id | `integer` | - | 是 | - |
| 8 | `fieldid` | 操作要赋予的目标字段id | `integer` | - | 是 | - |
| 9 | `fieldop1id` | 第一操作字段id | `integer` | - | 是 | - |
| 10 | `fieldop2id` | 第二操作字段id | `integer` | - | 是 | - |
| 11 | `operation` | 操作类型 | `integer` | - | 是 | 操作类型  1：+ 2：-  3：*  4：/ |
| 12 | `customervalue` | 自定义值 | `varchar2` | 4000 | 是 | type为0时，值为普通的附加操作设置 type为1时，值为附件上传,单文档，多文档的文档状态设置，如2，5等 type为2时，值为外部接口，如action.workflowtodoc |
| 13 | `rules` | 附加规则 | `integer` | - | 是 | 1：跳过周末  2：跳过公共假日  3：跳过周末且跳过公共假日 |
| 14 | `type` | 操作类型 | `integer` | - | 是 | 0：普通的附加操作设置  1：附件上传,单文档，多文档的文档状态设置  2：外部接口 |
| 15 | `ispreadd` | 是否节点前操作 | `char` | 1 | 是 | 1：是 0：否 |
| 16 | `wftomodesetid` | 未使用 | `varchar2` | 4000 | 是 | - |
| 17 | `isnewsap` | 是否新版SAP | `varchar2` | 400 | 是 | - |
| 18 | `wftofinancesetid` | 已作废 | `integer` | - | 是 | - |
| 19 | `istriggerreject` | 退回触发 | `integer` | - | 是 | - |

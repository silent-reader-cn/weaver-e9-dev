# 泛微OA 数据表: `workflow_tridiffwfsubwf`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_tridiffwfsubwf`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `tridiffwfdifffieldid` | 触发不同流程可区分字段表id | `integer` | - | 是 | - |
| 3 | `subworkflowid` | 子流程id | `integer` | - | 是 | - |
| 4 | `subwfcreatortype` | 子流程创建人类型 | `char` | 1 | 是 | 1:主流程当前操作人,2:主流程创建人,3:主流程单人力资源字段 |
| 5 | `subwfcreatorfieldid` | 主流程单人力资源字段id或多人力资源字段id或收文单位字段id | `integer` | - | 是 | - |
| 6 | `isread` | 流程之间的意见是否可相互查看 | `integer` | - | 是 | 1是，0或其它为否 |
| 7 | `fieldvalue_back` | 未使用 | `integer` | - | 是 | - |
| 8 | `fieldvalue` | 字段值，多人力资源与人力资源条件对应人力资源id，收（发）文单位对应收（发）文单位id | `varchar2` | 1000 | 是 | - |
| 9 | `isreadnodes` | 是否为已查看节点 | `varchar2` | 1000 | 是 | - |
| 10 | `isreadmainwf` | 是否为已看出主流程 | `char` | 1 | 是 | - |
| 11 | `isreadmainwfnodes` | 是否为已看出主流程节点 | `varchar2` | 1000 | 是 | - |
| 12 | `isreadparallelwf` | 是否是已查看并行流程 | `char` | 1 | 是 | - |
| 13 | `isreadparallelwfnodes` | 是否是已查看并行流程节点 | `varchar2` | 1000 | 是 | - |
| 14 | `ifsplitfield` | 是否拆分字段 | `char` | 1 | 是 | 1:是，0：否 |
| 15 | `isstopcreaternode` | 是否允许创建节点 | `char` | 1 | 是 | - |

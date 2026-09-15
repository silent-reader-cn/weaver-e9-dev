# 泛微OA 数据表: `workflow_distributionsummary`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_distributionsummary`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `mainwfid` | 主流程id | `integer` | - | 是 | - |
| 3 | `mainformid` | 主流程表单id | `integer` | - | 是 | - |
| 4 | `mainfieldid` | 主流程字段id | `integer` | - | 是 | - |
| 5 | `mainfieldname` | 主流程字段名称 | `varchar2` | 1000 | 是 | - |
| 6 | `maindetailnum` | 主流程明细number | `integer` | - | 是 | 1：主流程明细表1；2：主流程明细表2；... |
| 7 | `nodeid` | 主流程设置节点id | `integer` | - | 是 | - |
| 8 | `subwfid` | 子流程id | `integer` | - | 是 | - |
| 9 | `subformid` | 子流程表单id | `integer` | - | 是 | - |
| 10 | `subfieldid` | 子流程字段id | `integer` | - | 是 | - |
| 11 | `subfieldname` | 子流程字段名称id | `varchar2` | 1000 | 是 | - |
| 12 | `fieldhtmltype` | 子流程字段类型 | `char` | 1 | 是 | - |
| 13 | `type` | 子流程字段type | `integer` | - | 是 | - |
| 14 | `subtype` | 子流程字段位置id | `integer` | - | 是 | 0：主表；1：明细表1；... |
| 15 | `iscreatedoc` | 是否可以创建文档 | `char` | 1 | 是 | 0：否；1：是； |

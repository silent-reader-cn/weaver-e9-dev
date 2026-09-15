# 泛微OA 数据表: `hpsetting_wfcentertemplate`

- **所属模块**: `门户管理`
- **数据库表名**: `hpsetting_wfcentertemplate`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `eid` | 元素id | `integer` | - | 是 | - |
| 3 | `viewtype` | 流程查看类型 | `integer` | - | 是 | - |
| 4 | `typeids` | 流程类型id | `varchar2` | 4000 | 是 | - |
| 5 | `flowids` | 流程实例id | `varchar2` | 4000 | 是 | - |
| 6 | `nodeids` | 流程节点id | `varchar2` | 4000 | 是 | - |
| 7 | `isexclude` | 选择类型 | `char` | 1 | 是 | - |
| 8 | `tabid` | tab页id | `varchar2` | 1000 | 是 | - |
| 9 | `tabtitle` | tab标题 | `varchar2` | 1000 | 是 | - |
| 10 | `showcopy` | 是否显示抄送 | `varchar2` | 1000 | 是 | - |
| 11 | `completeflag` | 是否显示全部 | `integer` | - | 是 | - |
| 12 | `countflag` | 是否显示未读 | `varchar2` | 10 | 是 | - |
| 13 | `ordernum` | 序号 | `integer` | - | 是 | - |
| 14 | `showtimeout` | 优先显示超时 | `integer` | - | 是 | - |
| 15 | `isarrangement` | isarrangement | `varchar2` | 1000 | 是 | - |

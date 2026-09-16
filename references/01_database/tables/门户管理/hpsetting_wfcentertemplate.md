# 泛微OA 数据表: `hpsetting_wfcentertemplate`

- **中文名称**: 门户流程中心元素tab页设置信息模板表
- **所属模块**: `门户管理`
- **数据库表名**: `hpsetting_wfcentertemplate`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `eid` | 元素id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `viewtype` | 流程查看类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `typeids` | 流程类型id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `flowids` | 流程实例id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `nodeids` | 流程节点id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `isexclude` | 选择类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `tabid` | tab页id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `tabtitle` | tab标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `showcopy` | 是否显示抄送 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `completeflag` | 是否显示全部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `countflag` | 是否显示未读 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 13 | `ordernum` | 序号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `showtimeout` | 优先显示超时 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `isarrangement` | isarrangement | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

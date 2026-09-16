# 泛微OA 数据表: `mode_ganttset`

- **中文名称**: 甘特图基础信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_ganttset`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `ganttname` | 刚特图名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `sqlcondition` | 数据显示条件 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `mainfield` | 主键 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `titlefield` | 显示名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `superiorfield` | 上级 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `frontfield` | 前置关系字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `rearfield` | 实际字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `startdatefield` | 计划开始日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `starttimefield` | 计划开始时间字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `enddatefield` | 计划结束日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `endtimefield` | 计划结束时间字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `createdate` | 创建日期 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 18 | `createtime` | 创建时间 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 19 | `defaultrootid` | 默认根节点 | `varchar2` | 512 | 是 | 否 | 否 | - | - | - |
| 20 | `progressfield` | 进度 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `actualstartdatefield` | 实际开始日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 22 | `actualstarttimefield` | 实际开始时间字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `actualenddatefield` | 实际结束日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `actualendtimefield` | 实际结束时间字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `ganttdesc` | 描述 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

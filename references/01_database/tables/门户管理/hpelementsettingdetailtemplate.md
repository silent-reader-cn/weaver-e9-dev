# 泛微OA 数据表: `hpelementsettingdetailtemplate`

- **中文名称**: 门户元素设置明细模板表
- **所属模块**: `门户管理`
- **数据库表名**: `hpelementsettingdetailtemplate`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `userid` | 用户ID或分部ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `usertype` | 用户类型 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `eid` | 元素ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `perpage` | 元素显示条数 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `linkmode` | 链接模式 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 7 | `showfield` | 显示字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `sharelevel` | 共享级别 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `hpid` | 主页id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `currenttab` | 当前Tabid | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `isremind` | 是否提醒 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `hpinfo_workflow`

- **所属模块**: `门户管理`
- **数据库表名**: `hpinfo_workflow`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `infoname` | 名称 | `varchar2` | 1000 | 是 | - |
| 3 | `styleid` | 样式ID | `varchar2` | 1000 | 是 | - |
| 4 | `layoutid` | 布局id | `integer` | - | 是 | - |
| 5 | `isuse` | 是否启用 | `char` | 1 | 是 | - |
| 6 | `islocked` | 是否锁定 | `integer` | - | 是 | - |
| 7 | `creatortype` | 创建人类型 | `integer` | - | 是 | - |
| 8 | `creatorid` | 创建人id | `integer` | - | 是 | - |
| 9 | `menustyleid` | 菜单样式id | `varchar2` | 1000 | 是 | - |
| 10 | `wfid` | 流程实例id | `integer` | - | 是 | - |
| 11 | `wfnid` | 流程节点id | `integer` | - | 是 | - |
| 12 | `hpid` | 门户首页id | `integer` | - | 是 | - |

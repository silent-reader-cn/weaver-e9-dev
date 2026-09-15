# 泛微OA 数据表: `hpelementtemplate`

- **所属模块**: `门户管理`
- **数据库表名**: `hpelementtemplate`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `eid` | 元素id | `varchar2` | 1000 | 是 | - |
| 3 | `title` | 元素标题 | `varchar2` | 1000 | 是 | - |
| 4 | `ebaseid` | 原始的元素表ID | `varchar2` | 1000 | 是 | - |
| 5 | `templatedesc` | 模板描述 | `varchar2` | 4000 | 是 | - |
| 6 | `templatetitle` | 模板标题 | `varchar2` | 1000 | 是 | - |
| 7 | `logo` | 元素图标ID | `varchar2` | 1000 | 是 | - |
| 8 | `islocked` | 是否锁定 | `char` | 1 | 否 | - |
| 9 | `strsqlwhere` | 除开返回字段以名的SQL语句 | `varchar2` | 4000 | 是 | - |
| 10 | `issyselement` | 是否系统元素 | `char` | 1 | 否 | - |
| 11 | `hpid` | 所属主页 | `integer` | - | 否 | - |
| 12 | `isfixationrowheight` | 是否调整行高 | `char` | 1 | 是 | - |
| 13 | `background` | 背景样式 | `varchar2` | 1000 | 是 | - |
| 14 | `styleid` | 样式ID | `varchar2` | 1000 | 是 | - |
| 15 | `height` | 高度 | `integer` | - | 是 | - |
| 16 | `margintop` | 上间隔 | `integer` | - | 是 | - |
| 17 | `marginbottom` | 下间隔 | `integer` | - | 是 | - |
| 18 | `marginright` | 右间隔 | `integer` | - | 是 | - |
| 19 | `marginleft` | 左间隔 | `integer` | - | 是 | - |
| 20 | `shareuser` | 共享者 | `varchar2` | 1000 | 是 | - |
| 21 | `scrolltype` | 滚动方向 | `varchar2` | 1000 | 是 | - |
| 22 | `newstemplate` | 新闻模板id | `varchar2` | 1000 | 是 | - |
| 23 | `isremind` | 是否提醒 | `varchar2` | 1000 | 是 | - |
| 24 | `frommodule` | 模块 | `varchar2` | 1000 | 是 | - |
| 25 | `isuse` | 是否启用 | `integer` | - | 是 | - |

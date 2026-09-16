# 泛微OA 数据表: `hp_mobile_element`

- **中文名称**: 移动门户元素表
- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_element`
- **主键**: `id`
- **字段数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `title` | 标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `logo` | 元素图标ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `islocked` | 是否锁定 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 5 | `strsqlwhere` | 除开返回字段以名的SQL语句 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `ebaseid` | 原始的元素表ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `issyselement` | 是否系统元素 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `hpid` | 所属主页 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `isfixationrowheight` | 是否调整行高 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 10 | `background` | 背景样式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `styleid` | 样式ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `picstyleid` | 图片样式ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `height` | 高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `margintop` | 上间隔 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `marginbottom` | 下间隔 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `marginright` | 右间隔 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `marginleft` | 左间隔 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `shareuser` | 共享者 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `scrolltype` | 滚动方向 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `newstemplate` | 新闻模板id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `isremind` | 是否提醒 | `varchar2` | 1000 | 是 | 否 | 否 | - | isnew | - |
| 22 | `frommodule` | 模块 | `varchar2` | 1000 | 是 | 否 | 否 | - | Portal | - |
| 23 | `isuse` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | 1 | - |

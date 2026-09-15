# 泛微OA 数据表: `hp_mobile_element`

- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_element`
- **字段总数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `title` | 标题 | `varchar2` | 1000 | 是 | - |
| 3 | `logo` | 元素图标ID | `varchar2` | 4000 | 是 | - |
| 4 | `islocked` | 是否锁定 | `integer` | - | 是 | - |
| 5 | `strsqlwhere` | 除开返回字段以名的SQL语句 | `varchar2` | 4000 | 是 | - |
| 6 | `ebaseid` | 原始的元素表ID | `varchar2` | 1000 | 是 | - |
| 7 | `issyselement` | 是否系统元素 | `integer` | - | 是 | - |
| 8 | `hpid` | 所属主页 | `integer` | - | 是 | - |
| 9 | `isfixationrowheight` | 是否调整行高 | `integer` | - | 是 | - |
| 10 | `background` | 背景样式 | `varchar2` | 1000 | 是 | - |
| 11 | `styleid` | 样式ID | `varchar2` | 1000 | 是 | - |
| 12 | `picstyleid` | 图片样式ID | `varchar2` | 1000 | 是 | - |
| 13 | `height` | 高度 | `integer` | - | 是 | - |
| 14 | `margintop` | 上间隔 | `integer` | - | 是 | - |
| 15 | `marginbottom` | 下间隔 | `integer` | - | 是 | - |
| 16 | `marginright` | 右间隔 | `integer` | - | 是 | - |
| 17 | `marginleft` | 左间隔 | `integer` | - | 是 | - |
| 18 | `shareuser` | 共享者 | `varchar2` | 4000 | 是 | - |
| 19 | `scrolltype` | 滚动方向 | `varchar2` | 1000 | 是 | - |
| 20 | `newstemplate` | 新闻模板id | `varchar2` | 1000 | 是 | - |
| 21 | `isremind` | 是否提醒 | `varchar2` | 1000 | 是 | - |
| 22 | `frommodule` | 模块 | `varchar2` | 1000 | 是 | - |
| 23 | `isuse` | 是否启用 | `integer` | - | 是 | - |

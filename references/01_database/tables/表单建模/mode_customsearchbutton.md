# 泛微OA 数据表: `mode_customsearchbutton`

- **中文名称**: 查询列表自定义按钮基本信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_customsearchbutton`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `pageexpandid` | 页面扩展id | `integer` | - | 是 | 否 | 否 | - | - | 该模块的页面扩展id |
| 2 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `objid` | 查询列表id | `integer` | - | 是 | 否 | 否 | - | - | 查询列表id，对应mode_customsearch表的id |
| 4 | `buttonname` | 名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `hreftype` | 链接目标方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：手动输入<br>2：链接 |
| 6 | `hreftargetparid` | 链接目标参数id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 7 | `hreftargetparval` | 链接目标参数field | `varchar2` | 800 | 是 | 否 | 否 | - | - | 链接目标参数field是指查询列表中的字段id |
| 8 | `hreftarget` | 链接目标地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `jsmethodname` | javascript方法名 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 方法名命名规范：javascript:onurl(); |
| 10 | `jsparameter` | javascript方法参数 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 方法参数命名规范：field1,field2 |
| 11 | `isshow` | 是否显示 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 12 | `describe` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 13 | `showorder` | 显示顺序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 14 | `hreftargetopenway` | 链接打开方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：tab页<br>2：弹出框 |
| 15 | `interfacepath` | 接口路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `jsmethodbody` | javascript方法体 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 方法体命名规范：function onurl(id,params){} |

# 泛微OA 数据表: `mode_customtree`

- **中文名称**: 树形基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_customtree`
- **主键**: `id`
- **字段数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `treename` | 树形名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `treedesc` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 5 | `creater` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 对应hrmresource表的id |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 8 | `rootname` | 根节点名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 9 | `rooticon` | 根节点图标 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `defaultaddress` | 根节点链接地址 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `expandfirstnode` | 是否默认展开一级节点 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 12 | `showtype` | 显示样式 | `integer` | - | 是 | 否 | 否 | - | - | 0：导航树<br>1：树形浏览框 |
| 13 | `isselsub` | 多选时是否选中子项 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否<br>仅在字段设置为“自定义树形多选”时有效 |
| 14 | `isonlyleaf` | 仅允许选择叶子节点 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 15 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应modetreefield表的id |
| 16 | `treecode` | 32位uuid | `varchar2` | 256 | 是 | 否 | 否 | - | - | 主要用来复制树，作为唯一识别 |
| 17 | `isrefreshtree` | 是否刷新左侧树 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 18 | `isshowsearchtab` | 组合查询 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `searchbrowserid` | 组合查询i浏览框d | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `isquicksearch` | 是否快捷搜索 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 21 | `treeremark` | 操作说明 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

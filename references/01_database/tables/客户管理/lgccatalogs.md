# 泛微OA 数据表: `lgccatalogs`

- **中文名称**: 产品类别表
- **所属模块**: `客户管理`
- **数据库表名**: `lgccatalogs`
- **主键**: `id`
- **字段数**: `50`

> 说明：产品类别表（作用不明，名称待定，测试服务器中此表内无任何数据）

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | id |
| 2 | `catalogname` | 名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 0 |
| 3 | `catalogdesc` | 说明 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 0 |
| 4 | `catalogorder` | 排序 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 5 | `perpage` | 页容量 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 6 | `seclevelfrom` | 安全级别最小值 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 7 | `seclevelto` | 安全级别最大值 | `integer` | - | 是 | 否 | 否 | - | - | 1：最高，2：工具条，3：隐藏 |
| 8 | `navibardsp` | 显示 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 9 | `navibarbgcolor` | 背景颜色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 10 | `navibarfontcolor` | 字体颜色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 11 | `navibarfontsize` | 字体大小 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 12 | `navibarfonttype` | 字体类型 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 13 | `toolbardsp` | 工具条显示 | `char` | 1 | 是 | 否 | 否 | - | - | 1：左页，2：右页，3：隐藏 |
| 14 | `toolbarwidth` | 工具条宽度 | `integer` | - | 是 | 否 | 否 | - | 200 | 0 |
| 15 | `toolbarbgcolor` | 工具条背景色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 16 | `toolbarfontcolor` | 工具条字体颜色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 17 | `toolbarlinkbgcolor` | 工具条链接背景色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 18 | `toolbarlinkfontcolor` | 工具条链接字体颜色 | `char` | 6 | 是 | 否 | 否 | - | - | 0 |
| 19 | `toolbarfontsize` | 工具条字体大小 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 20 | `toolbarfonttype` | 工具条字体类型 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 21 | `countrydsp` | 国家 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 22 | `countrydeftype` | 默认 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 23 | `countryid` | 国家id | `integer` | - | 是 | 否 | 否 | - | - | 0：人力资源，1：固定 |
| 24 | `searchbyname` | 按名称搜素 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 25 | `searchbycrm` | 按人员搜索 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 26 | `searchadv` | 高级搜索 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 27 | `assortmentdsp` | 产品种类列表 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 28 | `assortmentname` | 列表名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 0 |
| 29 | `assortmentsql` | 列表条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 0 |
| 30 | `attributedsp` | 属性显示 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 31 | `attributecol` | 属性颜色 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 32 | `attributefontsize` | 属性字体大小 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 33 | `attributefonttype` | 属性字体 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 0 |
| 34 | `assetsql` | 显示条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 0 |
| 35 | `assetcol1` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 36 | `assetcol2` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 37 | `assetcol3` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 38 | `assetcol4` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 39 | `assetcol5` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 40 | `assetcol6` | 列 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 41 | `assetfontsize` | 字体大小 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 42 | `assetfonttype` | 字体类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 0 |
| 43 | `webshopdap` | 使用 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 44 | `webshoptype` | 类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：定向客户，一般访问者 |
| 45 | `webshopreturn` | 返回 | `char` | 1 | 是 | 否 | 否 | - | - | 0 |
| 46 | `webshopmanageid` | 人力资源 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 47 | `createrid` | 创建者 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 48 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 0 |
| 49 | `lastmoderid` | 最后修改者 | `integer` | - | 是 | 否 | 否 | - | - | 0 |
| 50 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 否 | 否 | - | - | 0 |

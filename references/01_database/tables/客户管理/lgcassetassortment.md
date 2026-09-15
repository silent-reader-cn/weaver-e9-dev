# 泛微OA 数据表: `lgcassetassortment`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcassetassortment`
- **字段总数**: `51`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `assortmentmark` | 产品种类编号 | `varchar2` | 1000 | 是 | 产品种类编号 |
| 3 | `assortmentname` | 产品种类名称 | `varchar2` | 1000 | 是 | 产品种类名称 |
| 4 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 5 | `resourceid` | 人力资源id | `integer` | - | 是 | hrmresource:id |
| 6 | `assortmentimageid` | 产品种类图片id | `integer` | - | 是 | ImageFile:id |
| 7 | `assortmentremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 8 | `supassortmentid` | 直接上级种类id | `integer` | - | 是 | 直接上级种类id |
| 9 | `supassortmentstr` | 所有上级种类id | `varchar2` | 1000 | 是 | - |
| 10 | `subassortmentcount` | 下级种类数量 | `integer` | - | 是 | 下级种类数量 |
| 11 | `assetcount` | 产品数量 | `integer` | - | 是 | 该分类下的所有产品数量（包括子分类） |
| 12 | `dff01name` | 默认属性1名称 | `varchar2` | 1000 | 是 | 备用字段 |
| 13 | `dff01use` | 默认属性1是否使用 | `integer` | - | 是 | 备用字段 |
| 14 | `dff02name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 15 | `dff02use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 16 | `dff03name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 17 | `dff03use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 18 | `dff04name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 19 | `dff04use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 20 | `dff05name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 21 | `dff05use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 22 | `nff01name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 23 | `nff01use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 24 | `nff02name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 25 | `nff02use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 26 | `nff03name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 27 | `nff03use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 28 | `nff04name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 29 | `nff04use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 30 | `nff05name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 31 | `nff05use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 32 | `tff01name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 33 | `tff01use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 34 | `tff02name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 35 | `tff02use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 36 | `tff03name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 37 | `tff03use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 38 | `tff04name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 39 | `tff04use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 40 | `tff05name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 41 | `tff05use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 42 | `bff01name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 43 | `bff01use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 44 | `bff02name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 45 | `bff02use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 46 | `bff03name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 47 | `bff03use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 48 | `bff04name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 49 | `bff04use` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 50 | `bff05name` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 51 | `bff05use` | 备用字段 | `integer` | - | 是 | 备用字段 |

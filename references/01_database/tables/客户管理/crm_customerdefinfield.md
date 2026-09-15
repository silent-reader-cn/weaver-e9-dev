# 泛微OA 数据表: `crm_customerdefinfield`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customerdefinfield`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 11 | 否 | id |
| 2 | `fieldname` | 字段名称 | `varchar2` | 480 | 是 | 字段名称 |
| 3 | `fieldlabel` | 标签id | `varchar2` | 2000 | 是 | 标签id |
| 4 | `fielddbtype` | 字段类型 | `varchar2` | 320 | 是 | 字段类型 |
| 5 | `fieldhtmltype` | html标签类型 | `char` | 1 | 是 | html标签类型 |
| 6 | `selectid` | 0 | `integer` | 11 | 是 | 0 |
| 7 | `type` | 子字段详细类型 | `integer` | 11 | 是 | 子字段详细类型 |
| 8 | `viewtype` | 字段类型 | `integer` | 11 | 是 | viewtype="0"表示主表字段,viewtype="1"表示明细表字段 |
| 9 | `usetable` | 用于表 | `varchar2` | 400 | 是 | 用于表 |
| 10 | `textheight` | 多行文本框的高度 | `integer` | 11 | 是 | 多行文本框的高度 |
| 11 | `imgwidth` | 上传图片的宽度 | `integer` | 11 | 是 | 上传图片的宽度 |
| 12 | `imgheight` | 上传图片的高度 | `integer` | 11 | 是 | 上传图片的高度 |
| 13 | `dsporder` | 排序 | `number` | (15,2) | 是 | 排序 |
| 14 | `isopen` | 是否启用 | `char` | 1 | 是 | 是否启用 |
| 15 | `ismust` | 是否必填 | `char` | 1 | 是 | 是否必填 |
| 16 | `places` | 小数位数 | `integer` | 11 | 是 | 小数位数 |
| 17 | `candel` | 能否删除 | `char` | 1 | 是 | 能否删除 |
| 18 | `groupid` | 分组id | `integer` | 11 | 是 | 分组id |
| 19 | `issearch` | 是否作为查询条件 | `char` | 1 | 是 | 是否作为查询条件 |
| 20 | `seltablename` | 0 | `varchar2` | 1000 | 是 | 0 |
| 21 | `selcolumname` | 0 | `varchar2` | 1000 | 是 | 0 |
| 22 | `selkeycolumname` | 0 | `varchar2` | 1000 | 是 | 0 |
| 23 | `dmlurl` | 0 | `varchar2` | 1000 | 是 | 0 |
| 24 | `isdisplay` | 是否列表标题 | `integer` | 11 | 是 | 是否列表标题 |
| 25 | `isexport` | 是否导出 | `integer` | 11 | 是 | 是否导出 |
| 26 | `slat` | 0 | `varchar2` | 800 | 是 | 0 |

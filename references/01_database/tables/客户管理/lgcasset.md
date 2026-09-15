# 泛微OA 数据表: `lgcasset`

- **所属模块**: `客户管理`
- **数据库表名**: `lgcasset`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | 0 | 否 | 产品id |
| 2 | `assetmark` | 产品编号 | `varchar2` | 1000 | 是 | 产品编号 |
| 3 | `barcode` | 代码 | `varchar2` | 1000 | 是 | 产品代码 |
| 4 | `seclevel` | 安全级别 | `integer` | 0 | 是 | 安全级别 |
| 5 | `assetimageid` | 产品图片id | `integer` | 0 | 是 | 产品图片id:   Imagefile |
| 6 | `assettypeid` | 产品类别id | `integer` | 0 | 是 | 产品类别id：LgcAssetAssortment |
| 7 | `assetunitid` | 产品单位id | `integer` | 0 | 是 | 产品单位id：LgcAssetUnit |
| 8 | `replaceassetid` | 替代产品id | `integer` | 0 | 是 | 替代产品id |
| 9 | `assetversion` | 产品版本 | `varchar2` | 1000 | 是 | 产品版本 |
| 10 | `assetattribute` | 产品属性 | `varchar2` | 1000 | 是 | 多选：可销售，可采购，可生产，可网上销售， 如果产品可销售，则在产品显示页面有分销商菜单，如果产品可以采购，在产品显示页面有供应商按钮 |
| 11 | `counttypeid` | 数量类型id | `integer` | 0 | 是 | 数量类型id |
| 12 | `assortmentid` | 产品种类id | `integer` | 0 | 是 | 产品种类id |
| 13 | `assortmentstr` | 产品种类 | `varchar2` | 1000 | 是 | 产品种类 |
| 14 | `relatewfid` | 关联对象id | `integer` | 0 | 是 | 关联对象id |

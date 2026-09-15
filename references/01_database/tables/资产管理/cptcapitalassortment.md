# 泛微OA 数据表: `cptcapitalassortment`

- **所属模块**: `资产管理`
- **数据库表名**: `cptcapitalassortment`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `assortmentname` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 3 | `assortmentremark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 4 | `supassortmentid` | 直接上级资产组id | `integer` | - | 是 | 直接上级资产组id |
| 5 | `supassortmentstr` | 所有的上级资产组id | `varchar2` | 1000 | 是 | 所有的上级资产组id |
| 6 | `subassortmentcount` | 下级资产组个数 | `integer` | - | 是 | 下级资产组个数 |
| 7 | `capitalcount` | 资产资料个数 | `integer` | - | 是 | 资产资料个数 |
| 8 | `assortmentmark` | 编号 | `varchar2` | 240 | 是 | 编号 |
| 9 | `subcompanyid1` | 所属分部 | `integer` | - | 是 | 所属分部 |

# 泛微OA 数据表: `cptcapitalassortment`

- **中文名称**: 资产组
- **所属模块**: `资产管理`
- **数据库表名**: `cptcapitalassortment`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `assortmentname` | 名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 名称 |
| 3 | `assortmentremark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 备注 |
| 4 | `supassortmentid` | 直接上级资产组id | `integer` | - | 是 | 否 | 否 | - | - | 直接上级资产组id |
| 5 | `supassortmentstr` | 所有的上级资产组id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 所有的上级资产组id |
| 6 | `subassortmentcount` | 下级资产组个数 | `integer` | - | 是 | 否 | 否 | - | 0 | 下级资产组个数 |
| 7 | `capitalcount` | 资产资料个数 | `integer` | - | 是 | 否 | 否 | - | 0 | 资产资料个数 |
| 8 | `assortmentmark` | 编号 | `varchar2` | 240 | 是 | 否 | 否 | - | - | 编号 |
| 9 | `subcompanyid1` | 所属分部 | `integer` | - | 是 | 否 | 否 | - | - | 所属分部 |

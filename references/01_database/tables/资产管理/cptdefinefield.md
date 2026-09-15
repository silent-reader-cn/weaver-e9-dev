# 泛微OA 数据表: `cptdefinefield`

- **所属模块**: `资产管理`
- **数据库表名**: `cptdefinefield`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `billid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 3 | `fieldname` | 字段名 | `varchar2` | 480 | 是 | 字段名 |
| 4 | `fieldlabel` | 字段标签 | `integer` | - | 是 | 字段标签 |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 字段数据库类型 |
| 6 | `fieldhtmltype` | 字段类型 | `char` | 1 | 是 | 字段类型 |
| 7 | `type` | 明细类型 | `integer` | - | 是 | 明细类型 |
| 8 | `viewtype` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 9 | `detailtable` | 备用字段 | `varchar2` | 400 | 是 | 备用字段 |
| 10 | `fromuser` | 备用字段 | `char` | 1 | 是 | 备用字段 |
| 11 | `textheight` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 12 | `dsporder` | 显示顺序 | `number` | (10,2) | 是 | 显示顺序 |
| 13 | `childfieldid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 14 | `imgheight` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 15 | `imgwidth` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 16 | `isopen` | 启用 | `char` | 1 | 是 | 启用 |
| 17 | `ismand` | 必填 | `char` | 1 | 是 | 必填 |
| 18 | `isused` | 已使用 | `char` | 1 | 是 | 已使用 |
| 19 | `issystem` | 是否系统字段 | `char` | 1 | 是 | 是否系统字段 |
| 20 | `allowhide` | 是否允许隐藏 | `char` | 1 | 是 | 是否允许隐藏 |
| 21 | `groupid` | 分组id | `integer` | - | 是 | 分组id |

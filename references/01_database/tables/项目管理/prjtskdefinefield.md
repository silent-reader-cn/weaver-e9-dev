# 泛微OA 数据表: `prjtskdefinefield`

- **所属模块**: `项目管理`
- **数据库表名**: `prjtskdefinefield`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `qfws` | 金额千分位 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 3 | `billid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 4 | `fieldname` | 字段名 | `varchar2` | 480 | 是 | 字段名 |
| 5 | `fieldlabel` | 字段标签 | `integer` | - | 是 | 字段标签 |
| 6 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 字段数据库类型 |
| 7 | `fieldhtmltype` | 字段类型 | `char` | 1 | 是 | 字段类型 |
| 8 | `type` | 明细类型 | `integer` | - | 是 | 明细类型 |
| 9 | `viewtype` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 10 | `detailtable` | 备用字段 | `varchar2` | 400 | 是 | 备用字段 |
| 11 | `fromuser` | 备用字段 | `char` | 1 | 是 | 备用字段 |
| 12 | `textheight` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 13 | `dsporder` | 显示顺序 | `number` | (10,2) | 是 | 显示顺序 |
| 14 | `childfieldid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 15 | `imgheight` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 16 | `imgwidth` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 17 | `isopen` | 启用 | `char` | 1 | 是 | 启用 |
| 18 | `ismand` | 必填 | `char` | 1 | 是 | 必填 |
| 19 | `isused` | 已使用 | `char` | 1 | 是 | 已使用 |
| 20 | `issystem` | 是否系统字段 | `char` | 1 | 是 | 是否系统字段 |
| 21 | `allowhide` | 是否允许隐藏 | `char` | 1 | 是 | 是否允许隐藏 |
| 22 | `groupid` | 分组id | `integer` | - | 是 | 分组id |

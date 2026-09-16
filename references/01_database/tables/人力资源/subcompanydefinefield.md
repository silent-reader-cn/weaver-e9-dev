# 泛微OA 数据表: `subcompanydefinefield`

- **中文名称**: 分部自定义字段信息表
- **所属模块**: `人力资源`
- **数据库表名**: `subcompanydefinefield`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `billid` | 对应流程id | `integer` | - | 是 | 否 | 否 | - | - | 对应流程id |
| 3 | `fieldname` | 字段名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 字段名称 |
| 4 | `fieldlabel` | 字段label id | `integer` | - | 是 | 否 | 否 | - | - | 字段label id |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 取值：integer、varchar |
| 6 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | 否 | 否 | - | - | 如1为文本，4为部门... |
| 7 | `type` | 字段详细类型 | `integer` | - | 是 | 否 | 否 | - | - | 字段详细类型 |
| 8 | `viewtype` | 显示类型 | `integer` | - | 是 | 否 | 否 | - | 0 | 显示类型 |
| 9 | `detailtable` | 详细table | `varchar2` | 400 | 是 | 否 | 否 | - | - | 详细table |
| 10 | `fromuser` | 创建人id | `char` | 1 | 是 | 否 | 否 | - | 1 | 创建人id |
| 11 | `textheight` | 文本高度 | `integer` | - | 是 | 否 | 否 | - | - | 文本高度 |
| 12 | `dsporder` | 序列号 | `number` | (15,2) | 是 | 否 | 否 | - | - | 序列号 |
| 13 | `childfieldid` | 下级字段id | `integer` | - | 是 | 否 | 否 | - | - | 下级字段id |
| 14 | `imgheight` | 图片显示高度 | `integer` | - | 是 | 否 | 否 | - | (0) | 图片显示高度 |
| 15 | `imgwidth` | 图片显示宽度 | `integer` | - | 是 | 否 | 否 | - | (0) | 图片显示宽度 |
| 16 | `isopen` | 是否启用 | `char` | 1 | 是 | 否 | 否 | - | - | 0-不启用(默认) 1-启用 |
| 17 | `ismand` | 是否必填 | `char` | 1 | 是 | 否 | 否 | - | - | 是否必填 |

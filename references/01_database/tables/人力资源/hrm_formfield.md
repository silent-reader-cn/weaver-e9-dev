# 泛微OA 数据表: `hrm_formfield`

- **中文名称**: 自定义字段信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrm_formfield`
- **主键**: `fieldid`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 否 | 否 | 是 | - | - | 字段id |
| 2 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | &nbsp;integer、varchar |
| 3 | `fieldname` | 字段名称 | `varchar2` | 240 | 是 | 否 | 否 | - | - | 数据库保存字段名 |
| 4 | `fieldlabel` | 字段显示名labelid | `varchar2` | 800 | 是 | 否 | 否 | - | - | 字段显示名labelid |
| 5 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：单行文本框<br>2：多行文本框<br>3：浏览按钮<br>4：check框<br>5：选择框 |
| 6 | `fieldorder` | 序列号 | `integer` | - | 是 | 否 | 否 | - | - | 序列号 |
| 7 | `ismand` | 是否必填 | `char` | 1 | 是 | 否 | 否 | - | - | 是否必填 |
| 8 | `isuse` | 是否启用 | `char` | 1 | 是 | 否 | 否 | - | - | 1-启用，2-不启用 |
| 9 | `groupid` | 分组外键id | `integer` | - | 是 | 否 | 否 | - | - | 分组外键id |
| 10 | `allowhide` | 是否允许隐藏 | `integer` | - | 是 | 否 | 否 | - | - | 是否允许隐藏 |
| 11 | `imgwidth` | 图片宽度 | `integer` | - | 是 | 否 | 否 | - | - | 图片宽度 |
| 12 | `imgheight` | 图片高度 | `integer` | - | 是 | 否 | 否 | - | - | 图片高度 |
| 13 | `textheight` | 文本框高度 | `integer` | - | 是 | 否 | 否 | - | - | 文本框高度 |
| 14 | `issystem` | 是否系统字段 | `integer` | - | 是 | 否 | 否 | - | - | 是否系统字段 |
| 15 | `dmlurl` | dmlurl | `varchar2` | 2000 | 是 | 否 | 否 | - | - | dmlurl |

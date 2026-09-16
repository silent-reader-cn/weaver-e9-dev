# 泛微OA 数据表: `customfieldshowchange`

- **中文名称**: 显示转换基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `customfieldshowchange`
- **主键**: `ID`
- **字段数**: `23`

> 说明：查询列表显示转换设置存储表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `rowbackvalue` | 行背景色 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `rowfontvalue` | 行字体颜色 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `displaystyles` | 显示样式 | `integer` | - | 是 | 否 | 否 | - | - | 弃用 |
| 4 | `thumbnail` | 是否缩略图 | `integer` | - | 是 | 否 | 否 | - | - | 图片附件使用 |
| 5 | `thumbnailheight` | 缩略图高 | `integer` | - | 是 | 否 | 否 | - | - | 图片附件使用 |
| 6 | `thumbnailwidth` | 缩略图宽 | `integer` | - | 是 | 否 | 否 | - | - | 图片附件使用 |
| 7 | `conditiontype` | 条件类型 | `integer` | - | 是 | 否 | 否 | - | - | 普通类型、sql |
| 8 | `conditionsql` | 条件sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `conditiontext` | 条件中文显示内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 条件类型为普通类型时才有值 |
| 10 | `transtype` | 转换类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `isneedconvert` | 是否需要转换 | `integer` | - | 是 | 否 | 否 | - | - | 历史数据使用 |
| 12 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 13 | `customid` | 查询列表id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_customsearch表的id |
| 14 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 15 | `fieldopt` | 字段条件 | `integer` | - | 是 | 否 | 否 | - | - | 1：大于<br>2：大于或等于<br>3：小于<br>4：小于或等于<br>5：等于<br>6：不等于 |
| 16 | `fieldoptvalue` | 字段值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `fieldshowvalue` | 显示值 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `fieldbackvalue` | 背景颜色 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `fieldfontvalue` | 字体颜色 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 20 | `fieldoptvalue2` | 显示值2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `fieldopt2` | 字段条件2 | `integer` | - | 是 | 否 | 否 | - | - | 1：大于<br>2：大于或等于<br>3：小于<br>4：小于或等于<br>5：等于<br>6：不等于 |
| 22 | `singlevalue` | 1：大于2：大于或等于3：小于4：小于或等于5：等于6：不等于 11 | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 23 | `morevalue` | 作废 12 | `integer` | - | 是 | 否 | 否 | - | - | 作废 |

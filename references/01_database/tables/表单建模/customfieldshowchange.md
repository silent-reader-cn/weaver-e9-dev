# 泛微OA 数据表: `customfieldshowchange`

- **所属模块**: `表单建模`
- **数据库表名**: `customfieldshowchange`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `rowbackvalue` | 行背景色 | `clob` | 4000 | 是 | - |
| 2 | `rowfontvalue` | 行字体颜色 | `clob` | 4000 | 是 | - |
| 3 | `displaystyles` | 显示样式 | `integer` | - | 是 | 弃用 |
| 4 | `thumbnail` | 是否缩略图 | `integer` | - | 是 | 图片附件使用 |
| 5 | `thumbnailheight` | 缩略图高 | `integer` | - | 是 | 图片附件使用 |
| 6 | `thumbnailwidth` | 缩略图宽 | `integer` | - | 是 | 图片附件使用 |
| 7 | `conditiontype` | 条件类型 | `integer` | - | 是 | 普通类型、sql |
| 8 | `conditionsql` | 条件sql | `varchar2` | 4000 | 是 | - |
| 9 | `conditiontext` | 条件中文显示内容 | `varchar2` | 4000 | 是 | 条件类型为普通类型时才有值 |
| 10 | `transtype` | 转换类型 | `integer` | - | 是 | - |
| 11 | `isneedconvert` | 是否需要转换 | `integer` | - | 是 | 历史数据使用 |
| 12 | `id` | ID | `integer` | - | 否 | - |
| 13 | `customid` | 查询列表id | `integer` | - | 是 | 对应mode_customsearch表的id |
| 14 | `fieldid` | 字段id | `integer` | - | 是 | 对应workflow_billfield表的id |
| 15 | `fieldopt` | 字段条件 | `integer` | - | 是 | - |

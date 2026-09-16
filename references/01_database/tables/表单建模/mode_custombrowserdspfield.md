# 泛微OA 数据表: `mode_custombrowserdspfield`

- **中文名称**: 浏览框字段信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_custombrowserdspfield`
- **主键**: `id`
- **字段数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `customid` | 浏览框id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_custombrowser表的id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 4 | `isquery` | 是否查询条件 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 5 | `isshow` | 是否显示 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 6 | `showorder` | 现实顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `queryorder` | 查询显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `istitle` | 是否链接字段 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否<br>一个浏览框，只能有一个链接字段，链接字段是生成浏览按钮的前提条件，作为浏览按钮的显示字段 |
| 9 | `isorder` | 是否排序 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 10 | `ordertype` | 排序类型i | `varchar2` | 800 | 是 | 否 | 否 | - | - | n：--<br>a：默认升序<br>d：默认降序 |
| 11 | `ordernum` | 默认排序优先级 | `integer` | - | 是 | 否 | 否 | - | - | 值越小，优先级越高 |
| 12 | `isquicksearch` | 是否快捷搜索字段 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 13 | `isorderfield` | 1：是0：否 10 | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 14 | `priorder` | 作废 11 | `char` | 4 | 是 | 否 | 否 | - | - | 作废 |
| 15 | `conditiontransition` | 是否条件转换 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 16 | `colwidth` | 列宽 | `number` | (10,2) | 是 | 否 | 否 | - | - | 列宽百分比 |
| 17 | `ispk` | 是否主键 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `shownamelabel` | 显示名称 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `mode_toolbar_search`

- **中文名称**: 工具栏查询信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_toolbar_search`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `isusedsearch` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `searchname` | 查询名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `searchfield` | 查询字段 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 5 | `imagesource` | 图片来源 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 6 | `imageid` | 图片id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `imageurl` | 图片链接 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `showorder` | 排序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `mainid` | 主表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `serachtype` | 查询类型 | `integer` | - | 是 | 否 | 否 | - | - | - |

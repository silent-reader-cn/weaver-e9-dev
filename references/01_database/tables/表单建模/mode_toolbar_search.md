# 泛微OA 数据表: `mode_toolbar_search`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_toolbar_search`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `isusedsearch` | 是否启用 | `integer` | - | 是 | - |
| 3 | `searchname` | 查询名称 | `varchar2` | 800 | 是 | - |
| 4 | `searchfield` | 查询字段 | `varchar2` | 400 | 是 | - |
| 5 | `imagesource` | 图片来源 | `varchar2` | 160 | 是 | - |
| 6 | `imageid` | 图片id | `integer` | - | 是 | - |
| 7 | `imageurl` | 图片链接 | `varchar2` | 1000 | 是 | - |
| 8 | `showorder` | 排序 | `integer` | - | 是 | - |
| 9 | `mainid` | 主表id | `integer` | - | 是 | - |
| 10 | `serachtype` | 查询类型 | `integer` | - | 是 | - |

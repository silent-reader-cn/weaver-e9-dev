# 泛微OA 数据表: `mode_customdspfield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customdspfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `shownamelabel` | 显示转换 | `integer` | - | 是 | - |
| 2 | `alignment` | 对齐方式 | `integer` | - | 是 | - |
| 3 | `ismaplocation` | 开启地图 | `integer` | - | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `customid` | 查询id | `integer` | - | 是 | 对应mode_customsearch表的id |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | 对应workflow_billfield表的id |
| 7 | `isquery` | 是否查询条件 | `char` | 1 | 是 | - |

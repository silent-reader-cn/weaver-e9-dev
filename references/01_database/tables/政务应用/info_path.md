# 泛微OA 数据表: `info_path`

- **所属模块**: `政务应用`
- **数据库表名**: `info_path`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `name` | 路径名称 | `varchar2` | 256 | 是 | - |
| 4 | `isrepeat` | 上报信息标题重复验证 | `integer` | - | 是 | 0否 1是 |
| 5 | `maincategory` | 附件上传1级目录 | `integer` | - | 是 | - |
| 6 | `subcategory` | 附件上传2级目录 | `integer` | - | 是 | - |
| 7 | `seccategory` | 附件上传3级目录 | `integer` | - | 是 | - |
| 8 | `showorder` | 排序 | `float` | - | 是 | - |
| 9 | `arithtype` | 加分项计算关系 | `integer` | - | 是 | 0累加 1取最高 2取最低 |
| 10 | `specialreport` | 是否允许专报 | `integer` | - | 是 | 0否 1是 |
| 11 | `additionalreport` | 是否允许特殊采用 | `integer` | - | 是 | 0否 1是 |
| 12 | `maincategory1` | 专报附件上传1级目录 | `integer` | - | 是 | - |
| 13 | `subcategory1` | 专报附件上传2级目录 | `integer` | - | 是 | - |
| 14 | `seccategory1` | 专报附件上传3级目录 | `integer` | - | 是 | - |
| 15 | `maincategory2` | 特殊采用1级目录 | `integer` | - | 是 | - |
| 16 | `subcategory2` | 特殊采用2级目录 | `integer` | - | 是 | - |
| 17 | `seccategory2` | 特殊采用3级目录 | `integer` | - | 是 | - |
| 18 | `ismanual` | 是否允许手动上传期刊内容 | `integer` | - | 是 | 0否 1是 |
| 19 | `isused` | 是否启用 | `integer` | - | 是 | 0否 1是 |

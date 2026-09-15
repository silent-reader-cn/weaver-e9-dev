# 泛微OA 数据表: `hrsyncsetparam`

- **所属模块**: `集成模块`
- **数据库表名**: `hrsyncsetparam`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `type` | 类型 | `char` | 1 | 是 | 1：分部  2：部门  3：岗位  4：人员 |
| 3 | `oafield` | OA字段 | `varchar2` | 800 | 是 | OA字段 |
| 4 | `outfield` | 外部字段 | `varchar2` | 800 | 是 | 外部字段 |
| 5 | `iskeyfield` | 关键匹配字段 | `char` | 1 | 是 | 1：是  0：否 |
| 6 | `isnewfield` | 增量标识字段 | `char` | 1 | 是 | 1：是  0：否 |
| 7 | `isparentfield` | 上级字段 | `char` | 1 | 是 | 1：是  0：否 |
| 8 | `issubcomfield` | 分部字段 | `char` | 1 | 是 | 1：是  0：否 |
| 9 | `isdeptfield` | 部门字段 | `char` | 1 | 是 | 1：是  0：否 |
| 10 | `ishrmdeptfield` | 人员部门字段 | `char` | 1 | 是 | 1：是  0：否 |
| 11 | `ishrmjobfield` | 人员岗位字段 | `char` | 1 | 是 | 1：是  0：否 |
| 12 | `transql` | 转换sql | `varchar2` | 1000 | 是 | 转换sql语句 |
| 13 | `ismulti_lang_` | 使用多语言 | `integer` | - | 是 | 使用多语言:1,使用;0或null,不使用 |

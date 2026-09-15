# 泛微OA 数据表: `datashowparam`

- **所属模块**: `集成模块`
- **数据库表名**: `datashowparam`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 自增长主键 |
| 2 | `mainid` | 主表id | `integer` | - | 是 | 关联展现配置表(datashowset)id |
| 3 | `fieldname` | 数据字段名称 | `varchar2` | 800 | 是 | 数据字段名称 |
| 4 | `searchname` | 查询字段显示名称 | `varchar2` | 800 | 是 | 显示字段显示名称 |
| 5 | `transql` | 转换sql | `varchar2` | 1000 | 是 | 转换sql |
| 6 | `isshowname` | 是否为标题栏 | `integer` | - | 是 | 是否为标题栏  0 否 ； 1 是 |
| 7 | `width` | 宽度 | `integer` | - | 是 | 宽度 |

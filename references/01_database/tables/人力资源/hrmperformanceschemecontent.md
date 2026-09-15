# 泛微OA 数据表: `hrmperformanceschemecontent`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceschemecontent`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `schemeid` | 考核基本信息表id | `integer` | - | 是 | hrmperformancecheckscheme表的id |
| 3 | `type_c` | 考核类型 | `char` | 1 | 是 | 考核类型 |
| 4 | `percent_n` | 考核对象 | `integer` | - | 是 | 考核对象 |
| 5 | `cycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |

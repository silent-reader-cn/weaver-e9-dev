# 泛微OA 数据表: `hrmperformanceschemecontent`

- **中文名称**: 人员自定义考核方案内容
- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformanceschemecontent`
- **主键**: `id`
- **字段数**: `5`

> 说明：人员自定义考核方案

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `schemeid` | 考核基本信息表id | `integer` | - | 是 | 否 | 否 | - | 0 | hrmperformancecheckscheme表的id |
| 3 | `type_c` | 考核类型 | `char` | 1 | 是 | 否 | 否 | - | - | 考核类型 |
| 4 | `percent_n` | 考核对象 | `integer` | - | 是 | 否 | 否 | - | 0 | 考核对象 |
| 5 | `cycle` | 考核周期 | `char` | 1 | 是 | 否 | 否 | - | - | 考核周期 |

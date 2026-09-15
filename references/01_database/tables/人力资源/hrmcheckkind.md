# 泛微OA 数据表: `hrmcheckkind`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcheckkind`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `kindname` | 考核种类名称 | `varchar2` | 480 | 是 | 考核种类名称 |
| 3 | `checkcycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |
| 4 | `checkexpecd` | 考核期 | `integer` | - | 是 | 考核期 |
| 5 | `checkstartdate` | 考核开始日期 | `char` | 10 | 是 | 考核开始日期 |

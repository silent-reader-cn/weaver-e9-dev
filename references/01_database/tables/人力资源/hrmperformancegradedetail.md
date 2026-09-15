# 泛微OA 数据表: `hrmperformancegradedetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancegradedetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `gradeid` | 目标id | `integer` | - | 是 | 目标id |
| 3 | `grade` | 目标名称 | `varchar2` | 80 | 是 | 目标名称 |
| 4 | `condition1` | 数据源1 | `integer` | - | 是 | 数据源1 |
| 5 | `condition2` | 数据源2 | `integer` | - | 是 | 数据源2 |

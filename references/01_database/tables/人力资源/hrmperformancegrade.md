# 泛微OA 数据表: `hrmperformancegrade`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancegrade`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `gradename` | 等级名称 | `varchar2` | 800 | 是 | 等级名称 |
| 3 | `source` | 数据源 | `char` | 1 | 是 | 数据源 |
| 4 | `memo` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 5 | `status` | 是否起用 | `char` | 1 | 是 | 0启用，1关闭 |

# 泛微OA 数据表: `hrmannualmanagement`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmannualmanagement`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 用户id | `integer` | - | 是 | 用户id |
| 3 | `annualyear` | 年假年 | `varchar2` | 1000 | 是 | 年假年 |
| 4 | `annualdays` | 年假天数 | `float` | 53 | 是 | 年假天数 |
| 5 | `status` | 状态 | `integer` | - | 是 | 状态   1：有效 |

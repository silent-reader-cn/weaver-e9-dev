# 泛微OA 数据表: `hrmcareerinvite`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerinvite`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `careername` | 职位名称 | `varchar2` | 1000 | 是 | 职位名称 |
| 3 | `careerpeople` | 招聘人数 | `char` | 4 | 是 | 招聘人数 |
| 4 | `careerage` | 年龄 | `varchar2` | 1000 | 是 | 年龄 |
| 5 | `careersex` | 性别 | `char` | 1 | 是 | 0: 男；1：女；2：不限 |
| 6 | `careeredu` | 最低教育程度 | `char` | 1 | 是 | - |

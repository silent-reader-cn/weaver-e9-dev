# 泛微OA 数据表: `hrmtrainresource`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainresource`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `name` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 3 | `type_n` | 类型 | `integer` | - | 是 | 类型 |
| 4 | `fare` | 费用 | `varchar2` | 1000 | 是 | 费用 |
| 5 | `time` | 周期 | `varchar2` | 1000 | 是 | 周期 |
| 6 | `memo` | 备忘 | `varchar2` | 4000 | 是 | 备忘 |

# 泛微OA 数据表: `hrmsalarychange`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarychange`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `multresourceid` | 多人员id | `varchar2` | 255 | 是 | 多人员id 如：25,38,30 |
| 3 | `itemid` | 薪酬设置id | `integer` | - | 是 | 薪酬项设置id |
| 4 | `changedate` | 变更日期 | `char` | 10 | 是 | 薪酬变更日期 |
| 5 | `changetype` | 变更类型 | `char` | 1 | 是 | 变更类型 |
| 6 | `salary` | 工资 | `number` | (10,2) | 是 | 工资 |
| 7 | `changeresion` | 变更缘由 | `varchar2` | 4000 | 是 | 变更缘由 |
| 8 | `changeuser` | 操作人 | `integer` | - | 是 | 操作人 |
| 9 | `oldvalue` | 变更前工资 | `number` | (15,2) | 是 | 变更前工资 |
| 10 | `newvalue` | 变更后工资 | `number` | (15,2) | 是 | 变更后工资 |

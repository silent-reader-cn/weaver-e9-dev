# 泛微OA 数据表: `hrmsalarypaylog`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarypaylog`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 人力资源工资单日志记录表 |
| 2 | `changid` | 更改人id | `integer` | - | 是 | 更改人id |
| 3 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 4 | `changedate` | 更改日期 | `varchar2` | 80 | 是 | 更改日期 |
| 5 | `changetime` | 更改时间 | `varchar2` | 64 | 是 | 更改时间 |
| 6 | `payid` | 工资单id | `integer` | - | 是 | 工资单id |
| 7 | `itemid` | 薪酬id | `varchar2` | 80 | 是 | 薪酬id |
| 8 | `oldvalue` | 更改之前工资 | `number` | (15,2) | 是 | 更改之前工资 |
| 9 | `newvalue` | 更改之后工资 | `number` | (15,2) | 是 | 更改之后工资 |
| 10 | `changedset` | 是否应用到薪酬设置 | `integer` | - | 是 | 0否，1是 |

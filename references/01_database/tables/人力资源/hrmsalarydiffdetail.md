# 泛微OA 数据表: `hrmsalarydiffdetail`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarydiffdetail`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `itemid` | 薪酬设置id | `integer` | - | 是 | 薪酬设置id |
| 2 | `resourceid` | 被考勤人id | `integer` | - | 是 | 被考勤人id |
| 3 | `payid` | 工资id | `integer` | - | 是 | 工资id |
| 4 | `diffid` | 考勤id | `integer` | - | 是 | 考勤id |
| 5 | `difftypeid` | 考勤类型id | `integer` | - | 是 | 考勤类型id |
| 6 | `startdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 7 | `enddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 8 | `realcounttime` | 实际计算时间 | `integer` | - | 是 | 实际计算时间 |
| 9 | `realcountpay` | 实际计算金额 | `number` | (10,2) | 是 | 实际计算金额 |

# 泛微OA 数据表: `fnayearsperiodslist`

- **所属模块**: `财务管理`
- **数据库表名**: `fnayearsperiodslist`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `status` | 账期状态 | `integer` | - | 否 | 0：开启 ； 1：关闭 |
| 2 | `id` | 主键 | `integer` | - | 否 | - |
| 3 | `fnayearid` | 主表主键 | `integer` | - | 是 | fnayearsperiods表id |
| 4 | `periodsid` | 期间id | `integer` | - | 是 | 值等于：1~13，每一个会计年度均会有1~13行记录 |
| 5 | `fnayear` | 年度 | `char` | 4 | 是 | - |
| 6 | `startdate` | 开始日期 | `char` | 10 | 是 | - |
| 7 | `enddate` | 结束日期 | `char` | 10 | 是 | - |
| 8 | `isclose` | 作废 | `char` | 1 | 是 | - |
| 9 | `isactive` | 作废 | `char` | 1 | 是 | - |
| 10 | `fnayearperiodsid` | 期间描述字符串 | `char` | 6 | 是 | 数据格式： 201301、201302… 201312、201313 |

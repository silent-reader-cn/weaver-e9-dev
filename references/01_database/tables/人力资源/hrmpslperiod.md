# 泛微OA 数据表: `hrmpslperiod`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmpslperiod`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `pslyear` | 有效期年份 | `varchar2` | 240 | 是 | 有效期年份 |
| 3 | `startdate` | 开始日期 | `varchar2` | 240 | 是 | 开始日期 |
| 4 | `enddate` | 结束日期 | `varchar2` | 240 | 是 | 结束日期 |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 6 | `leavetype` | 请假类型 | `integer` | - | 是 | 请假类型 |

# 泛微OA 数据表: `hrmtraintest`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtraintest`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `trainid` | 培训信息id | `integer` | - | 是 | 培训信息id |
| 3 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 4 | `testdate` | 考核日期 | `char` | 10 | 是 | 考核日期 |
| 5 | `result` | 考核结果 | `integer` | - | 是 | 0 不及格  1 及格  2 良好  3 优秀 |
| 6 | `explain` | 说明 | `varchar2` | 4000 | 是 | 说明 |
| 7 | `testerid` | 考官 | `integer` | - | 是 | 考官 |

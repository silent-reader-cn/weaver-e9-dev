# 泛微OA 数据表: `hrminterviewresult`

- **所属模块**: `人力资源`
- **数据库表名**: `hrminterviewresult`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 应聘人员id | `integer` | - | 是 | 应聘人员id |
| 3 | `stepid` | 应聘人员所处步骤 | `integer` | - | 是 | 应聘人员所处步骤 |
| 4 | `result` | 考核结果 | `integer` | - | 是 | 考核结果 |
| 5 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 6 | `tester` | 考核者 | `integer` | - | 是 | 考核者 |
| 7 | `testdate` | 考核日期 | `char` | 10 | 是 | 考核日期 |

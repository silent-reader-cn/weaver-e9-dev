# 泛微OA 数据表: `hrminterview`

- **所属模块**: `人力资源`
- **数据库表名**: `hrminterview`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 应聘人员id | `integer` | - | 是 | 应聘人员id |
| 3 | `stepid` | 应聘人员所处步骤 | `integer` | - | 是 | 应聘人员所处步骤 |
| 4 | `date_n` | 面试日期 | `char` | 10 | 是 | 面试日期 |
| 5 | `time` | 面试时间 | `char` | 8 | 是 | 面试时间 |
| 6 | `address` | 面试地点 | `varchar2` | 1000 | 是 | 面试地点 |
| 7 | `notice` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 8 | `status` | 状态 | `integer` | - | 是 | 状态 |
| 9 | `interviewer` | 面试者 | `varchar2` | 1000 | 是 | 面试者 |

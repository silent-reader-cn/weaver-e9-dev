# 泛微OA 数据表: `hrmcareerplanstep`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerplanstep`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planid` | 招聘计划id | `integer` | - | 是 | 招聘计划id |
| 3 | `stepname` | 步骤名称 | `varchar2` | 1000 | 是 | 步骤名称 |
| 4 | `stepstartdate` | 步骤开始日期 | `char` | 10 | 是 | 步骤开始日期 |
| 5 | `stependdate` | 步骤结束日期 | `char` | 10 | 是 | 步骤结束日期 |

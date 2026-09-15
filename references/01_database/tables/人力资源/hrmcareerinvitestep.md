# 泛微OA 数据表: `hrmcareerinvitestep`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerinvitestep`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `inviteid` | 招聘信息id | `integer` | - | 是 | 招聘信息id |
| 3 | `name` | 步骤名称 | `varchar2` | 480 | 是 | 步骤名称 |
| 4 | `startdate` | 步骤开始日期 | `char` | 10 | 是 | 步骤开始日期 |
| 5 | `enddate` | 步骤结束日期 | `char` | 10 | 是 | 步骤结束日期 |
| 6 | `assessor` | 审核人id | `integer` | - | 是 | 审核人id |
| 7 | `assessstartdate` | 审核开始日期 | `char` | 10 | 是 | 审核开始日期 |
| 8 | `assessenddate` | 审核结束日期 | `char` | 10 | 是 | 审核结束日期 |
| 9 | `informdate` | 审核通知日期 | `char` | 10 | 是 | 审核通知日期 |

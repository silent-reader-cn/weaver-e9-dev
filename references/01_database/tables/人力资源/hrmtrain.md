# 泛微OA 数据表: `hrmtrain`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrain`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `planid` | 培训计划id | `integer` | - | 是 | 培训规划表hrmtrainplanrange主键id |
| 4 | `organizer` | 组织人 | `varchar2` | 1000 | 是 | 组织人 |
| 5 | `startdate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 6 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 7 | `content` | 培训内容 | `varchar2` | 4000 | 是 | 培训内容 |
| 8 | `aim` | 培训目的 | `varchar2` | 4000 | 是 | 培训目的 |
| 9 | `resource_n` | 被培训人id | `varchar2` | 1000 | 是 | 被培训人id |
| 10 | `address` | 培训地址 | `varchar2` | 1000 | 是 | 培训地址 |
| 11 | `testdate` | 考试日期 | `char` | 10 | 是 | 考试日期 |
| 12 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 13 | `summarizer` | 培训总结 | `integer` | - | 是 | 培训总结 |
| 14 | `summarizedate` | 培训总结时间 | `char` | 10 | 是 | 培训总结时间 |
| 15 | `fare` | 培训进展 | `float` | 22 | 是 | 培训进展 |
| 16 | `faretype` | 培训进展类别 | `integer` | - | 是 | 培训进展类别 |
| 17 | `advice` | 培训意见 | `varchar2` | 4000 | 是 | 培训意见 |

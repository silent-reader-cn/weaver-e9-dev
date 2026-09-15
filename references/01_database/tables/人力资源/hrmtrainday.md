# 泛微OA 数据表: `hrmtrainday`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainday`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `trainid` | 培训信息id | `integer` | - | 是 | 培训信息表hrmtrain主键id |
| 3 | `traindate` | 培训日期 | `char` | 10 | 是 | 培训日期 |
| 4 | `daytraincontent` | 培训日程内容 | `varchar2` | 4000 | 是 | 培训日程内容 |
| 5 | `daytrainaim` | 培训日程目标 | `varchar2` | 4000 | 是 | 培训日程目标 |
| 6 | `daytraineffect` | 培训日程影响程度 | `varchar2` | 4000 | 是 | 培训日程影响程度 |
| 7 | `daytrainplain` | 培训日程计划 | `varchar2` | 4000 | 是 | 培训日程计划 |
| 8 | `starttime` | 开始时间 | `char` | 5 | 是 | 开始时间 |
| 9 | `endtime` | 结束时间 | `char` | 5 | 是 | 结束时间 |

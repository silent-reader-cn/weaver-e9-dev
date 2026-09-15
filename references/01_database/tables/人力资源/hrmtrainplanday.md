# 泛微OA 数据表: `hrmtrainplanday`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainplanday`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planid` | 培训安排id | `integer` | - | 是 | 培训安排id |
| 3 | `plandate` | 培训日期 | `char` | 10 | 是 | 培训日期 |
| 4 | `plandaycontent` | 培训安排内容 | `varchar2` | 4000 | 是 | 培训安排内容 |
| 5 | `plandayaim` | 培训安排目标 | `varchar2` | 4000 | 是 | 培训安排目标 |
| 6 | `starttime` | 开始时间 | `char` | 5 | 是 | 开始时间 |
| 7 | `endtime` | 结束时间 | `char` | 5 | 是 | 结束时间 |

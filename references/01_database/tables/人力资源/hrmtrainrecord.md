# 泛微OA 数据表: `hrmtrainrecord`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainrecord`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `trainstartdate` | 培训开始时间 | `char` | 10 | 是 | 培训开始时间 |
| 4 | `trainenddate` | 培训结束时间 | `char` | 10 | 是 | 培训结束时间 |
| 5 | `traintype` | 培训类型 | `integer` | - | 是 | 培训类型 |
| 6 | `trainrecord` | 培训内容 | `varchar2` | 4000 | 是 | 培训内容 |
| 7 | `trainhour` | 培训时长 | `number` | (18,3) | 是 | 培训时长 |
| 8 | `trainunit` | 培训单位 | `varchar2` | 800 | 是 | 培训单位 |

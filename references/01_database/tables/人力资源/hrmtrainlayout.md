# 泛微OA 数据表: `hrmtrainlayout`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainlayout`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `layoutname` | 规划名称 | `varchar2` | 480 | 是 | 规划名称 |
| 3 | `typeid` | 培训类型id | `integer` | - | 是 | 培训类型id |
| 4 | `layoutstartdate` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 5 | `layoutenddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 6 | `layoutcontent` | 内容 | `varchar2` | 4000 | 是 | 内容 |
| 7 | `layoutaim` | 目标 | `varchar2` | 4000 | 是 | 目标 |
| 8 | `layouttestdate` | 考试时间 | `char` | 10 | 是 | 考试时间 |
| 9 | `layoutassessor` | 考官 | `varchar2` | 1000 | 是 | 考官 |

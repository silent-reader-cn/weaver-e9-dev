# 泛微OA 数据表: `govern_report`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_report`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `reportcontent` | 汇报内容 | `clob` | 4000 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `topic` | 汇报主题 | `varchar2` | 1000 | 是 | - |
| 4 | `reportdate` | 汇报日期 | `varchar2` | 10 | 是 | - |
| 5 | `reporttime` | 汇报时间 | `varchar2` | 8 | 是 | - |
| 6 | `taskid` | 任务id | `integer` | - | 否 | 对应govern_task表id |
| 7 | `reporter` | 汇报人 | `integer` | - | 是 | - |
| 8 | `progress` | 进度 | `integer` | - | 是 | - |
| 9 | `doc` | 对应文档id | `integer` | - | 是 | - |

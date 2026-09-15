# 泛微OA 数据表: `govern_prompt`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_prompt`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `promptcontent` | 催办内容 | `clob` | 4000 | 是 | - |
| 2 | `flag` | 是否显示催办标识 | `integer` | - | 是 | - |
| 3 | `id` | 数据id | `integer` | - | 否 | - |
| 4 | `topic` | 催办主题 | `varchar2` | 1000 | 是 | - |
| 5 | `promptdate` | 催办日期 | `varchar2` | 10 | 是 | - |
| 6 | `prompttime` | 催办时间 | `varchar2` | 8 | 是 | - |
| 7 | `taskid` | 对应任务id | `integer` | - | 否 | 对应govern_task表id |
| 8 | `prompter` | 催办人 | `integer` | - | 是 | - |
| 9 | `doc` | 催办成文 | `integer` | - | 是 | - |

# 泛微OA 数据表: `govern_instruct`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_instruct`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `content` | 批示内容 | `clob` | 4000 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `taskid` | 数据id | `integer` | - | 否 | 对应govern_task表id |
| 4 | `userid` | 用户id | `integer` | - | 是 | - |
| 5 | `instype` | 批示类型 | `integer` | - | 是 | 1任务批示 2汇报批示 3批示回复 |
| 6 | `insdate` | 批示日期 | `varchar2` | 10 | 是 | - |
| 7 | `instime` | 批示时间 | `varchar2` | 8 | 是 | - |
| 8 | `instructid` | 评论id | `integer` | - | 是 | 回复哪条批示 |
| 9 | `instructtopid` | 评论顶层id | `integer` | - | 是 | - |
| 10 | `isdelete` | 是否删除 | `integer` | - | 是 | 0正常 1删除 |

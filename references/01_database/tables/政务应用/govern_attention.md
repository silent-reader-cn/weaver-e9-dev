# 泛微OA 数据表: `govern_attention`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_attention`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `taskid` | 任务id | `integer` | - | 否 | 对应govern_task表id |
| 4 | `attdate` | 关注日期 | `varchar2` | 10 | 是 | - |
| 5 | `atttime` | 关注时间 | `varchar2` | 8 | 是 | - |

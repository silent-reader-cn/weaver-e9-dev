# 泛微OA 数据表: `info_feedback`

- **所属模块**: `政务应用`
- **数据库表名**: `info_feedback`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | 数据id |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 用于做主键返回 |
| 3 | `title` | 标题 | `varchar2` | 256 | 是 | - |
| 4 | `content` | 反馈内容 | `clob` | - | 是 | - |
| 5 | `feeder` | 反馈人 | `integer` | - | 是 | - |
| 6 | `feeddate` | 反馈日期 | `varchar2` | 10 | 是 | - |
| 7 | `feedtime` | 反馈时间 | `varchar2` | 8 | 是 | - |
| 8 | `infoid` | 上报信息id | `integer` | - | 是 | info_report主键id |
| 9 | `type` | 反馈类型 | `integer` | - | 是 | 0驳回 1反馈 |

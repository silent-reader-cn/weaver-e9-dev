# 泛微OA 数据表: `hrmonlineavg`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmonlineavg`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `online_year` | 在线时间-年 | `integer` | - | 是 | 在线时间-年 |
| 3 | `online_month` | 在线时间-月 | `integer` | - | 是 | 在线时间-月 |
| 4 | `online_date` | 在线日期 | `varchar2` | 10 | 是 | 在线日期 |
| 5 | `point_time` | 在线时长平均数 | `integer` | - | 是 | 在线时长平均数 |
| 6 | `online_num` | 在线次数平均数 | `integer` | - | 是 | 在线次数平均数 |
| 7 | `serverip` | 服务地址IP | `varchar2` | 400 | 是 | 服务地址IP |

# 泛微OA 数据表: `hrmonlinecount`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmonlinecount`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `online_date` | 在线日期 | `varchar2` | 10 | 是 | 在线日期 |
| 3 | `online_time` | 在线时间 | `varchar2` | 64 | 是 | 在线时间 |
| 4 | `online_num` | 在线次数 | `integer` | - | 是 | 在线次数 |
| 5 | `online_month` | 在线时间-年 | `integer` | - | 是 | 在线时间-年 |
| 6 | `online_year` | 在线时间-月 | `integer` | - | 是 | 在线时间-月 |
| 7 | `serverip` | 服务IP | `varchar2` | 400 | 是 | 服务IP |

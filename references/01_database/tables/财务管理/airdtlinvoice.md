# 泛微OA 数据表: `airdtlinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `airdtlinvoice`
- **文档收录字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `from_city` | 出发站 | `varchar2` | 1000 | - | - |
| 4 | `to_city` | 到达站 | `varchar2` | 1000 | - | - |
| 5 | `flight_number` | 航班号 | `varchar2` | 200 | - | - |
| 6 | `airdate` | 乘机日期 | `varchar2` | 200 | - | - |
| 7 | `airtime` | 乘机时间 | `varchar2` | 200 | - | - |
| 8 | `seat` | 座位等级 | `varchar2` | 200 | - | - |

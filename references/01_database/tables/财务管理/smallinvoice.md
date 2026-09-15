# 泛微OA 数据表: `smallinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `smallinvoice`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `discount` | 折扣 | `varchar2` | 200 | - | - |
| 2 | `id` | 主键 | `integer` | - | - | - |
| 3 | `mainid` | 发票台账id | `integer` | - | - | - |
| 4 | `storename` | 店名 | `varchar2` | 1000 | - | - |
| 5 | `time` | 时间 | `varchar2` | 200 | - | - |
| 6 | `tips` | 小费 | `varchar2` | 200 | - | - |
| 7 | `station_getoff` | 作废 | `varchar2` | 200 | - | - |
| 8 | `currency_code` | 币种 | `varchar2` | 200 | - | - |
| 9 | `type` | 消费类型 | `varchar2` | 200 | - | - |

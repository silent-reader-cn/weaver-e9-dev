# 泛微OA 数据表: `carinvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `carinvoice`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | - | - |
| 2 | `mainid` | 发票台账id | `integer` | - | - | - |
| 3 | `time` | 时间 | `varchar2` | 200 | - | - |
| 4 | `station_geton` | 出发车站 | `varchar2` | 1000 | - | - |
| 5 | `station_getoff` | 到达车站 | `varchar2` | 1000 | - | - |
| 6 | `name` | 姓名 | `varchar2` | 200 | - | - |

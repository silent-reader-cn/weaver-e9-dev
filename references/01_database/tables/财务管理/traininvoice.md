# 泛微OA 数据表: `traininvoice`

- **所属模块**: `财务管理`
- **数据库表名**: `traininvoice`
- **文档收录字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `station_getoff` | 下车车站 | `varchar2` | 1000 | - | - |
| 2 | `train_number` | 车次 | `varchar2` | 200 | - | - |
| 3 | `seat` | 座位类型 | `varchar2` | 200 | - | - |
| 4 | `id` | 主键 | `integer` | - | - | - |
| 5 | `mainid` | 发票台账id | `integer` | - | - | - |
| 6 | `time` | 乘车时间 | `varchar2` | 200 | - | - |
| 7 | `name` | 乘车人姓名 | `varchar2` | 200 | - | - |
| 8 | `station_geton` | 上车车站 | `varchar2` | 1000 | - | - |

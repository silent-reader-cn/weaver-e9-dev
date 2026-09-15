# 泛微OA 数据表: `hrmcitytwo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcitytwo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `cityname` | 城市名称 | `varchar2` | 1000 | 是 | 城市名称 |
| 3 | `citylongitude` | 城市经度 | `number` | (8,3) | 是 | 城市经度 |
| 4 | `citylatitude` | 城市纬度 | `number` | (8,3) | 是 | 城市纬度 |
| 5 | `cityid` | 一级城市id | `integer` | - | 是 | 一级城市id |
| 6 | `canceled` | 删除标记 | `char` | 1 | 是 | 删除标记 |

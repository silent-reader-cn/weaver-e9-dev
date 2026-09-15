# 泛微OA 数据表: `kq_location`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_location`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `locationname` | 办公地点名称 | `varchar2` | 500 | 否 | - |
| 3 | `longitude` | 经度 | `number` | - | 否 | - |
| 4 | `latitude` | 纬度 | `number` | - | 否 | - |
| 5 | `address` | 地址 | `varchar2` | 500 | 否 | - |
| 6 | `groupid` | 考勤组ID | `integer` | - | 否 | - |

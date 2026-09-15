# 泛微OA 数据表: `hrmvalidatecardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmvalidatecardinfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `stationid` | 打卡机号 | `char` | 2 | 是 | 打卡机号 |
| 3 | `carddate` | 打卡日期 | `char` | 10 | 是 | 打卡日期 |
| 4 | `cardtime` | 打开时间 | `char` | 5 | 是 | 打开时间 |
| 5 | `workshift` | 打卡组 | `char` | 1 | 是 | 打卡组 |
| 6 | `cardid` | 卡号 | `char` | 10 | 是 | 卡号 |

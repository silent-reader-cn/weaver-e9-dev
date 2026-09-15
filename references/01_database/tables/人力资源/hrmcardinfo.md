# 泛微OA 数据表: `hrmcardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcardinfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `stationid` | 卡钟的台号 | `char` | 2 | 是 | 卡钟的台号 |
| 3 | `carddate` | 打卡日期 | `char` | 10 | 是 | 格式：yyyy-mm-dd |
| 4 | `cardtime` | 打卡时间 | `char` | 5 | 是 | 格式：hh:nn |
| 5 | `workshift` | 班组 | `char` | 1 | 是 | 班组 |
| 6 | `cardid` | 卡号 | `char` | 10 | 是 | 卡号 |

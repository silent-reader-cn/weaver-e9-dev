# 泛微OA 数据表: `hrmrightcardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrightcardinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `carddate` | 打卡日期 | `char` | 10 | 是 | 打卡日期 |
| 4 | `cardtime` | 打卡时间 | `char` | 5 | 是 | 打卡时间 |
| 5 | `inorout` | 默认输入0 | `integer` | - | 是 | ,默认输入0 |
| 6 | `islegal` | 是否非法打卡 | `integer` | - | 是 | 1 正常，2非法 |
| 7 | `workout` | 是否处理 | `integer` | - | 是 | 1 未处理，2已处理 |

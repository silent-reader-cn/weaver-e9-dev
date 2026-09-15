# 泛微OA 数据表: `hrmpubholiday`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmpubholiday`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `countryid` | 所在国家id | `integer` | - | 是 | 所在国家id |
| 3 | `holidaydate` | 公众假日 | `char` | 10 | 是 | 公众假日 |
| 4 | `holidayname` | 公众假日描述 | `varchar2` | 1000 | 是 | 公众假日描述 |
| 5 | `changetype` | 类型 | `integer` | - | 是 | 类型（1-公共假日，2-调配工作日，3-调配休息日） |
| 6 | `relateweekday` | 对应工作日 | `integer` | - | 是 | 对应工作日 |

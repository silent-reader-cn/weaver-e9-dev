# 泛微OA 数据表: `hrmannualleaveinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmannualleaveinfo`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 请求id |
| 3 | `resourceid` | 请假人 | `integer` | - | 是 | 请假人 |
| 4 | `startdate` | 开始日期 | `varchar2` | 1000 | 是 | 开始日期 |
| 5 | `starttime` | 开始时间 | `varchar2` | 1000 | 是 | 开始时间 |
| 6 | `enddate` | 结束日期 | `varchar2` | 1000 | 是 | 结束日期 |
| 7 | `endtime` | 结束时间 | `varchar2` | 1000 | 是 | 结束时间 |
| 8 | `leavetime` | 请假时间 | `float` | 53 | 是 | 请假时间 |
| 9 | `occurdate` | 发生日期 | `varchar2` | 1000 | 是 | 发生日期 |
| 10 | `otherleavetype` | 其它请假类型 | `integer` | - | 是 | 其它请假类型 |
| 11 | `leavetype` | 请假类型 | `integer` | - | 是 | 请假类型 |
| 12 | `status` | 状态 | `integer` | - | 是 | 1：有效 |

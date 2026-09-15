# 泛微OA 数据表: `hrmtimecardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtimecardinfo`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `resourceid` | 用户id | `integer` | - | 是 | 用户id |
| 2 | `timecarddate` | 打卡时间 | `char` | 10 | 是 | 打卡时间 |
| 3 | `intime` | 签到时间 | `char` | 5 | 是 | 签到时间 |
| 4 | `outtime` | 签退时间 | `char` | 5 | 是 | 签退时间 |
| 5 | `relateshiftid` | 打卡时间类别 | `integer` | - | 是 | 0 作为正常的一般工作时间,1 作为加班的一般工作时间 |

# 泛微OA 数据表: `hrmschedulemaintance`

- **中文名称**: 人力资源考勤信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmschedulemaintance`
- **主键**: `id`
- **字段数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `diffid` | 考勤种类id | `integer` | - | 是 | 否 | 否 | - | - | 考勤种类id |
| 3 | `resourceid` | 人力资源id | `integer` | - | 是 | 否 | 否 | - | - | 人力资源id |
| 4 | `startdate` | 开始日期 | `char` | 10 | 是 | 否 | 否 | - | - | 开始日期 |
| 5 | `starttime` | 开始时间 | `char` | 8 | 是 | 否 | 否 | - | - | 开始时间 |
| 6 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | 结束日期 |
| 7 | `endtime` | 结束时间 | `char` | 8 | 是 | 否 | 否 | - | - | 结束时间 |
| 8 | `memo` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 备注 |
| 9 | `createtype` | 创建类别 | `integer` | - | 是 | 否 | 否 | - | (0) | 工作流或者直接输入 |
| 10 | `createrid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 创建人id |
| 11 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 创建日期 |
| 12 | `totalday` | 总的天数 | `integer` | - | 是 | 否 | 否 | - | (0) | 总的天数 |
| 13 | `totaltime` | 总的时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 总的时间 |
| 14 | `realdifftime` | 输入时间格式 | `integer` | - | 是 | 否 | 否 | - | 0 | 输入时间格式 |
| 15 | `realcarddifftime` | 时间格式 | `integer` | - | 是 | 否 | 否 | - | 0 | HrmWorkTimeWarp表里面的counttime字段 |
| 16 | `difftype` | 考勤种类 | `char` | 1 | 是 | 否 | 否 | - | - | HrmScheduleDiff表里的difftype字段 |

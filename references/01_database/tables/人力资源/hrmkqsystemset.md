# 泛微OA 数据表: `hrmkqsystemset`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmkqsystemset`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `tosomeone` | 收件人地址 | `varchar2` | 480 | 是 | 收件人地址 |
| 2 | `timeinterval` | 数据采集时间间隔(分钟) | `integer` | - | 是 | 数据采集时间间隔(分钟) |
| 3 | `getdatatype` | 数据采集方式 | `integer` | - | 是 | 类型为“510[本机端口采集]”、“350[tcp/ip采集]” |
| 4 | `getdatavalue` | 数据采集所得数据 | `varchar2` | 1000 | 是 | 数据采集方式为“510[本机端口采集]”时为com 端口号，数据采集方式为“350[tcp/ip采集]”时为ip 地址 |
| 5 | `avgworkhour` | 每月平均工作时间(小时) | `integer` | - | 是 | 每月平均工作时间(小时) |
| 6 | `salaryenddate` | 薪资计算截至日期(包含当天) | `integer` | - | 是 | 薪资计算截至日期(包含当天) |
| 7 | `signipscope` | 签到签退ip范围 | `varchar2` | 1000 | 是 | 签到签退ip范围 |
| 8 | `needsign` | 是否需要签到签退 | `integer` | - | 是 | 是否需要签到签退 |
| 9 | `onlyworkday` | 仅工作日 | `integer` | - | 是 | 仅工作日 |
| 10 | `signtimescope` | 签到时间范围 | `varchar2` | 1000 | 是 | 签到时间范围 |
| 11 | `needsignhasinit` | 是否签到签退初始化 | `integer` | - | 是 | 是否签到签退初始化 |

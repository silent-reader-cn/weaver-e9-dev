# 泛微OA 数据表: `mode_reminddata`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `subbillid` | 明细表id | `integer` | - | 是 | 对应明细表数据的id |
| 2 | `isremindsms` | 短信提醒 | `integer` | - | 是 | 短信提醒方式 |
| 3 | `isremindemail` | 邮件提醒 | `integer` | - | 是 | 邮件提醒方式 |
| 4 | `isremindworkflow` | 流程提醒 | `integer` | - | 是 | 流程提醒方式 |
| 5 | `isremindwechat` | 云桥微信提醒 | `integer` | - | 是 | 云桥微信提醒方式 |
| 6 | `isremindemobile` | emobile移动端提醒 | `integer` | - | 是 | emobile移动端提醒方式 |
| 7 | `id` | ID | `integer` | - | 否 | - |
| 8 | `billid` | 数据id | `integer` | - | 是 | 对应模块中uf表的数据的id |
| 9 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表的id |
| 10 | `remindjobid` | 提醒基本信息id | `integer` | - | 是 | 对应mode_remindjob表的id |
| 11 | `reminddate` | 提醒日期 | `varchar2` | 80 | 是 | 要提醒的日期 |
| 12 | `remindtime` | 提醒时间 | `varchar2` | 80 | 是 | 要提醒的时间 |
| 13 | `status` | 提醒状态 | `integer` | - | 是 | - |

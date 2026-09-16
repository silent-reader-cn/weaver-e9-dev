# 泛微OA 数据表: `mode_reminddata_all`

- **中文名称**: 数据提醒新表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata_all`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `isremindsms` | 短信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `isremindemail` | 邮件提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `isremindworkflow` | 流程提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `isremindwechat` | 微信云桥提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `isremindemobile` | e-mobile提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `billid` | 数据id | `varchar2` | 800 | 是 | 否 | 否 | - | - | 对应的是uf_xxx的id，也就是该提醒的模块的id |
| 7 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `remindjobid` | 提醒id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_remindjob的id |
| 9 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `subbillid` | 明细表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `lastdate` | 最后日期 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 12 | `lasttime` | 最后时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |

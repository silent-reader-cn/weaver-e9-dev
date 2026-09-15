# 泛微OA 数据表: `mode_reminddata_all`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata_all`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `isremindsms` | 短信提醒 | `integer` | - | 是 | - |
| 2 | `isremindemail` | 邮件提醒 | `integer` | - | 是 | - |
| 3 | `isremindworkflow` | 流程提醒 | `integer` | - | 是 | - |
| 4 | `isremindwechat` | 微信云桥提醒 | `integer` | - | 是 | - |
| 5 | `isremindemobile` | e-mobile提醒 | `integer` | - | 是 | - |
| 6 | `billid` | 数据id | `varchar2` | 800 | 是 | 对应的是uf_xxx的id，也就是该提醒的模块的id |
| 7 | `id` | id | `integer` | - | 是 | - |
| 8 | `remindjobid` | 提醒id | `integer` | - | 是 | 对应mode_remindjob的id |
| 9 | `modeid` | 模块id | `integer` | - | 是 | - |
| 10 | `subbillid` | 明细表id | `integer` | - | 是 | - |
| 11 | `lastdate` | 最后日期 | `varchar2` | 160 | 是 | - |
| 12 | `lasttime` | 最后时间 | `varchar2` | 160 | 是 | - |

# 泛微OA 数据表: `mode_reminddata_error`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata_error`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | - |
| 2 | `remindjobid` | 提醒id | `integer` | - | 是 | 对应mode_remindjob的id |
| 3 | `modeid` | 模块id | `integer` | - | 是 | - |
| 4 | `billid` | 数据id | `integer` | - | 是 | - |
| 5 | `subbillid` | 明细表id | `integer` | - | 是 | - |
| 6 | `createdate` | 创建日期 | `varchar2` | 160 | 是 | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 160 | 是 | - |
| 8 | `remindway` | 提醒方式 | `integer` | - | 是 | - |
| 9 | `remindwaydesc` | 提醒描述 | `varchar2` | 400 | 是 | - |
| 10 | `msg` | 错误信息 | `varchar2` | 4000 | 是 | - |
| 11 | `lastdate` | 最后日期 | `varchar2` | 160 | 是 | - |
| 12 | `lasttime` | 最后时间 | `varchar2` | 160 | 是 | - |

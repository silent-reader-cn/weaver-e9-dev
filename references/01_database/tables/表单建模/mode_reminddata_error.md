# 泛微OA 数据表: `mode_reminddata_error`

- **中文名称**: 记录提醒错误日志
- **所属模块**: `表单建模`
- **数据库表名**: `mode_reminddata_error`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `remindjobid` | 提醒id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_remindjob的id |
| 3 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `billid` | 数据id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `subbillid` | 明细表id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `createdate` | 创建日期 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 8 | `remindway` | 提醒方式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `remindwaydesc` | 提醒描述 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 10 | `msg` | 错误信息 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `lastdate` | 最后日期 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 12 | `lasttime` | 最后时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |

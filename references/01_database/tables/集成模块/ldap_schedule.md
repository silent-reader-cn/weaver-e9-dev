# 泛微OA 数据表: `ldap_schedule`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_schedule`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ldapid` | LDAP标识 | `varchar2` | 100 | 是 | LDAP标识 |
| 2 | `synctype` | 定时任务类型 | `varchar2` | 100 | 是 | pull:正向同步，push:反向同步 |
| 3 | `lastsyncdate` | 最后同步时间 | `varchar2` | 100 | 是 | 最后同步时间（增量同时有效） |
| 4 | `scheduleid` | 计划任务ID | `varchar2` | 100 | 是 | 计划任务ID |
| 5 | `syncmode` | 同步类型 | `char` | 1 | 是 | 1:全量同步，0:增量同步 |
| 6 | `cronexpr` | 同步时间表达式 | `varchar2` | 100 | 是 | 同步时间表达式 |
| 7 | `pointid` | 计划任务标识 | `varchar2` | 100 | 是 | 计划任务标识 |

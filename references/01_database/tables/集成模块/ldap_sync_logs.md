# 泛微OA 数据表: `ldap_sync_logs`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_sync_logs`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `logId` | 日志ID | `integer` | 11 | 否 | 日志ID |
| 2 | `ldapId` | LDAP标识 | `varchar2` | 100 | 是 | LDAP标识 |
| 3 | `syncType` | 同步类型 | `char` | 1 | 是 | 同步类型（1、正向同步 2、反向同步） |
| 4 | `syncMode` | 同步方式 | `char` | 1 | 是 | 同步方式（1、定时 2、手动） |
| 5 | `syncStatus` | 同步结果 | `char` | 1 | 是 | 同步结果（1、成功 2、失败） |
| 6 | `fileName` | 文件名称 | `varchar2` | 100 | 是 | 文件名 |
| 7 | `runTime` | 运行时间 | `varchar2` | 100 | 是 | 运行时间 |
| 8 | `startTime` | 开始时间 | `varchar2` | 100 | 是 | 同步开始时间 |
| 9 | `endTime` | 结束时间 | `varchar2` | 100 | 是 | 同步结束时间 |

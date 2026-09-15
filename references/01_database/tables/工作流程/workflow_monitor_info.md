# 泛微OA 数据表: `workflow_monitor_info`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_monitor_info`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `monitortype` | 监控类型 | `integer` | - | 否 | - |
| 3 | `flowcount` | 流程数量 | `integer` | - | 是 | - |
| 4 | `operatordate` | 操作日期 | `char` | 10 | 否 | - |
| 5 | `operatortime` | 操作时间 | `char` | 8 | 否 | - |
| 6 | `jktype` | 监控类型 | `integer` | - | 是 | 1、人力资源，2、角色，3、管理员账号 |
| 7 | `jkvalue` | 具体监控人值 | `varchar2` | 4000 | 是 | - |
| 8 | `operator` | 操作人 | `integer` | - | 否 | - |
| 9 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 10 | `fwtype` | 监控范围类型 | `integer` | - | 是 | - |

# 泛微OA 数据表: `workflow_monitor_detail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_monitor_detail`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `infoid` | 流程监控信息表id | `integer` | - | 是 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `operatordate` | 操作日期 | `char` | 10 | 是 | - |
| 4 | `operatortime` | 操作时间 | `char` | 8 | 是 | - |
| 5 | `isview` | 是否可查看流程内容 | `integer` | - | 是 | 1：可以，0：不可以 |
| 6 | `isintervenor` | 是否可干预流程流转 | `char` | 1 | 是 | 1：可以，0：不可以 |
| 7 | `isdelete` | 是否可删除 | `char` | 1 | 是 | 1：可以，0：不可以 |
| 8 | `isforcedrawback` | 是否可强制归档 | `char` | 1 | 是 | 1：可以，0：不可以 |
| 9 | `isforceover` | 是否可强制收回 | `char` | 1 | 是 | 1：可以，0：不可以 |
| 10 | `operator` | 操作人 | `integer` | - | 是 | - |
| 11 | `monitortype` | 监控类型 | `integer` | - | 是 | - |
| 12 | `subcompanyid` | 分部id | `integer` | - | 是 | - |
| 13 | `issooperator` | 是否可暂停撤销启用 | `char` | 1 | 是 | 1：可以，0：不可以 |

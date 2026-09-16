# 泛微OA 数据表: `actionexecutelog`

- **中文名称**: 流程流转集成调用日志表
- **所属模块**: `集成模块`
- **数据库表名**: `actionexecutelog`
- **主键**: `id`
- **字段数**: `11`

> 说明：记录流程流转每日调用次数

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 无 |
| 2 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 无 |
| 3 | `clientip` | 客户端IP | `char` | 15 | 是 | 否 | 否 | - | - | 无 |
| 4 | `actiondbid` | 未知字段 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 5 | `execresult` | 执行结果 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 6 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | 无 |
| 7 | `actionid` | action标识或id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 8 | `actiontype` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 9 | `datashowcount` | 调用次数 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 10 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 无 |
| 11 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | 无 |

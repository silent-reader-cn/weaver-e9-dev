# 泛微OA 数据表: `docsubscribe`

- **所属模块**: `知识管理`
- **数据库表名**: `docsubscribe`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `hrmid` | 订阅申请者id | `integer` | - | 是 | - |
| 4 | `ownerid` | 文档所有者id | `integer` | - | 是 | - |
| 5 | `subscribedate` | 订阅申请日期 | `char` | 10 | 是 | - |
| 6 | `approvedate` | 审批日期 | `char` | 10 | 是 | - |
| 7 | `searchcase` | 搜索条件 | `varchar2` | 1000 | 是 | - |
| 8 | `othersubscribe` | 其他订阅 | `varchar2` | 1000 | 是 | - |
| 9 | `subscribedesc` | 订阅说明 | `varchar2` | 1000 | 是 | - |
| 10 | `getbackdesc` | 退回说明 | `varchar2` | 1000 | 是 | - |
| 11 | `state` | 订阅状态 | `char` | 1 | 是 | 1.已申请，2.已批准，3.已收回 |
| 12 | `subscribetype` | 订阅申请者类型 | `integer` | - | 是 | 1：内部用户，2：外部用户 |
| 13 | `ownertype` | 文档所有者类型 | `integer` | - | 是 | 1：内部用户，2：外部用户 |

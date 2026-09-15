# 泛微OA 数据表: `workflow_requestsign`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestsign`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | - |
| 3 | `nodeid` | 节点id | `integer` | - | 是 | - |
| 4 | `userid` | 用户id | `integer` | - | 是 | - |
| 5 | `logintype` | 用户类型 | `integer` | - | 是 | 1：内部用户,2：外部用户 |
| 6 | `signnum` | 签章数目 | `integer` | - | 是 | 负数表示撤销签章的数目 |
| 7 | `signdate` | 签章日期 | `char` | 10 | 是 | - |
| 8 | `signtime` | 签章时间 | `char` | 8 | 是 | - |

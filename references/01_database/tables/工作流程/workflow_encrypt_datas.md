# 泛微OA 数据表: `workflow_encrypt_datas`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_encrypt_datas`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | - |
| 2 | `requestid` | 请求id | `integer` | - | 是 | workflow_requestbase的id |
| 3 | `logid` | 日志id | `integer` | - | 是 | workflow_requestlog表的logid |
| 4 | `configstr` | 配置信息 | `clob` | - | 是 | 流程节点上配置的数据保护信息的记录，DES加密 |
| 5 | `uuidstr` | uuid | `varchar2` | 100 | 是 | - |
| 6 | `sourcestr` | 被保护数据的源数据 | `clob` | - | 是 | 被保护的数据的源数据，DES加密 |
| 7 | `encryptkey` | 源加密数据使用的key | `varchar2` | 100 | 是 | - |
| 8 | `encryptstr` | 被保护数据的加密后数据 | `clob` | - | 是 | - |
| 9 | `userid` | 用户id | `integer` | - | 是 | - |
| 10 | `usertype` | 用户类型 | `integer` | - | 是 | 0：用户，1：客户 |
| 11 | `createtime` | 创建时间 | `varchar2` | 20 | 是 | - |

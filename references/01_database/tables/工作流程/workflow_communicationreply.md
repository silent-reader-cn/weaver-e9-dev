# 泛微OA 数据表: `workflow_communicationreply`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationreply`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `contentid` | 被回复内容id | `integer` | - | 是 | - |
| 3 | `remark` | 内容 | `varchar2` | 4000 | 是 | - |
| 4 | `createuser` | 创建人 | `integer` | - | 是 | - |
| 5 | `resiveuser` | 被回复人 | `integer` | - | 是 | - |
| 6 | `createdate` | 创建日期 | `char` | 20 | 是 | - |
| 7 | `createtime` | 创建时间 | `char` | 20 | 是 | - |
| 8 | `replyid` | 被回复的回复id | `integer` | - | 是 | - |

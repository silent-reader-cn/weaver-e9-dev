# 泛微OA 数据表: `workflow_communicationreply`

- **中文名称**: 相关交流回复表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationreply`
- **主键**: `id`
- **字段数**: `8`

> 说明：相关交流回复

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `contentid` | 被回复内容id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `remark` | 内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `createuser` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `resiveuser` | 被回复人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `createdate` | 创建日期 | `char` | 20 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 创建时间 | `char` | 20 | 是 | 否 | 否 | - | - | - |
| 8 | `replyid` | 被回复的回复id | `integer` | - | 是 | 否 | 否 | - | - | - |

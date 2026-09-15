# 泛微OA 数据表: `social_imchatresource`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imchatresource`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 是 | 主键id |
| 2 | `resourceid` | 文档或者流程id | `integer` | - | 是 | 流程id |
| 3 | `resourcename` | 文档或者流程的标题 | `varchar2` | 800 | 是 | 流程的标题 |
| 4 | `resourcedesc` | 文档或者流程详细信息 | `varchar2` | 800 | 是 | 流程详细信息 |
| 5 | `resourcetype` | 文档或者流程 | `char` | 2 | 是 | 文档或者流程 |
| 6 | `creatorid` | 发送人id | `integer` | - | 是 | 发送人id |
| 7 | `createtime` | 创建时间 | `varchar2` | 800 | 是 | 创建时间 |
| 8 | `targetid` | 接收者 | `varchar2` | 800 | 是 | 接收者 |
| 9 | `targettype` | 接收者类型 | `varchar2` | 160 | 是 | 群或者对话 |
| 10 | `memberids` | 权限id集合 | `varchar2` | 1000 | 是 | 权限id集合 |

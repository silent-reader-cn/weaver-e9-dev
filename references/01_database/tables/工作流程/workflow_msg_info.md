# 泛微OA 数据表: `workflow_msg_info`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_msg_info`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `requestid` | requestid | `integer` | - | 是 | - |
| 2 | `msgtype` | 消息类型 | `varchar2` | 4 | 是 | - |
| 3 | `msgtypedesc` | 消息描述 | `varchar2` | 40 | 是 | - |
| 4 | `targetid` | 目标id | `varchar2` | 4000 | 是 | - |
| 5 | `detailinfo` | 详细内容 | `clob` | 4000 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 20 | 是 | - |

# 泛微OA 数据表: `workflow_subwfrequest`

- **中文名称**: 子流程请求表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_subwfrequest`
- **主键**: `subrequestid`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `subwfid` | 子流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `subrequestid` | 子流程请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `mainrequestid` | 主流程请求id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `issame` | 是否相同 | `char` | 1 | 是 | 否 | 否 | - | - | - |

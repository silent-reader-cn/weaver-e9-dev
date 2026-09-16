# 泛微OA 数据表: `bill_hrmdismiss`

- **中文名称**: 工作流单据表（离职申请）
- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmdismiss`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `dismissdate` | 离职时间 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 4 | `docid` | 离职合同 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `dismissreason` | 离职原因 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 否 | 否 | - | - | 对应表workflow_requestbase中的字段requestid |
| 7 | `manager` | 经理 | `integer` | - | 是 | 否 | 否 | - | - | - |

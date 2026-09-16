# 泛微OA 数据表: `bill_hrmtrainplan`

- **中文名称**: 工作流单据表 (培训申请)
- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmtrainplan`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `resource_n` | 申请人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `trainplanid` | 培训安排 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `reason` | 说明 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `createdate` | 培训日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 6 | `requestid` | 工作流请求的ID | `integer` | - | 是 | 否 | 否 | - | - | 对应表workflow_requestbase中的字段requestid |

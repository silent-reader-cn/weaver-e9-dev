# 泛微OA 数据表: `fnafeewfinfocoststandard`

- **中文名称**: 费用标准流程设置表
- **所属模块**: `财务管理`
- **数据库表名**: `fnafeewfinfocoststandard`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `workflowid` | wfid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `enable` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fnawftype` | 财务流程类型 | `varchar2` | 50 | 是 | 否 | 否 | - | - | - |
| 5 | `overstandardtips` | 超费用标准自定义提醒信息 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `lastmodifieddate` | 最后修改日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |

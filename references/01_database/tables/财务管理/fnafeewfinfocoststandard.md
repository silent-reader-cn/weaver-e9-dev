# 泛微OA 数据表: `fnafeewfinfocoststandard`

- **所属模块**: `财务管理`
- **数据库表名**: `fnafeewfinfocoststandard`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `workflowid` | wfid | `integer` | - | 是 | - |
| 3 | `enable` | 是否启用 | `integer` | - | 是 | - |
| 4 | `fnawftype` | 财务流程类型 | `varchar2` | 50 | 是 | - |
| 5 | `overstandardtips` | 超费用标准自定义提醒信息 | `varchar2` | 4000 | 是 | - |
| 6 | `lastmodifieddate` | 最后修改日期 | `char` | 10 | 是 | - |

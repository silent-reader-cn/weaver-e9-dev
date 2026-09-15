# 泛微OA 数据表: `exp_workflowdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_workflowdetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 3 | `workflowname` | 流程名称 | `varchar2` | 1000 | 是 | - |
| 4 | `workflowtype` | 流程类型 | `integer` | - | 是 | - |
| 5 | `expid` | 选择方案id | `integer` | - | 是 | exp_ProList里的id |
| 6 | `createdate` | 方案创建日期 | `varchar2` | 160 | 是 | - |
| 7 | `creator` | 方案创建人 | `integer` | - | 是 | - |

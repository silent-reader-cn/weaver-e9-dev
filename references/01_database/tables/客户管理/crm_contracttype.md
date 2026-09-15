# 泛微OA 数据表: `crm_contracttype`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_contracttype`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `contractdesc` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `workflowid` | 工作流ID | `integer` | - | 是 | 工作流ID |
| 5 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |

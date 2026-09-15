# 泛微OA 数据表: `crm_customertype`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customertype`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `fullname` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `description` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 4 | `candelete` | 能否删除 | `char` | 1 | 是 | n:不可删除 |
| 5 | `canedit` | 能否编辑 | `char` | 1 | 是 | n:不可编辑 |
| 6 | `workflowid` | 流程ID | `integer` | - | 是 | 流程ID |
| 7 | `orderkey` | 排序字段 | `integer` | - | 是 | 排序字段 |

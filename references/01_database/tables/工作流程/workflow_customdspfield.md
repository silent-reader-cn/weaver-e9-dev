# 泛微OA 数据表: `workflow_customdspfield`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customdspfield`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `customid` | 流程自定义查询主明细表id | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 4 | `ifquery` | 是否作为查询条件 | `char` | 1 | 是 | 0、否，1、是 |
| 5 | `ifshow` | 是否显示列表标题 | `char` | 1 | 是 | 0、否，1、是 |
| 6 | `showorder` | 显示列表标题顺序 | `integer` | - | 是 | - |
| 7 | `queryorder` | 查询显示顺序 | `integer` | - | 是 | - |

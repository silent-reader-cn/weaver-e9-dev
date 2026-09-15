# 泛微OA 数据表: `fnarptrulesetdtl`

- **所属模块**: `财务管理`
- **数据库表名**: `fnarptrulesetdtl`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `mainid` | FnaRptRuleSet表pk | `integer` | - | 否 | - |
| 3 | `showid` | 权限id类型 | `integer` | - | 否 | 1:表示showid的值是-分部id；2：表示showid的值是-部门id；18004：表示showid的值是-成本中心id； |
| 4 | `showidtype` | 权限id | `integer` | - | 否 | - |

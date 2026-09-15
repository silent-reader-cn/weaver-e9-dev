# 泛微OA 数据表: `fnaruleset`

- **所属模块**: `财务管理`
- **数据库表名**: `fnaruleset`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `allowfb` | 是否允许分部 | `integer` | - | 是 | - |
| 2 | `allowbm` | 是否允许部门 | `integer` | - | 是 | - |
| 3 | `allowfcc` | 是否允许成本中心 | `integer` | - | 是 | - |
| 4 | `id` | 主键 | `integer` | - | 否 | - |
| 5 | `roleid` | 角色id | `integer` | - | 否 | - |
| 6 | `allowzb` | 是否有总部权限 | `integer` | - | 否 | 1：有；其他：没有； |
| 7 | `name` | 名称 | `varchar2` | 4000 | 是 | - |

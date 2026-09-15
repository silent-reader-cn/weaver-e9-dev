# 泛微OA 数据表: `hrmperformancecheckrule`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancecheckrule`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `rulename` | 权重名称 | `varchar2` | 800 | 是 | 权重名称 |
| 3 | `memo` | 规则定义 | `varchar2` | 1000 | 是 | 规则定义 |
| 4 | `status` | 是否启用 | `char` | 1 | 是 | 0启用，1关闭 |

# 泛微OA 数据表: `hrmtrainplanrange`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainplanrange`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `planid` | 计划id | `integer` | - | 是 | 计划id |
| 3 | `type_n` | 培训公开范围类型 | `integer` | - | 是 | 培训公开范围类型 |
| 4 | `resourceid` | 人力资源 | `integer` | - | 是 | 如果公开类型为人力资源 |
| 5 | `seclevel` | 安全级别 从 | `integer` | - | 是 | 安全级别 从 |
| 6 | `seclevel_to` | 安全级别 到 | `integer` | - | 是 | 安全级别 到 |

# 泛微OA 数据表: `hrmcareerplaninform`

- **中文名称**: 人力资源招聘计划通知表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerplaninform`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `careerplanid` | 招聘计划id | `integer` | - | 否 | 否 | 否 | - | - | 招聘计划id |
| 3 | `resourceid` | 人力资源id | `integer` | - | 否 | 否 | 否 | - | - | 人力资源id |
| 4 | `type` | 通知类型 | `integer` | - | 否 | 否 | 否 | - | 0 | 通知类型 |
| 5 | `stepid` | 步骤id | `integer` | - | 否 | 否 | 否 | - | - | hrmcareerplaninform stepid |

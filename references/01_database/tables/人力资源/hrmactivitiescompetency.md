# 泛微OA 数据表: `hrmactivitiescompetency`

- **中文名称**: 职责技能表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmactivitiescompetency`
- **主键**: `id`
- **字段数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `jobactivityid` | 对应的职责id | `integer` | - | 是 | 否 | 否 | - | - | HrmJobActivities职责表id |
| 3 | `competencyid` | 对应的技能id | `integer` | - | 是 | 否 | 否 | - | - | HrmCompetency技能表id |

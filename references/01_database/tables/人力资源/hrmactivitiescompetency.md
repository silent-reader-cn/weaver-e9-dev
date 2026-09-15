# 泛微OA 数据表: `hrmactivitiescompetency`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmactivitiescompetency`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `jobactivityid` | 对应的职责id | `integer` | - | 是 | HrmJobActivities职责表id |
| 3 | `competencyid` | 对应的技能id | `integer` | - | 是 | HrmCompetency技能表id |

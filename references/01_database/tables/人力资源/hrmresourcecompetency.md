# 泛微OA 数据表: `hrmresourcecompetency`

- **中文名称**: 人力资源能力表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcecompetency`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 否 | 否 | - | - | 人力资源id |
| 3 | `competencyid` | 技能id | `integer` | - | 是 | 否 | 否 | - | - | HrmCompetency表技能id |
| 4 | `lastgrade` | 前一次分数 | `float` | 22 | 是 | 否 | 否 | - | - | 前一次分数 |
| 5 | `lastdate` | 前一次评分日期 | `char` | 10 | 是 | 否 | 否 | - | - | 前一次评分日期 |
| 6 | `currentgrade` | 最新分数 | `float` | 22 | 是 | 否 | 否 | - | - | 最新分数 |
| 7 | `currentdate` | 最新评分日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最新评分日期 |
| 8 | `countgrade` | 总分数 | `float` | 22 | 是 | 否 | 否 | - | - | 所有次数的总和 |
| 9 | `counttimes` | 评测次数 | `integer` | - | 是 | 否 | 否 | - | - | 供平均分用 |

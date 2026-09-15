# 泛微OA 数据表: `hrmresourcecompetency`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcecompetency`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `competencyid` | 技能id | `integer` | - | 是 | HrmCompetency表技能id |
| 4 | `lastgrade` | 前一次分数 | `float` | 22 | 是 | 前一次分数 |
| 5 | `lastdate` | 前一次评分日期 | `char` | 10 | 是 | 前一次评分日期 |
| 6 | `currentgrade` | 最新分数 | `float` | 22 | 是 | 最新分数 |
| 7 | `currentdate` | 最新评分日期 | `char` | 10 | 是 | 最新评分日期 |
| 8 | `countgrade` | 总分数 | `float` | 22 | 是 | 所有次数的总和 |
| 9 | `counttimes` | 评测次数 | `integer` | - | 是 | 供平均分用 |

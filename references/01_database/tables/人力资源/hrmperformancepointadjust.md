# 泛微OA 数据表: `hrmperformancepointadjust`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancepointadjust`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `pointid` | 计划id | `integer` | - | 是 | 计划id |
| 3 | `content` | 内容 | `varchar2` | 4000 | 是 | 内容 |
| 4 | `adjustdate` | 修正时间 | `varchar2` | 80 | 是 | 修正时间 |
| 5 | `adjustperson` | 修正人员 | `integer` | - | 是 | 修正人员 |
| 6 | `point_before` | 修正前分数 | `number` | (10,0) | 是 | 修正前分数 |
| 7 | `point_after` | 修正后分数 | `number` | (10,3) | 是 | 修正后分数 |

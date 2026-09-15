# 泛微OA 数据表: `hrmperformancecheckpoint`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancecheckpoint`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `cycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |
| 3 | `checktype` | 考核类型 | `char` | 1 | 是 | 考核类型 |
| 4 | `checkdate` | 考核日期 | `varchar2` | 80 | 是 | 考核日期 |
| 5 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 6 | `point1` | 分数1 | `number` | (10,3) | 是 | 分数1 |
| 7 | `point2` | 分数2 | `number` | (10,3) | 是 | 分数2 |
| 8 | `point3` | 分数3 | `number` | (10,3) | 是 | 分数3 |
| 9 | `point4` | 分数4 | `number` | (10,3) | 是 | 分数4 |
| 10 | `point5` | 分数5 | `number` | (10,3) | 是 | 分数5 |
| 11 | `point6` | 分数6 | `number` | (10,3) | 是 | 分数6 |
| 12 | `point7` | 分数7 | `number` | (10,1) | 是 | 分数7 |
| 13 | `point8` | 分数8 | `varchar2` | 1000 | 是 | 分数8 |
| 14 | `content` | 描述 | `varchar2` | 4000 | 是 | 描述 |
| 15 | `memo` | 规则定义 | `varchar2` | 4000 | 是 | 规则定义 |
| 16 | `ruleids` | 考核权重id | `varchar2` | 1000 | 是 | 考核权重id |

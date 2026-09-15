# 泛微OA 数据表: `hrmrewardbeforework`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmrewardbeforework`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `rewardname` | 奖励名称 | `varchar2` | 1000 | 是 | 奖励名称 |
| 4 | `rewarddate` | 奖励时间 | `char` | 10 | 是 | 奖励时间 |
| 5 | `rewardmemo` | 备注 | `varchar2` | 4000 | 是 | 备注 |

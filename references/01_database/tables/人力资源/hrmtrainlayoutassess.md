# 泛微OA 数据表: `hrmtrainlayoutassess`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainlayoutassess`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `layoutid` | 培训信息id | `integer` | - | 是 | 培训信息id |
| 3 | `assessorid` | 考官id | `integer` | - | 是 | 考官id |
| 4 | `assessdate` | 考评日期 | `char` | 10 | 是 | 考评日期 |
| 5 | `implement` | 培训考评结果 | `char` | 1 | 是 | 0 极差 1 差  2 一般  3 好  4 很好 |
| 6 | `explain` | 说明 | `varchar2` | 4000 | 是 | 说明 |
| 7 | `advice` | 意见 | `varchar2` | 4000 | 是 | 意见 |

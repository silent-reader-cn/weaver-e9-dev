# 泛微OA 数据表: `hrmtrainassess`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainassess`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `trainid` | 培训信息id | `integer` | - | 是 | 培训信息id |
| 3 | `resourceid` | 人员id | `integer` | - | 是 | 人力资源hrmresource主键id |
| 4 | `assessdate` | 培训评估日期 | `char` | 10 | 是 | 培训评估日期 |
| 5 | `implement` | 培训考评结果 | `integer` | - | 是 | 0 极差 1 差  2 一般  3 好  4 很好 |
| 6 | `explain` | 说明 | `varchar2` | 4000 | 是 | 说明 |

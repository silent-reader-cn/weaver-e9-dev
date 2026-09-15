# 泛微OA 数据表: `hrmapplyremark`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmapplyremark`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `applyid` | 关联id | `integer` | - | 是 | hrmcareerapply表的id |
| 3 | `remark` | 详情 | `varchar2` | 1000 | 是 | 详情 |
| 4 | `resourceid` | 人员id | `integer` | - | 是 | 人力资源表id |
| 5 | `date_n` | 日期 | `char` | 10 | 是 | 日期 |
| 6 | `time` | 时间 | `char` | 8 | 是 | 时间 |

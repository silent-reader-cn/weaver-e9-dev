# 泛微OA 数据表: `hrmchecklist`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmchecklist`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `checkname` | 每一次考核的名称 | `varchar2` | 480 | 是 | 每一次考核的名称 |
| 3 | `checktypeid` | 考核种类的id | `integer` | - | 是 | 考核种类的id |
| 4 | `startdate` | 考核的开始日期 | `char` | 10 | 是 | 考核的开始日期 |
| 5 | `enddate` | 考核的结束日期 | `char` | 10 | 是 | 考核的结束日期 |
| 6 | `status` | 状态 | `integer` | - | 是 | 状态 |

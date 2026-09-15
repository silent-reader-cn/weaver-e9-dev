# 泛微OA 数据表: `hrmannualperiod`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmannualperiod`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `annualyear` | 年假年 | `varchar2` | 1000 | 是 | 年假年 |
| 3 | `startdate` | 年假开始日期 | `varchar2` | 1000 | 是 | 年假开始日期 |
| 4 | `enddate` | 年假结束日期 | `varchar2` | 1000 | 是 | 年假结束日期 |
| 5 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |

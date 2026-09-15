# 泛微OA 数据表: `hrmsalarycomponent`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarycomponent`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `componentname` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 3 | `countryid` | 国家id | `integer` | - | 是 | 国家id |
| 4 | `jobactivityid` | 职务id | `integer` | - | 是 | 职务id |
| 5 | `componenttype` | 所属类型 | `char` | 1 | 是 | 所属类型 |
| 6 | `componentperiod` | 工资期间 | `char` | 1 | 是 | 工资期间 |
| 7 | `currencyid` | 币种id | `integer` | - | 是 | 币种id |
| 8 | `ledgerid` | 对账id | `integer` | - | 是 | 对账id |
| 9 | `docid` | 文档id | `integer` | - | 是 | 文档id |
| 10 | `startdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 11 | `enddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 12 | `includetex` | 是否包含 | `char` | 1 | 是 | 0代表否，1代表是。 |
| 13 | `componenttypeid` | 所属类型id | `integer` | - | 是 | 所属类型id |

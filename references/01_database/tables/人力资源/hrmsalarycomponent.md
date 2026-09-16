# 泛微OA 数据表: `hrmsalarycomponent`

- **中文名称**: 人力资源原有工资类型
- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarycomponent`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `componentname` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 名称 |
| 3 | `countryid` | 国家id | `integer` | - | 是 | 否 | 否 | - | - | 国家id |
| 4 | `jobactivityid` | 职务id | `integer` | - | 是 | 否 | 否 | - | - | 职务id |
| 5 | `componenttype` | 所属类型 | `char` | 1 | 是 | 否 | 否 | - | - | 所属类型 |
| 6 | `componentperiod` | 工资期间 | `char` | 1 | 是 | 否 | 否 | - | - | 工资期间 |
| 7 | `currencyid` | 币种id | `integer` | - | 是 | 否 | 否 | - | - | 币种id |
| 8 | `ledgerid` | 对账id | `integer` | - | 是 | 否 | 否 | - | - | 对账id |
| 9 | `docid` | 文档id | `integer` | - | 是 | 否 | 否 | - | - | 文档id |
| 10 | `startdate` | 开始时间 | `char` | 10 | 是 | 否 | 否 | - | - | 开始时间 |
| 11 | `enddate` | 结束时间 | `char` | 10 | 是 | 否 | 否 | - | - | 结束时间 |
| 12 | `includetex` | 是否包含 | `char` | 1 | 是 | 否 | 否 | - | - | 0代表否，1代表是。 |
| 13 | `componenttypeid` | 所属类型id | `integer` | - | 是 | 否 | 否 | - | - | 所属类型id |

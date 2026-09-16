# 泛微OA 数据表: `hrmresourcecomponent`

- **中文名称**: 人力资源工资表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcecomponent`
- **主键**: `id`
- **字段数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 否 | 否 | - | - | 人力资源id |
| 3 | `componentid` | 财务要素id | `integer` | - | 是 | 否 | 否 | - | - | HrmSalaryComponent财务要素id |
| 4 | `componentmark` | 详细标识 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 详细标识 |
| 5 | `ledgerid` | 科目id | `integer` | - | 是 | 否 | 否 | - | - | 科目id |
| 6 | `componentperiod` | 工资期间 | `char` | 1 | 是 | 否 | 否 | - | - | 工资期间 |
| 7 | `selbank` | 工资银行 | `char` | 1 | 是 | 否 | 否 | - | - | 工资银行 |
| 8 | `bankid` | 银行id | `integer` | - | 是 | 否 | 否 | - | - | 银行id |
| 9 | `salarysum` | 金额 | `number` | (10,3) | 是 | 否 | 否 | - | - | 金额 |
| 10 | `canedit` | 是否可编辑 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否,1:是 |
| 11 | `currencyid` | 币种 | `integer` | - | 是 | 否 | 否 | - | - | 币种 |
| 12 | `startdate` | 起始日期 | `char` | 10 | 是 | 否 | 否 | - | - | 起始日期 |
| 13 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | 结束日期 |
| 14 | `hasused` | 已使用 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否,1:是 |
| 15 | `remark` | 备注 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 备注 |
| 16 | `createid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 创建人id |
| 17 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 创建日期 |
| 18 | `lastmoderid` | 最后修改人 | `integer` | - | 是 | 否 | 否 | - | - | 最后修改人 |
| 19 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最后修改日期 |

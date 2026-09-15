# 泛微OA 数据表: `hrmresourcecomponent`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcecomponent`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `componentid` | 财务要素id | `integer` | - | 是 | HrmSalaryComponent财务要素id |
| 4 | `componentmark` | 详细标识 | `varchar2` | 480 | 是 | 详细标识 |
| 5 | `ledgerid` | 科目id | `integer` | - | 是 | 科目id |
| 6 | `componentperiod` | 工资期间 | `char` | 1 | 是 | 工资期间 |
| 7 | `selbank` | 工资银行 | `char` | 1 | 是 | 工资银行 |
| 8 | `bankid` | 银行id | `integer` | - | 是 | 银行id |
| 9 | `salarysum` | 金额 | `number` | (10,3) | 是 | 金额 |
| 10 | `canedit` | 是否可编辑 | `char` | 1 | 是 | 0:否,1:是 |
| 11 | `currencyid` | 币种 | `integer` | - | 是 | 币种 |
| 12 | `startdate` | 起始日期 | `char` | 10 | 是 | 起始日期 |
| 13 | `enddate` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 14 | `hasused` | 已使用 | `char` | 1 | 是 | 0:否,1:是 |
| 15 | `remark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 16 | `createid` | 创建人id | `integer` | - | 是 | 创建人id |
| 17 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 18 | `lastmoderid` | 最后修改人 | `integer` | - | 是 | 最后修改人 |
| 19 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 最后修改日期 |

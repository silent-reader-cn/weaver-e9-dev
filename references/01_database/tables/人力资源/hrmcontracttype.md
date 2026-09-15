# 泛微OA 数据表: `hrmcontracttype`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcontracttype`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `typename` | 合同种类名称 | `varchar2` | 1000 | 是 | 合同种类名称 |
| 3 | `contracttempletid` | 合同模板id | `integer` | - | 是 | 合同模板id |
| 4 | `saveurl` | 合同文档目录 | `varchar2` | 1000 | 是 | 合同文档目录 |
| 5 | `ishirecontract` | 是否入职合同 | `char` | 1 | 是 | 0：否,1：是 |
| 6 | `remindaheaddate` | 提前提醒天数 | `integer` | - | 是 | 提前提醒天数 |
| 7 | `remindman` | 提醒人 | `varchar2` | 1000 | 是 | 提醒人 |
| 8 | `subcompanyid` | 合同模板所属分部id | `integer` | - | 是 | 合同模板所属分部id |

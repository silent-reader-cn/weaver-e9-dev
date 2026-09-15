# 泛微OA 数据表: `hrmcontract`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcontract`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `contractname` | 合同名称 | `varchar2` | 1000 | 是 | 合同名称 |
| 3 | `contractman` | 合同人员 | `integer` | - | 是 | 合同人员 |
| 4 | `contracttypeid` | 合同种类id | `integer` | - | 是 | 合同种类id |
| 5 | `contractstartdate` | 合同开始日期 | `char` | 10 | 是 | 合同开始日期 |
| 6 | `contractenddate` | 合同结束日期 | `char` | 10 | 是 | 合同结束日期 |
| 7 | `contractdocid` | 合同相关文档 | `integer` | - | 是 | 合同相关文档 |
| 8 | `proenddate` | 试用结束日期 | `char` | 10 | 是 | 试用结束日期 |

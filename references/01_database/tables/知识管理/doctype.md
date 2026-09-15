# 泛微OA 数据表: `doctype`

- **所属模块**: `知识管理`
- **数据库表名**: `doctype`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `hrmresclause` | 选择人力资源的where子句 | `varchar2` | 1000 | 是 | - |
| 2 | `hrmreslabel` | 选择人力资源项的标题 | `varchar2` | 1000 | 是 | - |
| 3 | `hascrm` | 是否使用crm | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 4 | `crmclause` | 选择crm的where子句 | `varchar2` | 1000 | 是 | - |
| 5 | `crmlabel` | 选择crm项的标题 | `varchar2` | 1000 | 是 | - |
| 6 | `hasproject` | 是否使用项目 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 7 | `projectclause` | 选择项目的where子句 | `varchar2` | 1000 | 是 | - |
| 8 | `projectlabel` | 选择项目项的标题 | `varchar2` | 1000 | 是 | - |
| 9 | `hasfinance` | 是否使用财务-交易 0 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 10 | `financeclause` | 选择财务-交易的where子句 | `varchar2` | 1000 | 是 | - |
| 11 | `financelabel` | 选择财务-交易项的标题 | `varchar2` | 1000 | 是 | - |
| 12 | `hasrefence1` | 是否使用财务-参考1 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 13 | `hasrefence2` | 是否使用财务-参考2 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 14 | `id` | 文档种类id | `integer` | - | 否 | - |
| 15 | `typename` | 种类描述 | `varchar2` | 1000 | 是 | - |
| 16 | `isactive` | 是否活跃 | `char` | 1 | 是 | 0:否，1:是 |
| 17 | `hasaccessory` | 是否有附件 | `char` | 1 | 是 | 0:否，1:是 |
| 18 | `accessorynum` | 附件数量 | `integer` | - | 是 | - |
| 19 | `hasitems` | 是否使用物品 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 20 | `itemclause` | 选择物品的where子句 | `varchar2` | 1000 | 是 | - |
| 21 | `itemlabel` | 选择物品项的标题 | `varchar2` | 1000 | 是 | - |
| 22 | `hasitemmaincategory` | 是否使用物品种类 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |
| 23 | `itemmaincategorylabel` | 选择物品种类项的标题 | `varchar2` | 1000 | 是 | - |
| 24 | `hashrmres` | 是否使用人力资源 | `char` | 1 | 是 | 0:否，1:可选，2:必须 |

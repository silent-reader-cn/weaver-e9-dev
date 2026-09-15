# 泛微OA 数据表: `hrmcontracttemplet`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcontracttemplet`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `templetname` | 合同模板名称 | `varchar2` | 1000 | 是 | 合同模板名称 |
| 3 | `templetdocid` | 合同模板文档id | `integer` | - | 是 | 合同模板文档id |
| 4 | `subcompanyid` | 合同模板所属分部id | `integer` | - | 是 | 合同模板所属分部id |

# 泛微OA 数据表: `hrmsalaryresourcepay`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalaryresourcepay`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemid` | 薪酬设置项id | `integer` | - | 是 | 对应hrmsalaryitem主键id |
| 3 | `resourceid` | 人员id | `integer` | - | 是 | 对应hrmresource表主键id |
| 4 | `resourcepay` | 金额 | `number` | (10,2) | 是 | 金额 |
| 5 | `isbatch` | 是否为批处理 | `char` | 1 | 是 | 0、表示个人基准设置 ，1、为批处理设置，从hrmsalarypersonality中显示批处理结果 |

# 泛微OA 数据表: `hrmsalaryrank`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalaryrank`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `itemid` | 薪酬id | `integer` | - | 是 | 薪酬id |
| 3 | `jobid` | 岗位id | `integer` | - | 是 | 岗位id |
| 4 | `joblevelfrom` | 职级开始 | `integer` | - | 是 | 职级开始 |
| 5 | `joblevelto` | 职级结束 | `integer` | - | 是 | 职级结束 |
| 6 | `amount` | 金额 | `number` | (10,2) | 是 | 金额 |
| 7 | `jobactivityid` | 职务id | `integer` | - | 是 | 职务id |

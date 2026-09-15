# 泛微OA 数据表: `hrmsalarycreateinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarycreateinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `currentdate` | 当前时间 | `char` | 7 | 是 | 当前时间 |
| 3 | `salarybegindate` | 工资生成开始时间 | `char` | 10 | 是 | 工资生成开始时间 |
| 4 | `salaryenddate` | 工资生成结束时间 | `char` | 10 | 是 | 工资生成结束时间 |
| 5 | `payid` | 工资id | `varchar2` | 48 | 是 | 工资id |
| 6 | `plandate` | 计划日期 | `char` | 10 | 是 | 计划日期 |
| 7 | `hasdone` | 是否处理 | `char` | 1 | 是 | 0未执行 |

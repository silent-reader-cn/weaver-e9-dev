# 泛微OA 数据表: `hrmperformancereportlog`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmperformancereportlog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `reportname` | 报告名字 | `varchar2` | 800 | 是 | 报告名字 |
| 3 | `reportlog` | 报告备注 | `varchar2` | 4000 | 是 | 报告备注 |
| 4 | `cycle` | 考核周期 | `char` | 1 | 是 | 考核周期 |
| 5 | `reportdate` | 报告日期 | `varchar2` | 400 | 是 | 报告日期 |
| 6 | `reporttype` | 报告所属类型 | `char` | 1 | 是 | 报告所属类型 |
| 7 | `objid` | 对象id | `integer` | - | 是 | 对象id |

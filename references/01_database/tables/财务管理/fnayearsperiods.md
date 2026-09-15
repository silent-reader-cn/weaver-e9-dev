# 泛微OA 数据表: `fnayearsperiods`

- **所属模块**: `财务管理`
- **数据库表名**: `fnayearsperiods`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `fnayear` | 年度 | `char` | 4 | 是 | - |
| 3 | `startdate` | 开始日期 | `char` | 10 | 是 | - |
| 4 | `enddate` | 结束日期 | `char` | 10 | 是 | - |
| 5 | `budgetid` | 作废 | `integer` | - | 是 | - |
| 6 | `status` | 状态 | `integer` | - | 是 | 0： 未生效；1 ：生效；-1： 关闭；默认为0 |

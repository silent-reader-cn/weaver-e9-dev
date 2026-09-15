# 泛微OA 数据表: `docmark`

- **所属模块**: `知识管理`
- **数据库表名**: `docmark`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `integer` | - | 是 | - |
| 3 | `markhrmtype` | 打分人用户类型 | `integer` | - | 是 | - |
| 4 | `markhrmid` | 打分人用户id | `integer` | - | 是 | - |
| 5 | `mark` | 分数 | `integer` | - | 是 | - |
| 6 | `remark` | 备注 | `varchar2` | 1000 | 是 | - |
| 7 | `markdate` | 打分日期 | `char` | 10 | 是 | - |

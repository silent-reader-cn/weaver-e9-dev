# 泛微OA 数据表: `fullsearch_searchset`

- **所属模块**: `微搜`
- **数据库表名**: `fullsearch_searchset`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | &nbsp; |
| 2 | `userid` | 用户id | `integer` | - | 是 | &nbsp; |
| 3 | `searchfield` | 查询字段 | `integer` | - | 是 | 0 全文 1标题 |
| 4 | `sortfield` | 排序方式 | `integer` | - | 是 | 0 相关度 1时间 |

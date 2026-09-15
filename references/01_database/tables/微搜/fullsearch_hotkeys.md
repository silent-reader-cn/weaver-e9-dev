# 泛微OA 数据表: `fullsearch_hotkeys`

- **所属模块**: `微搜`
- **数据库表名**: `fullsearch_hotkeys`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 是 | &nbsp; |
| 2 | `userid` | 用户id | `integer` | - | 是 | &nbsp; |
| 3 | `hotkey` | 搜索关键字 | `varchar2` | 1000 | 是 | &nbsp; |
| 4 | `intcount` | 统计次数 | `integer` | - | 是 | &nbsp; |
| 5 | `updatetime` | 最近更新时间 | `number` | (19,0) | 是 | &nbsp; |

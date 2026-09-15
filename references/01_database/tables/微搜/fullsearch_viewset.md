# 泛微OA 数据表: `fullsearch_viewset`

- **所属模块**: `微搜`
- **数据库表名**: `fullsearch_viewset`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | &nbsp; |
| 2 | `userid` | 用户id | `integer` | - | 是 | &nbsp; |
| 3 | `contenttype` | 类型 | `varchar2` | 160 | 是 | all 通用. 其他各个搜索模块配置 |
| 4 | `canshowfield` | 可显示字段 | `varchar2` | 1000 | 是 | 废弃.不用 |
| 5 | `showfield` | 显示字段 | `varchar2` | 1000 | 是 | 废弃.不用 |
| 6 | `bgimg` | 背景 | `integer` | - | 是 | &nbsp; |
| 7 | `numperpage` | 每页显示条数 | `integer` | - | 是 | 每页条数 |
| 8 | `showcontenttypes` | 可搜索显示项 | `varchar2` | 1000 | 是 | 废弃 |

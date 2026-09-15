# 泛微OA 数据表: `docprivateseccategory`

- **所属模块**: `知识管理`
- **数据库表名**: `docprivateseccategory`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 目录id | `integer` | - | 否 | - |
| 2 | `categoryname` | 目录名称 | `varchar2` | 1000 | 是 | - |
| 3 | `ecology_pinyin_search` | 缩写 | `varchar2` | 1000 | 是 | - |
| 4 | `parentid` | 父目录 | `integer` | - | 是 | - |
| 5 | `userid` | 用户id | `integer` | - | 是 | - |
| 6 | `usertype` | 用户类型 | `integer` | - | 是 | - |

# 泛微OA 数据表: `govern_column`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_column`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `name` | 栏目名称 | `varchar2` | 256 | 是 | - |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `isuse` | 是否启用 | `integer` | - | 是 | - |
| 5 | `linkurl` | 链接 | `varchar2` | 1000 | 是 | - |
| 6 | `type` | 栏目类型 | `integer` | - | 是 | - |
| 7 | `systype` | 是否系统默认栏目 | `integer` | - | 是 | - |
| 8 | `showorder` | 显示顺序 | `float` | 22 | 是 | - |

# 泛微OA 数据表: `fnatmptblogcolinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnatmptblogcolinfo`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `guid1` | 主表唯一标识 | `varchar2` | 250 | 是 | fnatmptblog表guid1 |
| 3 | `coldbname` | 数据库列名 | `varchar2` | 400 | 是 | - |
| 4 | `coltype` | 列名称值类型名称 | `varchar2` | 2000 | 是 | - |
| 5 | `colvalue` | 列名称值 | `varchar2` | 250 | 是 | 列名称值（字符串型） 内容与colvalueint一致 |
| 6 | `colvalueint` | 列名称值 | `integer` | - | 是 | 列名称值（数值型） 当colvalue值是数值型时，内容与colvalue一致（方便链表查询用） |

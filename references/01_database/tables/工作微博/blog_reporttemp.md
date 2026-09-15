# 泛微OA 数据表: `blog_reporttemp`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_reporttemp`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `userid` | 人员id | `integer` | - | 是 | - |
| 3 | `tempname` | 模板名称 | `varchar2` | 400 | 是 | - |
| 4 | `isdisplay` | 是否显示 | `integer` | - | 是 | - |
| 5 | `isdefault` | 是否默认 | `integer` | - | 是 | - |
| 6 | `sort` | 排序 | `integer` | - | 是 | - |

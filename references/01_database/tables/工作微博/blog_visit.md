# 泛微OA 数据表: `blog_visit`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_visit`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `userid` | 人员id | `integer` | - | 是 | - |
| 3 | `blogid` | 访问微博人员id | `integer` | - | 是 | - |
| 4 | `visitdate` | 访问日期 | `varchar2` | 80 | 是 | - |
| 5 | `visittime` | 访问时间 | `varchar2` | 80 | 是 | - |

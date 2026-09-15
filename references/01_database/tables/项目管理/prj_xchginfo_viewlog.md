# 泛微OA 数据表: `prj_xchginfo_viewlog`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_xchginfo_viewlog`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `xchg_id` | 相关交流id | `integer` | - | 是 | 相关交流id |
| 3 | `sortid` | 对象id | `integer` | - | 是 | 对象id |
| 4 | `type_n` | 类型 | `char` | 2 | 是 | 类型 |
| 5 | `viewer_id` | 访问者id | `integer` | - | 是 | 访问者id |
| 6 | `view_date` | 访问日期 | `varchar2` | 400 | 是 | 访问日期 |
| 7 | `view_time` | 访问时间 | `varchar2` | 400 | 是 | 访问时间 |

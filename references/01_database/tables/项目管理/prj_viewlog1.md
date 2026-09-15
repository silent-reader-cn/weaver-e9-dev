# 泛微OA 数据表: `prj_viewlog1`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_viewlog1`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | 否 | 标识列 |
| 2 | `viewer` | 访问者 | `integer` | - | 是 | 访问者 |
| 3 | `viewdate` | 访问日期 | `char` | 10 | 是 | 访问日期 |
| 4 | `viewtime` | 访问时间 | `char` | 8 | 是 | 访问时间 |
| 5 | `ipaddress` | ip地址 | `char` | 15 | 是 | ip地址 |
| 6 | `submitertype` | 提交类型 | `integer` | - | 是 | 提交类型 |

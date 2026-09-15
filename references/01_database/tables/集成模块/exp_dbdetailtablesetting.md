# 泛微OA 数据表: `exp_dbdetailtablesetting`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_dbdetailtablesetting`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `dbsettingid` | 数据库方案id | `integer` | - | 是 | - |
| 3 | `columnname` | 字段名称 | `varchar2` | 1000 | 是 | - |
| 4 | `columntype` | 字段类型 | `varchar2` | 400 | 是 | - |
| 5 | `primarykey` | 是否是主键字段 | `char` | 1 | 是 | - |
| 6 | `isdoce` | 是否为文档字段 | `char` | 1 | 是 | - |
| 7 | `doctype` | 是否为文档类型字段 | `char` | 1 | 是 | - |
| 8 | `mainid` | 是否为保存主表id字段 | `char` | 1 | 是 | - |
| 9 | `filename` | 是否为文件名称保存字段 | `char` | 1 | 是 | - |

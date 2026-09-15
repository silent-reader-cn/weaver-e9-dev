# 泛微OA 数据表: `fnadataset`

- **所属模块**: `财务管理`
- **数据库表名**: `fnadataset`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `dsetname` | 数据集名称 | `char` | 100 | 是 | - |
| 3 | `datasourcename` | 数据源名称 | `char` | 50 | 是 | - |
| 4 | `dsmemo` | 备注 | `varchar2` | 4000 | 是 | - |
| 5 | `dsettype` | 数据集类型 | `char` | 1 | 是 | - |
| 6 | `fnavoucherxmlid` | fnavoucherxml.id | `integer` | - | 是 | - |
| 7 | `dsetstr` | 数据集内容字符串 | `clob` | 4000 | 是 | - |

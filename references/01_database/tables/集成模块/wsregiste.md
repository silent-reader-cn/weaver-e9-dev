# 泛微OA 数据表: `wsregiste`

- **所属模块**: `集成模块`
- **数据库表名**: `wsregiste`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 自增长主键 |
| 2 | `customcode` | 自定义编码 | `varchar2` | 800 | 是 | 自定义编码 |
| 3 | `customname` | 自定义名称 | `varchar2` | 800 | 是 | 自定义名称 |
| 4 | `webserviceurl` | webservice地址 | `varchar2` | 2000 | 是 | webservice地址 |

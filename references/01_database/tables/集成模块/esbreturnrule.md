# 泛微OA 数据表: `esbreturnrule`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `setid` | ESB接口主键 | `integer` | - | 是 | ESB接口主键 |
| 3 | `rulename` | 规则名称 | `varchar2` | 2000 | 是 | 规则名称 |
| 4 | `condition` | 规则条件内容 | `varchar2` | 2000 | 是 | 规则条件内容 |
| 5 | `esbid` | ESB服务主键 | `varchar2` | 1000 | 是 | ESB服务主键 |
| 6 | `version` | 版本 | `integer` | - | 是 | 版本 |

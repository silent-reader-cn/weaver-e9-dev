# 泛微OA 数据表: `esbreturnrule`

- **中文名称**: ESB接口配置返回规则
- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnrule`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 是 | - | - | 主键ID |
| 2 | `setid` | ESB接口主键 | `integer` | - | 是 | 是 | 否 | esbformactionset.id | - | ESB接口主键 |
| 3 | `rulename` | 规则名称 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 规则名称 |
| 4 | `condition` | 规则条件内容 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 规则条件内容 |
| 5 | `esbid` | ESB服务主键 | `varchar2` | 1000 | 是 | 是 | 否 | esb_publish.publishId | - | ESB服务主键 |
| 6 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | - | 版本 |

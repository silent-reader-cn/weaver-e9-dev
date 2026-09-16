# 泛微OA 数据表: `esbmethodparamvalue`

- **中文名称**: ESB接口配置参数表
- **所属模块**: `集成模块`
- **数据库表名**: `esbmethodparamvalue`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 否 | 是 | - | - | 主键ID |
| 2 | `actionid` | ESB接口配置主键 | `integer` | - | 是 | 是 | 否 | esbformactionset.id | - | ESB接口配置主键 |
| 3 | `paramname` | 参数名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 参数名 |
| 4 | `showname` | 参数显示名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 参数显示名 |
| 5 | `paramtype` | 参数类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 参数类型 |
| 6 | `isarray` | 参数是否数组 | `char` | 1 | 是 | 否 | 否 | - | - | 参数是否数组 |
| 7 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 字段名 |
| 8 | `fieldtype` | 字段类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 字段类型 |
| 9 | `transtype` | 转换类型 | `integer` | - | 是 | 否 | 否 | - | - | 转换类型 |
| 10 | `extrainfo` | 附加信息 | `clob` | 4000 | 是 | 否 | 否 | - | - | 附加信息 |
| 11 | `showorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | 显示顺序 |
| 12 | `formid` | 流程表单ID | `integer` | - | 是 | 是 | 否 | - | - | 流程表单ID |
| 13 | `version` | 版本 | `integer` | - | 是 | 否 | 否 | - | - | 版本 |

# 泛微OA 数据表: `esbreturnassign`

- **所属模块**: `集成模块`
- **数据库表名**: `esbreturnassign`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | 主键ID |
| 2 | `actionid` | ESB接口ID | `varchar2` | 1000 | 是 | ESB接口ID |
| 3 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | 字段名 |
| 4 | `fieldtype` | 字段类型 | `varchar2` | 1000 | 是 | 字段类型 |
| 5 | `operation` | 操作符 | `varchar2` | 1000 | 是 | 操作符 |
| 6 | `returnparam` | 返回参数 | `varchar2` | 1000 | 是 | 返回参数 |
| 7 | `transtype` | 转换类型 | `integer` | - | 是 | 转换类型 |
| 8 | `extrainfo` | 转换值 | `varchar2` | 1000 | 是 | 转换值 |
| 9 | `showorder` | 显示顺序 | `integer` | - | 是 | 显示顺序 |
| 10 | `formid` | 表单ID | `integer` | - | 是 | 表单ID |
| 11 | `esbid` | ESB服务ID | `varchar2` | 1000 | 是 | ESB服务ID |
| 12 | `fieldshowname` | 字段显示名 | `varchar2` | 1000 | 是 | 字段显示名 |
| 13 | `version` | 版本 | `integer` | - | 是 | 版本 |

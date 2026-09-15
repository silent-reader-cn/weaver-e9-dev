# 泛微OA 数据表: `exp_dbdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_dbdetail`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `name` | 方案名称 | `varchar2` | 1000 | 是 | - |
| 3 | `resoure` | 数据源名称 | `varchar2` | 800 | 是 | - |
| 4 | `maintable` | 主表名称 | `varchar2` | 800 | 是 | - |
| 5 | `detailtable` | 明细表名称 | `varchar2` | 800 | 是 | - |
| 6 | `createdate` | 方案创建日期 | `varchar2` | 160 | 是 | - |
| 7 | `creator` | 方案创建人 | `integer` | - | 是 | - |

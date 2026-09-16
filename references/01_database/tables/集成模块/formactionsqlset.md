# 泛微OA 数据表: `formactionsqlset`

- **中文名称**: DML接口自定义sql设置表
- **所属模块**: `集成模块`
- **数据库表名**: `formactionsqlset`
- **主键**: `id`
- **字段数**: `18`

> 说明：无

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 是 | - | - | 无 |
| 2 | `actionid` | 接口id | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 3 | `actiontable` | 表名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 无 |
| 4 | `dmlformid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 5 | `dmlformname` | 表单名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 无 |
| 6 | `dmlisdetail` | 明细表 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 7 | `dmltablename` | 表名 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 无 |
| 8 | `dmltablebyname` | 未知字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 无 |
| 9 | `dmlsql` | 自定义sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 10 | `dmlfieldtypes` | 字段类型 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 11 | `dmlfieldnames` | 字段名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 12 | `dmlothersql` | 其他sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 13 | `dmlotherfieldtypes` | 其他字段类型 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 14 | `dmlotherfieldnames` | 其他字段名 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 15 | `dmlcuswhere` | 自定义条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 16 | `dmlmainsqltype` | sql类型 | `integer` | - | 是 | 否 | 否 | - | - | 无 |
| 17 | `dmlcussql` | 自定义sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 无 |
| 18 | `olddmlactionsqlsetid` | 未知字段 | `integer` | - | 是 | 否 | 否 | - | - | 无 |

# 泛微OA 数据表: `ldapsetdetail`

- **中文名称**: 分部对应设置表
- **所属模块**: `集成模块`
- **数据库表名**: `ldapsetdetail`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `subcompanycode` | 分部编码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 3 | `subcomusertodepcode` | subcomusertodepcode | `varchar2` | 800 | 是 | 否 | 否 | - | - | 废弃 |
| 4 | `subcompanydomain` | 同步域 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 对应ad里ou |
| 5 | `subcompanyid` | 分部id | `varchar2` | 400 | 是 | 否 | 否 | - | - | 分部id |

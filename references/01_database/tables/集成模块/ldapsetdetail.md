# 泛微OA 数据表: `ldapsetdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `ldapsetdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `subcompanycode` | 分部编码 | `varchar2` | 800 | 是 | - |
| 3 | `subcomusertodepcode` | subcomusertodepcode | `varchar2` | 800 | 是 | 废弃 |
| 4 | `subcompanydomain` | 同步域 | `varchar2` | 1000 | 是 | 对应ad里ou |
| 5 | `subcompanyid` | 分部id | `varchar2` | 400 | 是 | 分部id |

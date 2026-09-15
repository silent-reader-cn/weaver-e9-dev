# 泛微OA 数据表: `ldap_formart`

- **所属模块**: `集成模块`
- **数据库表名**: `ldap_formart`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `formartid` | 标识 | `varchar2` | 100 | 否 | 标识 |
| 2 | `formartclass` | 插件类名称 | `varchar2` | 800 | 是 | 插件类名称 |
| 3 | `formartparams` | 调用参数 | `varchar2` | 1000 | 是 | 调用参数 |
| 4 | `formartname` | 插件显示名称 | `varchar2` | 800 | 是 | 插件显示名称 |
| 5 | `formarttype` | 插件类型 | `char` | 1 | 是 | 1:LDAP转换插件，2:OA转换插件 |
| 6 | `formartlevel` | 插件级别 | `char` | 1 | 是 | 1：系统级别，2：用户级别 |

# 泛微OA 数据表: `fnavoucherobjinfo`

- **中文名称**: 财务凭证配置项信息表
- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherobjinfo`
- **主键**: `id`
- **字段数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fnavoucherinittypestr` | 凭证初始化类型字符串 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 3 | `displayorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `fieldvaluetype1` | 字段类型1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldvaluetype2` | 字段类型2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `fieldvalue` | 字段值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `fielddbtbname` | 字段数据库表名 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 9 | `detailtable` | 凭证分录配置项 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 10 | `fielddbname` | 字段数据库列名 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 11 | `fielddbtype` | 字段数据库类型 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `memo` | 备注 | `varchar2` | 3000 | 是 | 否 | 否 | - | - | - |
| 13 | `isshow` | 是否显示（配置界面） | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `islockdeftype` | 是否锁定类型（配置界面） | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `isnull` | 是否允许不填（配置界面） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `inputisselect` | 字段是否是选择框（配置界面） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `selectvalues` | 字段选择项值（配置界面） | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `selectnames` | 字段选择项键（配置界面） | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

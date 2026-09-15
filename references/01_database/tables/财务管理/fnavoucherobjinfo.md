# 泛微OA 数据表: `fnavoucherobjinfo`

- **所属模块**: `财务管理`
- **数据库表名**: `fnavoucherobjinfo`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `fnavoucherinittypestr` | 凭证初始化类型字符串 | `varchar2` | 200 | 是 | - |
| 3 | `displayorder` | 显示顺序 | `integer` | - | 是 | - |
| 4 | `fieldname` | 字段名 | `varchar2` | 1000 | 是 | - |
| 5 | `fieldvaluetype1` | 字段类型1 | `varchar2` | 1000 | 是 | - |
| 6 | `fieldvaluetype2` | 字段类型2 | `varchar2` | 1000 | 是 | - |
| 7 | `fieldvalue` | 字段值 | `varchar2` | 1000 | 是 | - |
| 8 | `fielddbtbname` | 字段数据库表名 | `varchar2` | 200 | 是 | - |
| 9 | `detailtable` | 凭证分录配置项 | `varchar2` | 200 | 是 | - |
| 10 | `fielddbname` | 字段数据库列名 | `varchar2` | 200 | 是 | - |
| 11 | `fielddbtype` | 字段数据库类型 | `varchar2` | 1000 | 是 | - |
| 12 | `memo` | 备注 | `varchar2` | 3000 | 是 | - |
| 13 | `isshow` | 是否显示（配置界面） | `varchar2` | 1000 | 是 | - |
| 14 | `islockdeftype` | 是否锁定类型（配置界面） | `varchar2` | 1000 | 是 | - |
| 15 | `isnull` | 是否允许不填（配置界面） | `integer` | - | 是 | - |
| 16 | `inputisselect` | 字段是否是选择框（配置界面） | `integer` | - | 是 | - |
| 17 | `selectvalues` | 字段选择项值（配置界面） | `varchar2` | 1000 | 是 | - |
| 18 | `selectnames` | 字段选择项键（配置界面） | `varchar2` | 1000 | 是 | - |

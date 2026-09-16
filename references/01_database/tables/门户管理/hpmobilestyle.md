# 泛微OA 数据表: `hpmobilestyle`

- **中文名称**: 移动门户菜单样式信息表
- **所属模块**: `门户管理`
- **数据库表名**: `hpmobilestyle`
- **主键**: `styleid`
- **字段数**: `8`

> 说明：移动门户样式信息表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `styleid` | 样式id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 2 | `menustylename` | 菜单样式名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `menustyletype` | 菜单样式类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 4 | `menustylecreater` | 菜单样式创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `menustylemodifyid` | 菜单样式更新人 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 6 | `menustylelastdate` | 菜单样式最后修改日期 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 7 | `menustylelasttime` | 菜单样式最后修改时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 8 | `menustylecite` | menustylecite | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |

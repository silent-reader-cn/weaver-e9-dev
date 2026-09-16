# 泛微OA 数据表: `social_imsysbroadcast`

- **中文名称**: emessage广播权限表
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_imsysbroadcast`
- **主键**: `id`
- **字段数**: `8`

> 说明：用来设定发起广播的权限

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | id。不同数据库id策略不同 |
| 2 | `permissiontype` | 权限种类 | `integer` | - | 否 | 否 | 否 | - | - | 可填cookie |
| 3 | `contents` | 权限种类下的人员/部门/分部/角色的ID | `integer` | - | 否 | 否 | 否 | - | - | 与permissiontype一起确定选定范围 |
| 4 | `seclevel` | 安全级别下限 | `integer` | - | 否 | 否 | 否 | - | 0 | 安全级别下限 |
| 5 | `seclevelmax` | 安全级别上限 | `integer` | - | 否 | 否 | 否 | - | 100 | 安全级别上限 |
| 6 | `jobtitleid` | Deprecated废弃字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | Deprecated废弃字段 |
| 7 | `joblevel` | Deprecated废弃字段 | `integer` | - | 是 | 否 | 否 | - | 0 | Deprecated废弃字段 |
| 8 | `scopeid` | Deprecated废弃字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | Deprecated废弃字段 |

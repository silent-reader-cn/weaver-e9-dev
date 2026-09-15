# 泛微OA 数据表: `social_imsysbroadcast`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imsysbroadcast`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | id。不同数据库id策略不同 |
| 2 | `permissiontype` | 权限种类 | `integer` | - | 否 | 可填cookie |
| 3 | `contents` | 权限种类下的人员/部门/分部/角色的ID | `integer` | - | 否 | 与permissiontype一起确定选定范围 |
| 4 | `seclevel` | 安全级别下限 | `integer` | - | 否 | 安全级别下限 |
| 5 | `seclevelmax` | 安全级别上限 | `integer` | - | 否 | 安全级别上限 |
| 6 | `jobtitleid` | Deprecated废弃字段 | `varchar2` | 1000 | 是 | Deprecated废弃字段 |
| 7 | `joblevel` | Deprecated废弃字段 | `integer` | - | 是 | Deprecated废弃字段 |
| 8 | `scopeid` | Deprecated废弃字段 | `varchar2` | 800 | 是 | Deprecated废弃字段 |

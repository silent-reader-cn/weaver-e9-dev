# 泛微OA 数据表: `mode_boardshareinfo`

- **中文名称**: 看板权限表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_boardshareinfo`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `boardid` | 看板id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `sharetype` | 权限类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `relatedid` | 关系id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `rolelevel` | 权限级别（角色） | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `showlevel` | 安全级别下限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `hrmcompanyvirtualtype` | 虚拟公司类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `jobleveltext` | 岗位级别指定对象id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

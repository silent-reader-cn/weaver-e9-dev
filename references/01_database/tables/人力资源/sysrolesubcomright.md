# 泛微OA 数据表: `sysrolesubcomright`

- **中文名称**: 系统角色分部权限表
- **所属模块**: `人力资源`
- **数据库表名**: `sysrolesubcomright`
- **主键**: `id,roleid,subcompanyid`
- **字段数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `roleid` | 角色id | `integer` | - | 否 | 否 | 否 | - | - | 角色id |
| 3 | `subcompanyid` | 分部id | `integer` | - | 否 | 否 | 否 | - | - | 分部id |
| 4 | `rightlevel` | 操作级别 | `integer` | - | 是 | 否 | 否 | - | - | -1:禁止<br>0:只读<br>1:编辑<br>2:完全控制 |

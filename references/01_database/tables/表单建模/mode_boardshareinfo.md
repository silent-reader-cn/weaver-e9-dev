# 泛微OA 数据表: `mode_boardshareinfo`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_boardshareinfo`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `boardid` | 看板id | `integer` | - | 是 | - |
| 3 | `sharetype` | 权限类型 | `integer` | - | 是 | - |
| 4 | `relatedid` | 关系id | `integer` | - | 是 | - |
| 5 | `rolelevel` | 权限级别（角色） | `integer` | - | 是 | - |
| 6 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 7 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 8 | `joblevel` | 岗位级别 | `integer` | - | 是 | - |
| 9 | `hrmcompanyvirtualtype` | 虚拟公司类型 | `integer` | - | 是 | - |
| 10 | `jobleveltext` | 岗位级别指定对象id | `varchar2` | 4000 | 是 | - |

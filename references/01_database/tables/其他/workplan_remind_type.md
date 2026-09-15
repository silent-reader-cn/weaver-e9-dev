# 泛微OA 数据表: `workplan_remind_type`

- **所属模块**: `其他`
- **数据库表名**: `workplan_remind_type`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 是 | ID |
| 2 | `name` | 提醒方式中文名 | `varchar2` | 800 | 是 | 提醒方式中文名 |
| 3 | `label` | 提醒方式标签id,支持国际化 | `integer` | - | 是 | 提醒方式标签id,支持国际化 |
| 4 | `hastitle` | 是否有标题 | `char` | 1 | 是 | 是否有标题 |
| 5 | `isuse` | 启用 | `integer` | - | 是 | 1是启用 |
| 6 | `isdefault` | 默认 | `integer` | - | 是 | 1是默认 |
| 7 | `clazzname` | 提醒方式的实现类全名 | `varchar2` | 1000 | 是 | 提醒方式的实现类全名 |
| 8 | `settingurl` | 提醒方式设置路径 | `varchar2` | 2000 | 是 | 提醒方式设置路径 |
| 9 | `sysrights` | 提醒方式设置权限 | `varchar2` | 1000 | 是 | 提醒方式设置权限 |

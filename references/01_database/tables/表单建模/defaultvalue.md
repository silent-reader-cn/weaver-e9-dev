# 泛微OA 数据表: `defaultvalue`

- **中文名称**: 默认值基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `defaultvalue`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 4 | `customervalue` | 默认值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 默认值，一个字段只能设置一个默认值 |
| 5 | `formid` | 表单id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |

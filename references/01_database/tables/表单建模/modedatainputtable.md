# 泛微OA 数据表: `modedatainputtable`

- **中文名称**: 字段联动引用数据库表名
- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputtable`
- **主键**: `id`
- **字段数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `datainputid` | 字段联动主id | `integer` | - | 是 | 否 | 否 | - | - | 对应modedatainputmain表的id |
| 3 | `tablename` | 表名 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 存储数据库表名 |
| 4 | `alias` | 别名 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 5 | `formid` | 表单id | `varchar2` | 800 | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |

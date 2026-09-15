# 泛微OA 数据表: `modedatainputtable`

- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputtable`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `datainputid` | 字段联动主id | `integer` | - | 是 | 对应modedatainputmain表的id |
| 3 | `tablename` | 表名 | `varchar2` | 320 | 是 | 存储数据库表名 |
| 4 | `alias` | 别名 | `varchar2` | 80 | 是 | - |
| 5 | `formid` | 表单id | `varchar2` | 800 | 是 | 对应workflow_bill表的id |

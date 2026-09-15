# 泛微OA 数据表: `modedatainputfield`

- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputfield`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `datainputid` | 字段联动主id | `integer` | - | 是 | 对应modedatainputmain表的id |
| 3 | `tableid` | 字段联动引用数据库表名id | `integer` | - | 是 | 对应modedatainputtable表id |
| 4 | `type` | 设置类型 | `integer` | - | 是 | - |

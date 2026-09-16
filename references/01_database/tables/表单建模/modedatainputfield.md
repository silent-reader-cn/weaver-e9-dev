# 泛微OA 数据表: `modedatainputfield`

- **中文名称**: 字段联动字段信息
- **所属模块**: `表单建模`
- **数据库表名**: `modedatainputfield`
- **主键**: `id`
- **字段数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `datainputid` | 字段联动主id | `integer` | - | 是 | 否 | 否 | - | - | 对应modedatainputmain表的id |
| 3 | `tableid` | 字段联动引用数据库表名id | `integer` | - | 是 | 否 | 否 | - | - | 对应modedatainputtable表id |
| 4 | `type` | 设置类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：:取值设置<br>2：赋值设置 |
| 5 | `dbfieldname` | 引用数据库表字段 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 6 | `pagefieldname` | 赋值字段 | `varchar2` | 320 | 是 | 否 | 否 | - | - | (ield+字段id |
| 7 | `treenodeid` | 树节点id | `varchar2` | 800 | 是 | 否 | 否 | - | - | 树字段联动使用 |
| 8 | `pagefieldindex` | 判读主表还是明细表 | `integer` | - | 是 | 否 | 否 | - | - | 0 主表 1 明细1 2明细2…… |

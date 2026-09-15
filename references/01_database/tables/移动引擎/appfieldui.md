# 泛微OA 数据表: `appfieldui`

- **所属模块**: `移动引擎`
- **数据库表名**: `appfieldui`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | 字段所属表单id, workflow_bill表的id列外键 |
| 3 | `appid` | 应用id | `integer` | - | 是 | 所属应用，mobileappbaseinfo表的id列外键 |
| 4 | `fieldid` | 字段id | `integer` | - | 是 | 字段id， workflow_billfield表id列外键 |
| 5 | `uiparam` | ui参数 | `varchar2` | 1000 | 是 | 无用，已废弃 |
| 6 | `showtype` | 显示类型 | `integer` | - | 是 | 显示类型，0隐藏，1只读，2编辑，3必填 |
| 7 | `formuiid` | 布局id | `integer` | - | 是 | 所属ui布局，appformui表id列的外键 |
| 8 | `comptype` | 组件类型 | `integer` | - | 是 | 无用，已废弃 |
| 9 | `fieldname` | 字段名称 | `varchar2` | 480 | 是 | 字段名称(数据库列名称)，和workflow_billfield的fieldname对应 |

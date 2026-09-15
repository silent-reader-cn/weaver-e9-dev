# 泛微OA 数据表: `appformui对应表`

- **所属模块**: `移动引擎`
- **数据库表名**: `appformui对应表`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `formid` | 表单id | `integer` | - | 是 | 布局对应的表单id，workflow_bill表的id列外键 |
| 3 | `uicontent` | ui内容 | `clob` | 4000 | 是 | 存放ui布局的html代码 |
| 4 | `uitype` | ui类型 | `integer` | - | 是 | ui类型：0新建,1显示,2编辑,3列表 |
| 5 | `appid` | 应用id | `integer` | - | 是 | 所属应用，mobileappbaseinfo表的id列外键 |
| 6 | `uiname` | ui名称 | `varchar2` | 1000 | 是 | ui的中文名称，根据ui类型分别对应表单建模模块下的新建布局名称，编辑布局名称，显示布局名称，查询列表的名称 |
| 7 | `isdelete` | 是否删除 | `integer` | - | 是 | 是否删除，1是，0否 |
| 8 | `uitemplate` | ui模板 | `clob` | 4000 | 是 | 存放ui布局的html代码 |
| 9 | `defaulttitle` | 默认名称 | `varchar2` | 1000 | 是 | 无用，已废弃 |
| 10 | `entityid` | 模块id | `integer` | - | 是 | 模块id，mobileappmodelinfo表id列的外键 |
| 11 | `sourceid` | 查询id | `integer` | - | 是 | 表单建模，查询列表id。mode_customsearch表id列的外键 |
| 12 | `mobiledeviceid` | 设备类型id | `integer` | - | 是 | 设备类型，mobiledevice表id列的外键 |
| 13 | `parentid` | 父id | `integer` | - | 是 | 父id，和本表id列自身关联 |
| 14 | `ishide` | 是否隐藏 | `varchar2` | 80 | 是 | 是否隐藏，1是，null否 |

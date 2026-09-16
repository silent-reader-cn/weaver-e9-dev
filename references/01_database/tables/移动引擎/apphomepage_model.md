# 泛微OA 数据表: `apphomepage_model`

- **中文名称**: 自定义页面关联模块表
- **所属模块**: `移动引擎`
- **数据库表名**: `apphomepage_model`
- **主键**: `apphomepageid`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `isdefault` | 是否默认 | `integer` | - | 是 | 否 | 否 | - | - | 是否默认 |
| 2 | `layoutid` | 布局ID | `integer` | - | 是 | 否 | 否 | - | - | 布局ID |
| 3 | `apphomepageid` | 页面id | `integer` | - | 否 | 否 | 是 | - | - | 所属页面id,apphomepage表id列外键 |
| 4 | `modelid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 表单建模中模块的id(即和modeinfo表的id列对应) |
| 5 | `uitype` | 布局类型 | `varchar2` | 400 | 是 | 否 | 否 | - | - | ui类型：0新建,1显示,2编辑,3列表 |
| 6 | `sourceid` | 查询id | `varchar2` | 400 | 是 | 否 | 否 | - | - | 表单建模，查询列表id。mode_customsearch表id列的外键 |

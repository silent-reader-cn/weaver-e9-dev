# 泛微OA 数据表: `modeattrlinkage`

- **中文名称**: 属性联动基本信息表
- **所属模块**: `表单建模`
- **数据库表名**: `modeattrlinkage`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `isenabled` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表中的id |
| 4 | `type` | 布局类型 | `integer` | - | 是 | 否 | 否 | - | - | 1、新建<br>2、编辑<br>这里的布局类型只有新建布局和编辑布局 |
| 5 | `selectfieldid` | 选择框 | `varchar2` | 160 | 是 | 否 | 否 | - | - | 选择框的字段id，对应workflow_billfield表中的id |
| 6 | `selectfieldvalue` | 选择框值 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 选择框的对应的值 |
| 7 | `changefieldids` | 变更字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 被更改字段属性的字段id，多个字段id用英文逗号隔开 |
| 8 | `viewattr` | 显示属性 | `integer` | - | 是 | 否 | 否 | - | - | 1：编辑<br>2：必填<br>3：只读 |
| 9 | `layoutid` | 布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表中 的id |

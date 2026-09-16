# 泛微OA 数据表: `workflow_browdef_fieldconf`

- **中文名称**: 流程浏览定义字段配置表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browdef_fieldconf`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `number` | (38,0) | 否 | 否 | 否 | - | - | - |
| 2 | `fieldtype` | 字段类型 | `number` | (38,0) | 否 | 否 | 否 | - | - | - |
| 3 | `fieldname` | 字段名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 4 | `namelabel` | 标签名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 5 | `conditionfieldtype` | 条件字段类型 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 6 | `defaultshoworder` | 默认显示顺序 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 7 | `disabled` | 隐藏条件 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `conditione9type` | 条件类型 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 9 | `browsertype` | 浏览框类型 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 10 | `ismultbrowser` | 是否多选 | `char` | 1 | 是 | 否 | 否 | - | - | - |

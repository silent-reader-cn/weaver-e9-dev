# 泛微OA 数据表: `workflow_browdef_fieldconf`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_browdef_fieldconf`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `number` | (38,0) | 否 | - |
| 2 | `fieldtype` | 字段类型 | `number` | (38,0) | 否 | - |
| 3 | `fieldname` | 字段名称 | `varchar2` | 800 | 否 | - |
| 4 | `namelabel` | 标签名称 | `varchar2` | 800 | 否 | - |
| 5 | `conditionfieldtype` | 条件字段类型 | `varchar2` | 800 | 否 | - |
| 6 | `defaultshoworder` | 默认显示顺序 | `varchar2` | 800 | 否 | - |
| 7 | `disabled` | 隐藏条件 | `char` | 1 | 是 | - |
| 8 | `conditione9type` | 条件类型 | `varchar2` | 800 | 是 | - |
| 9 | `browsertype` | 浏览框类型 | `varchar2` | 800 | 是 | - |
| 10 | `ismultbrowser` | 是否多选 | `char` | 1 | 是 | - |

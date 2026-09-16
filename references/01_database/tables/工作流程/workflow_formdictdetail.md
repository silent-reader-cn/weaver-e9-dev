# 泛微OA 数据表: `workflow_formdictdetail`

- **中文名称**: 流程表单字典明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formdictdetail`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `istemplate` | 模板 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `fieldshowtypes` | 下拉框字段显示类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fieldname` | 字段名称 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldhtmltype` | 字段html类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `subcompanyid` | 子公司id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `description` | 描述信息 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 10 | `textheight` | 文本高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `childfieldid` | 子字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `qfws` | 小数位数 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 13 | `textheight_2` | 文档高度_2 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 14 | `imgwidth` | 图片宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `imgheight` | 图片高度 | `integer` | - | 是 | 否 | 否 | - | - | - |

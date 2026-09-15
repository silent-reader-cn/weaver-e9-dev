# 泛微OA 数据表: `workflow_formdictdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formdictdetail`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `istemplate` | 模板 | `char` | 1 | 是 | - |
| 2 | `fieldshowtypes` | 下拉框字段显示类型 | `integer` | - | 是 | - |
| 3 | `id` | ID | `integer` | - | 是 | - |
| 4 | `fieldname` | 字段名称 | `varchar2` | 320 | 是 | - |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | - |
| 6 | `fieldhtmltype` | 字段html类型 | `char` | 1 | 是 | - |
| 7 | `type` | 类型 | `integer` | - | 是 | - |
| 8 | `subcompanyid` | 子公司id | `integer` | - | 是 | - |
| 9 | `description` | 描述信息 | `varchar2` | 800 | 是 | - |
| 10 | `textheight` | 文本高度 | `integer` | - | 是 | - |
| 11 | `childfieldid` | 子字段id | `integer` | - | 是 | - |
| 12 | `qfws` | 小数位数 | `varchar2` | 400 | 是 | - |
| 13 | `textheight_2` | 文档高度_2 | `varchar2` | 400 | 是 | - |
| 14 | `imgwidth` | 图片宽度 | `integer` | - | 是 | - |
| 15 | `imgheight` | 图片高度 | `integer` | - | 是 | - |

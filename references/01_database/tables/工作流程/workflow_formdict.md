# 泛微OA 数据表: `workflow_formdict`

- **中文名称**: 工作流字段字典表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formdict`
- **主键**: `工作流字段字典表`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `fieldshowtypes` | 下拉开显示类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `istemplate` | 是否模板 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 4 | `fieldname` | 字段名称 | `varchar2` | 320 | 是 | 否 | 否 | - | - | 数据库字段名 |
| 5 | `fielddbtype` | 字段数据库类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldhtmltype` | 字段页面类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：单行文本框<br>2：多行文本框<br>3：浏览按钮<br>4：check框<br>5：选择框 |
| 7 | `subcompanyid` | 子公司id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `description` | 描述 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 9 | `textheight` | 文本高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `childfieldid` | 子字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `imgheight` | 图片高度 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 12 | `imgwidth` | 图片宽度 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 13 | `qfws` | 小数点位数 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 14 | `textheight_2` | 文本高度_2 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 15 | `locatetype` | 定位方式 | `char` | 1 | 是 | 否 | 否 | - | - | 1：手动，2自动 |

# 泛微OA 数据表: `govern_field`

- **中文名称**: 督查督办字段设置表
- **所属模块**: `政务督办采编`
- **数据库表名**: `govern_field`
- **主键**: `id`
- **字段数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `defaultvalue` | 默认值 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 2 | `isinherit` | 子任务是否继承 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `name` | 字段显示名 | `varchar2` | 255 | 是 | 否 | 否 | - | - | - |
| 4 | `issystem` | 是否系统字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `textheight` | 多行文本高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `dsporder` | 显示顺序 | `number` | (15,2) | 是 | 否 | 否 | - | - | - |
| 7 | `fieldlabel` | 标签 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `showinasplit` | 分解是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `showinadd` | 新建是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `isshowdetail` | 明细是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `isreserved` | 是否预留字段 | `integer` | - | 是 | 否 | 否 | - | - | 是否为系统预留字段 无需在设置页面体现这个字段（用户标记一些不可编辑的自带字段 比如：类型、状态、tasktype） |
| 12 | `isexcelimport` | 是否excel导入 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 14 | `fieldname` | 字段名 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 15 | `categoryid` | 类型id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `source` | 应用范围 | `integer` | - | 是 | 否 | 否 | - | - | 督办事项、督办任务、汇报、分解、催办 |
| 17 | `fieldhtmltype` | 字段类型 | `integer` | - | 是 | 否 | 否 | - | - | 1单行、2多行、3浏览框、5选择框等 参考workflow_billfield |
| 18 | `fieldtype` | 字段类型 | `varchar2` | 100 | 是 | 否 | 否 | - | - | 单文本、整数 参考workflow_billfield |
| 19 | `fielddbtype` | 数据库字段类型 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 20 | `isrequired` | 是否必填 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `isexcelout` | 是否excel导出 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `isshow` | 是否显示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `isshowlist` | 是否列表展示 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `issearch` | 是否列表查询条件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `isused` | 是否生效 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `triggerfield` | 触发字段 | `integer` | - | 是 | 否 | 否 | - | - | - |

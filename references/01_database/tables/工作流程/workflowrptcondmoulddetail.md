# 泛微OA 数据表: `workflowrptcondmoulddetail`

- **中文名称**: 工作流报表条件模板明细表
- **所属模块**: `工作流程`
- **数据库表名**: `workflowrptcondmoulddetail`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `mouldid` | 模板id | `integer` | - | 是 | 否 | 否 | - | - | workflowrptcondmould表的id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 其中 -1：请求说明，-2：紧急程度，-3：工作流程状态 |
| 4 | `ismain` | 是否主字段 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是主字段，0：不是主字段，而是明细字段 |
| 5 | `isshow` | 是否显示 | `char` | 1 | 是 | 否 | 否 | - | - | 查询出来的报表中是否显示该列，1：显示，0：不显示 |
| 6 | `ischeckcond` | 是否检查报表条件 | `char` | 1 | 是 | 否 | 否 | - | - | 1：检查，0：不检查 |
| 7 | `colname` | 列名 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 8 | `htmltype` | 字段页面类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：单行文本框，2：多行文本框，3：浏览按钮，4：check框，5：选择框 |
| 9 | `type` | 字段详细类型 | `integer` | - | 是 | 否 | 否 | - | - | 与工作流单据字段表（workflow_billfield）的type字段含义一致。 |
| 10 | `optionfirst` | 第一个选项 | `char` | 1 | 是 | 否 | 否 | - | - | 具体意义与htmltype、type相关 |
| 11 | `valuefirst` | 第一个选项的值 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 12 | `namefirst` | 第一个选项的显示名称 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 13 | `optionsecond` | 第二个选项 | `char` | 1 | 是 | 否 | 否 | - | - | 具体意义与htmltype、type相关 |
| 14 | `valuesecond` | 第二个选项的值 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |

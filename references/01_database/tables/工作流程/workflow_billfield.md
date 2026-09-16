# 泛微OA 数据表: `workflow_billfield`

- **中文名称**: 工作流单据字段表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_billfield`
- **主键**: `id`
- **字段数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `fieldshowtypes` | 显示类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `billid` | 单据id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `fieldname` | 数据库表字段名称 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 5 | `fieldlabel` | 字段显示名称 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `fielddbtype` | 单据字段数据库类型 | `varchar2` | 320 | 是 | 否 | 否 | - | - | - |
| 7 | `fieldhtmltype` | 单据字段页面类型 | `char` | 1 | 是 | 否 | 否 | - | - | 1：单行文本框<br>2：多行文本框<br>3：浏览按钮<br>4：check框<br>5：选择框 |
| 8 | `viewtype` | 主表字段还是从表字段 | `integer` | - | 是 | 否 | 否 | - | 0 | 0：主表<br>1：从表 |
| 9 | `detailtable` | 明细表 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 10 | `fromuser` | 用户表单 | `char` | 1 | 是 | 否 | 否 | - | 1 | - |
| 11 | `textheight` | 文本高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `dsporder` | 显示顺序 | `number` | (15,2) | 是 | 否 | 否 | - | - | - |
| 13 | `childfieldid` | 子字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `imgheight` | 图片高度 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 15 | `imgwidth` | 图片宽度 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 16 | `places` | 位置 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `qfws` | 小数位数 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 18 | `textheight_2` | 文本高度_2 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 19 | `selectitem` | 选择条目 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `linkfield` | 连接字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 21 | `selectitemtype` | 公共选择框 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `pubchoiceid` | 公共选择框ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `pubchilchoiceid` | 公共选择框子项ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `statelev` | 选择框级数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `locatetype` | 定位类型 | `char` | 1 | 是 | 否 | 否 | - | - | 2：自动、1：手动 |

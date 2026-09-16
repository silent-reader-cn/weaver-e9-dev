# 泛微OA 数据表: `mode_exportcustomstyle`

- **中文名称**: 查询列表自定义导出样式
- **所属模块**: `表单建模`
- **数据库表名**: `mode_exportcustomstyle`
- **主键**: `customid`
- **字段数**: `17`

> 说明：查询列表自定义导出样式说明表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `customid` | 查询列表id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `headerbg` | 表头背景色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 3 | `headerfontcolor` | 表头字体颜色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 4 | `headerfont` | 表头字体 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 5 | `headerfontsize` | 表头字体大小 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `headertextalign` | 表头对齐方式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `contentfontcolor` | 内容字体颜色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `contentdoublerowbg` | 偶数行内容背景色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 9 | `contentsinglerowbg` | 奇数行内容背景色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 10 | `contentfont` | 内容字体 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 11 | `contentfontsize` | 内容字体大小 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `contenttextalgin` | 内容对齐方式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `gridlinewidth` | 网格线宽 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `gridlinecolor` | 网格线条颜色 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 15 | `lastoperator` | 操作者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `operatedate` | 操作日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 17 | `operatetime` | 操作时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |

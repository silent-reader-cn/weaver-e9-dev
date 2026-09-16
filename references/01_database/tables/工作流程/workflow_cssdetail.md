# 泛微OA 数据表: `workflow_cssdetail`

- **中文名称**: 用户在线编辑CSS文件的明细值
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_cssdetail`
- **主键**: `detailid`
- **字段数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `detailid` | id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `outerbordercolor` | 外边框颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 3 | `outerbordersize` | 外边框宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `requestnamesize` | 流程标题字号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `requestnamecolor` | 流程标题颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 6 | `requestnamefont` | 流程标题字体 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 7 | `requestnamestyle0` | 流程标题是否粗体 | `integer` | - | 是 | 否 | 否 | - | - | 1、是 |
| 8 | `requestnamestyle1` | 流程标题是否斜体 | `integer` | - | 是 | 否 | 否 | - | - | 1、是 |
| 9 | `maintablecolor` | 主表边框颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 10 | `maintablesize` | 主表边框宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `mainfieldsize` | 主表字段显示名字号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `mainfieldcolor` | 主表字段显示名颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 13 | `mainfieldnamecolor` | 主表字段显示名单元格底色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 14 | `mainfieldvaluecolor` | 主表字段值单元格底色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 15 | `mainfieldheight` | 主表单元格高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `detailtablecolor` | 明细表边框颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 17 | `detailtablesize` | 明细表边框宽度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `detailfieldheight` | 明细表单元格高度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `detailfieldsize` | 明细表字段显示名字号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `detailfieldcolor` | 明细表字段显示名颜色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 21 | `detailfieldnamecolor` | 明细表字段显示名单元格底色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 22 | `detailfieldvaluecolor` | 明细表字段值单元格底色 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |

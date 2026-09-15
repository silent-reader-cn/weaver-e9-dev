# 泛微OA 数据表: `workflow_cssdetail`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_cssdetail`
- **字段总数**: `22`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `detailid` | id | `integer` | - | 是 | - |
| 2 | `outerbordercolor` | 外边框颜色 | `varchar2` | 80 | 是 | - |
| 3 | `outerbordersize` | 外边框宽度 | `integer` | - | 是 | - |
| 4 | `requestnamesize` | 流程标题字号 | `integer` | - | 是 | - |
| 5 | `requestnamecolor` | 流程标题颜色 | `varchar2` | 80 | 是 | - |
| 6 | `requestnamefont` | 流程标题字体 | `varchar2` | 160 | 是 | - |
| 7 | `requestnamestyle0` | 流程标题是否粗体 | `integer` | - | 是 | 1、是 |
| 8 | `requestnamestyle1` | 流程标题是否斜体 | `integer` | - | 是 | 1、是 |
| 9 | `maintablecolor` | 主表边框颜色 | `varchar2` | 80 | 是 | - |
| 10 | `maintablesize` | 主表边框宽度 | `integer` | - | 是 | - |
| 11 | `mainfieldsize` | 主表字段显示名字号 | `integer` | - | 是 | - |
| 12 | `mainfieldcolor` | 主表字段显示名颜色 | `varchar2` | 80 | 是 | - |
| 13 | `mainfieldnamecolor` | 主表字段显示名单元格底色 | `varchar2` | 80 | 是 | - |
| 14 | `mainfieldvaluecolor` | 主表字段值单元格底色 | `varchar2` | 80 | 是 | - |
| 15 | `mainfieldheight` | 主表单元格高度 | `integer` | - | 是 | - |
| 16 | `detailtablecolor` | 明细表边框颜色 | `varchar2` | 80 | 是 | - |
| 17 | `detailtablesize` | 明细表边框宽度 | `integer` | - | 是 | - |
| 18 | `detailfieldheight` | 明细表单元格高度 | `integer` | - | 是 | - |
| 19 | `detailfieldsize` | 明细表字段显示名字号 | `integer` | - | 是 | - |
| 20 | `detailfieldcolor` | 明细表字段显示名颜色 | `varchar2` | 80 | 是 | - |
| 21 | `detailfieldnamecolor` | 明细表字段显示名单元格底色 | `varchar2` | 80 | 是 | - |
| 22 | `detailfieldvaluecolor` | 明细表字段值单元格底色 | `varchar2` | 80 | 是 | - |

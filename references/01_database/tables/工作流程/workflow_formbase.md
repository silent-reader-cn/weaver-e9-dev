# 泛微OA 数据表: `workflow_formbase`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formbase`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `formname` | 表单名称 | `varchar2` | 800 | 是 | - |
| 3 | `formdesc` | 表单描述 | `varchar2` | 1000 | 是 | - |
| 4 | `securelevel` | 安全级别 | `char` | 3 | 是 | - |
| 5 | `userid` | 用户id | `integer` | - | 是 | - |
| 6 | `formhtmlcode` | script 脚本 | `varchar2` | 4000 | 是 | - |
| 7 | `formdate` | 创建日期 | `char` | 10 | 是 | - |
| 8 | `subcompanyid` | 子公司id | `integer` | - | 是 | - |
| 9 | `subcompanyid3` | 子公司id3 | `integer` | - | 是 | - |

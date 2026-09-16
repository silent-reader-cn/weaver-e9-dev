# 泛微OA 数据表: `workflow_formbase`

- **中文名称**: 工作流表单信息表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formbase`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `formname` | 表单名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 3 | `formdesc` | 表单描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `securelevel` | 安全级别 | `char` | 3 | 是 | 否 | 否 | - | - | - |
| 5 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `formhtmlcode` | script 脚本 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 7 | `formdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 8 | `subcompanyid` | 子公司id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `subcompanyid3` | 子公司id3 | `integer` | - | 是 | 否 | 否 | - | - | - |

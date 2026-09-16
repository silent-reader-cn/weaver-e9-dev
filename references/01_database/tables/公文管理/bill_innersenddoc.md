# 泛微OA 数据表: `bill_innersenddoc`

- **中文名称**: 内部发文表单
- **所属模块**: `公文管理`
- **数据库表名**: `bill_innersenddoc`
- **主键**: `id`
- **字段数**: `28`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `resourceid` | 资源编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `departmentid` | 部门编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `docid` | 文档编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `pieces` | 数量 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `subjectword` | 主题词 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `dockind` | 文档种类 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `docinstancylevel` | 文档紧急程度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `docsecretlevel` | 文档秘密等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `docnumber` | 文号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `docnumberyear` | 文号年 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `docnumberissue` | 文号事件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `finishdate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 15 | `senddate` | 发送日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 16 | `phone` | 电话 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 17 | `department_1` | 部门编号1 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 18 | `department_2` | 部门编号2 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 19 | `department_3` | 部门编号3 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 20 | `department_4` | 部门编号4 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 21 | `leadercheck` | 领导是否检查 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `generalmanagercheck` | 管理员是否检查 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `resourceid_1` | 资源编号1 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 24 | `resourceid_2` | 资源编号2 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 25 | `resourceid_3` | 资源编号3 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 26 | `resourceid_4` | 资源编号4 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `resourceid_5` | 资源编号5 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `resourceid_6` | 资源编号6 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

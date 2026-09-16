# 泛微OA 数据表: `bill_senddoc`

- **中文名称**: 发文表单
- **所属模块**: `公文管理`
- **数据库表名**: `bill_senddoc`
- **主键**: `id`
- **字段数**: `28`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `generalmanagercheck` | 管理员核查 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `resourceid_1` | 资源编号1 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 3 | `resourceid_2` | 资源编号2 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 4 | `resourceid_3` | 资源编号3 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 5 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `requestid` | 请求编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `subject` | 主题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 8 | `resourceid` | 资源编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `departmentid` | 部门编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `docids` | 文档编号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 11 | `pieces` | 数量 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `subjectword` | 主题关键词 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `dockind` | 文档种类 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `docinstancylevel` | 文档紧急程度 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `docsecretlevel` | 文档保密级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `docnumber` | 文号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `docnumberyear` | 文号年 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `docnumberissue` | 文号事件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `finishdate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 20 | `senddate` | 发送日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `phone` | 联系电话 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 22 | `department_1` | 部门1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `department_2` | 部门2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `department_3` | 部门3 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `department_4` | 部门4 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `desc_n` | 描述 | `varchar2` | 3000 | 是 | 否 | 否 | - | - | - |
| 27 | `systemids` | 系统编号 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 28 | `leadercheck` | 领导核查 | `char` | 1 | 是 | 否 | 否 | - | - | - |

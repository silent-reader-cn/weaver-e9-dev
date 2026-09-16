# 泛微OA 数据表: `workflow_requestuserdefault`

- **中文名称**: 流程自定义表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_requestuserdefault`
- **主键**: `userid`
- **字段数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `wfspaopenwindow` | 流程spa默认弹框 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `signdefault` | 默认意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 3 | `addwfdefaultselectedtab` | 新建流程默认选中tab | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 4 | `addwfmulitcol` | 新建流程默认显示类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `addwfisabc` | 新建流程默认显示abc样式 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `userid` | 自定义用户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `isuserdefault` | 是否自定义 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `numperpage` | 显示行数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `hascreatetime` | 是否显示创建日期 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `hascreater` | 是否显示创建人 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 11 | `hasworkflowname` | 是否显示工作流 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 12 | `hasrequestlevel` | 是否显示紧急程度 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 13 | `hasrequestname` | 是否显示请求说明 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 14 | `hasreceivetime` | 是否显示接收日期 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 15 | `hasstatus` | 是否显示当前状况 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 16 | `hasreceivedpersons` | 是否显示未操作者 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 17 | `hascurrentnode` | 是否显示当前节点 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 18 | `noreceivemailremind` | 是否不接收邮件提醒 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 19 | `showoperator` | 显示操作者 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 20 | `commonuse` | 是否使用常用流程 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 0：否，1：是 |
| 21 | `signlisttype` | 签字意见列表类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `showtype` | 显示类型 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 23 | `multisubmitnotinputsign` | 批量提交是否需要提交签字意见 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 24 | `selectedworkflow` | 显示创建工作流范围 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

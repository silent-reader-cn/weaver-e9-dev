# 泛微OA 数据表: `prj_settings`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_settings`
- **字段总数**: `26`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `subcompanyid` | 分部id | `integer` | - | 是 | 分部id |
| 3 | `departmentid` | 部门id | `integer` | - | 是 | 部门id |
| 4 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 5 | `prj_dsc_doc` | 项目交流文档开关 | `char` | 1 | 是 | 项目交流文档开关 |
| 6 | `prj_dsc_wf` | 项目交流流程开关 | `char` | 1 | 是 | 项目交流流程开关 |
| 7 | `prj_dsc_crm` | 项目交流客户开关 | `char` | 1 | 是 | 项目交流客户开关 |
| 8 | `prj_dsc_prj` | 项目交流项目开关 | `char` | 1 | 是 | 项目交流项目开关 |
| 9 | `prj_dsc_tsk` | 项目交流任务开关 | `char` | 1 | 是 | 项目交流任务开关 |
| 10 | `prj_dsc_acc` | 项目交流附件开关 | `char` | 1 | 是 | 项目交流附件开关 |
| 11 | `prj_dsc_accsec` | 项目交流附件目录 | `integer` | - | 是 | 项目交流附件目录 |
| 12 | `tsk_dsc_doc` | 任务交流文档开关 | `char` | 1 | 是 | 任务交流文档开关 |
| 13 | `tsk_dsc_wf` | 任务交流流程开关 | `char` | 1 | 是 | 任务交流流程开关 |
| 14 | `tsk_dsc_crm` | 任务交流客户开关 | `char` | 1 | 是 | 任务交流客户开关 |
| 15 | `tsk_dsc_prj` | 任务交流项目开关 | `char` | 1 | 是 | 任务交流项目开关 |
| 16 | `tsk_dsc_tsk` | 任务交流任务开关 | `char` | 1 | 是 | 任务交流任务开关 |
| 17 | `tsk_dsc_acc` | 任务交流附件开关 | `char` | 1 | 是 | 任务交流附件开关 |
| 18 | `tsk_dsc_accsec` | 任务交流附件目录 | `integer` | - | 是 | 任务交流附件目录 |
| 19 | `prj_acc` | 项目卡片附件开关 | `char` | 1 | 是 | 项目卡片附件开关 |
| 20 | `prj_accsec` | 项目卡片附件目录 | `integer` | - | 是 | 项目卡片附件目录 |
| 21 | `tsk_acc` | 任务卡片附件开关 | `char` | 1 | 是 | 任务卡片附件开关 |
| 22 | `tsk_accsec` | 任务卡片附件目录 | `integer` | - | 是 | 任务卡片附件目录 |
| 23 | `prj_gnt_showplan_` | 甘特图显示计划任务 | `char` | 1 | 是 | 甘特图显示计划任务 |
| 24 | `prj_gnt_warningday` | 甘特图显示预警提前天数 | `integer` | - | 是 | 甘特图显示预警提前天数 |
| 25 | `tsk_approval` | 任务审批开关 | `char` | 1 | 是 | 任务审批开关 |
| 26 | `tsk_approval_type` | 任务审批类型 | `integer` | - | 是 | 1,项目经理审批; 2,任务上级负责人审批; |

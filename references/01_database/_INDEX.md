# 数据库表总索引

> 共收录 **1699** 张表，覆盖 26 个业务模块。索引由 `scripts/build_index.py` 从 `tables/` 下的 Markdown 自动生成，请勿手工编辑。

> 检索表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py workflow_currentoperator --scope db -d
> python scripts/search.py 待办 --scope db
> ```

## 模块统计概览

| 序号 | 业务模块 | 表数量 | 说明 |
| :---: | :--- | :---: | :--- |
| 1 | [人力资源](#人力资源) | **295** | 涵盖 人力资源 模块核心业务与系统配置表 |
| 2 | [工作流程](#工作流程) | **236** | 涵盖 工作流程 模块核心业务与系统配置表 |
| 3 | [集成模块](#集成模块) | **136** | 涵盖 集成模块 模块核心业务与系统配置表 |
| 4 | [财务管理](#财务管理) | **133** | 涵盖 财务管理 模块核心业务与系统配置表 |
| 5 | [表单建模](#表单建模) | **120** | 涵盖 表单建模 模块核心业务与系统配置表 |
| 6 | [客户管理](#客户管理) | **103** | 涵盖 客户管理 模块核心业务与系统配置表 |
| 7 | [知识管理](#知识管理) | **92** | 涵盖 知识管理 模块核心业务与系统配置表 |
| 8 | [门户管理](#门户管理) | **53** | 涵盖 门户管理 模块核心业务与系统配置表 |
| 9 | [公文管理](#公文管理) | **49** | 涵盖 公文管理 模块核心业务与系统配置表 |
| 10 | [会议管理](#会议管理) | **48** | 涵盖 会议管理 模块核心业务与系统配置表 |
| 11 | [政务应用](#政务应用) | **47** | 涵盖 政务应用 模块核心业务与系统配置表 |
| 12 | [项目管理](#项目管理) | **47** | 涵盖 项目管理 模块核心业务与系统配置表 |
| 13 | [即时通讯-EMESSAGE](#即时通讯-emessage) | **46** | 涵盖 即时通讯-EMESSAGE 模块核心业务与系统配置表 |
| 14 | [E9新版考勤表结构](#e9新版考勤表结构) | **36** | 涵盖 E9新版考勤表结构 模块核心业务与系统配置表 |
| 15 | [日程管理](#日程管理) | **33** | 涵盖 日程管理 模块核心业务与系统配置表 |
| 16 | [其他](#其他) | **32** | 涵盖 其他 模块核心业务与系统配置表 |
| 17 | [邮件模块](#邮件模块) | **32** | 涵盖 邮件模块 模块核心业务与系统配置表 |
| 18 | [移动引擎](#移动引擎) | **29** | 涵盖 移动引擎 模块核心业务与系统配置表 |
| 19 | [资产管理](#资产管理) | **27** | 涵盖 资产管理 模块核心业务与系统配置表 |
| 20 | [工作微博](#工作微博) | **26** | 涵盖 工作微博 模块核心业务与系统配置表 |
| 21 | [协作管理](#协作管理) | **21** | 涵盖 协作管理 模块核心业务与系统配置表 |
| 22 | [版本升级](#版本升级) | **17** | 涵盖 版本升级 模块核心业务与系统配置表 |
| 23 | [网上调查](#网上调查) | **17** | 涵盖 网上调查 模块核心业务与系统配置表 |
| 24 | [短信模块](#短信模块) | **11** | 涵盖 短信模块 模块核心业务与系统配置表 |
| 25 | [车辆管理](#车辆管理) | **7** | 涵盖 车辆管理 模块核心业务与系统配置表 |
| 26 | [微搜](#微搜) | **6** | 涵盖 微搜 模块核心业务与系统配置表 |
| **合计** | **全部模块** | **1699** | - |

---

## 分模块全量表清单

### 人力资源

> 本模块共收录 `295` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `bill_hrmawardinfo` | 8 | `id`(ID)、`rptitle`(奖惩标题)、`resource_n`(员工id)、`rpdate`(奖惩日期) 等共 8 个字段 | [bill_hrmawardinfo.md](./tables/人力资源/bill_hrmawardinfo.md) |
| 2 | `bill_hrmdismiss` | 7 | `id`(ID)、`resource_n`(申请人)、`dismissdate`(离职时间)、`docid`(离职合同) 等共 7 个字段 | [bill_hrmdismiss.md](./tables/人力资源/bill_hrmdismiss.md) |
| 3 | `bill_hrmhire` | 6 | `id`(ID)、`resource_n`(申请人)、`hiredate`(转正日期)、`hirereason`(转正备注) 等共 6 个字段 | [bill_hrmhire.md](./tables/人力资源/bill_hrmhire.md) |
| 4 | `bill_hrmovertimesapa` | 16 | `id`(ID)、`resourceid`(姓名)、`departmentid`(部门)、`applydate`(申请日期) 等共 16 个字段 | [bill_hrmovertimesapa.md](./tables/人力资源/bill_hrmovertimesapa.md) |
| 5 | `bill_hrmredeploy` | 11 | `id`(ID)、`resource_n`(申请人)、`redeploydate`(调动日期)、`oldjob`(原岗位) 等共 11 个字段 | [bill_hrmredeploy.md](./tables/人力资源/bill_hrmredeploy.md) |
| 6 | `bill_hrmscheduledetail` | 8 | `id`(ID)、`scheduleid`(请假主表id)、`diffid`(请假类型id)、`startdate`(开始日期) 等共 8 个字段 | [bill_hrmscheduledetail.md](./tables/人力资源/bill_hrmscheduledetail.md) |
| 7 | `bill_hrmschedulemain` | 6 | `id`(ID)、`resource_n`(申请人)、`reason`(事由)、`sumday`(总天数) 等共 6 个字段 | [bill_hrmschedulemain.md](./tables/人力资源/bill_hrmschedulemain.md) |
| 8 | `bill_hrmtimedetail` | 18 | `id`(ID)、`requestid`(流程id)、`name`(说明)、`resourceid`(提交人) 等共 18 个字段 | [bill_hrmtimedetail.md](./tables/人力资源/bill_hrmtimedetail.md) |
| 9 | `bill_hrmtrainplan` | 6 | `id`(ID)、`resource_n`(申请人)、`trainplanid`(培训安排)、`reason`(说明) 等共 6 个字段 | [bill_hrmtrainplan.md](./tables/人力资源/bill_hrmtrainplan.md) |
| 10 | `bill_hrmusedemand` | 15 | `id`(ID)、`resource_n`(人员id)、`demandjobtitle`(岗位)、`demandnum`(数量) 等共 15 个字段 | [bill_hrmusedemand.md](./tables/人力资源/bill_hrmusedemand.md) |
| 11 | `departmentdefinefield` | 6 | `id`(ID)、`billid`(单据id)、`fieldname`(数据库表字段名称)、`fieldlabel`(字段显示名称) 等共 6 个字段 | [departmentdefinefield.md](./tables/人力资源/departmentdefinefield.md) |
| 12 | `docsignature` | 11 | `markid`(签章id)、`hrmresid`(签章所属的用户id)、`password`(用户签章的密码)、`markname`(签章名称) 等共 11 个字段 | [docsignature.md](./tables/人力资源/docsignature.md) |
| 13 | `hrm_att_vacation` | 11 | `id`(ID)、`field001`(请求id)、`field002`(流程id)、`field003`(人员id) 等共 11 个字段 | [hrm_att_vacation.md](./tables/人力资源/hrm_att_vacation.md) |
| 14 | `hrm_chart_set` | 6 | `id`(ID)、`is_sys`(是否系统默认)、`author`(创建人)、`show_type`(显示类型) 等共 6 个字段 | [hrm_chart_set.md](./tables/人力资源/hrm_chart_set.md) |
| 15 | `hrm_compensationtargetdetail` | 3 | `compensationtargetid`(指标数据id)、`targetid`(指标id)、`target`(指标值) | [hrm_compensationtargetdetail.md](./tables/人力资源/hrm_compensationtargetdetail.md) |
| 16 | `hrm_compensationtargetinfo` | 8 | `id`(ID)、`subcompanyid`(分部id)、`departmentid`(部门id)、`compensationyear`(年) 等共 8 个字段 | [hrm_compensationtargetinfo.md](./tables/人力资源/hrm_compensationtargetinfo.md) |
| 17 | `hrm_compensationtargetset` | 5 | `id`(ID)、`subcompanyid`(分部id)、`targetname`(简称)、`explain`(说明) 等共 5 个字段 | [hrm_compensationtargetset.md](./tables/人力资源/hrm_compensationtargetset.md) |
| 18 | `hrm_comtargetsetdetail` | 2 | `targetid`(指标设置id)、`companyordeptid`(部门/分部id) | [hrm_comtargetsetdetail.md](./tables/人力资源/hrm_comtargetsetdetail.md) |
| 19 | `hrm_detialformfield` | 11 | `fieldid`(字段id)、`fielddbtype`(字段类型)、`fieldname`(数据库字段名)、`fieldlabel`(字段显示名) 等共 11 个字段 | [hrm_detialformfield.md](./tables/人力资源/hrm_detialformfield.md) |
| 20 | `hrm_fieldgroup` | 5 | `isshow`(是否显示)、`id`(ID)、`grouplabel`(分组名称 label id)、`grouporder`(序列号) 等共 5 个字段 | [hrm_fieldgroup.md](./tables/人力资源/hrm_fieldgroup.md) |
| 21 | `hrm_forgotpassword` | 3 | `id`(ID)、`forgottype`(忘记类型)、`forgottypelabel`(忘记类型标签) | [hrm_forgotpassword.md](./tables/人力资源/hrm_forgotpassword.md) |
| 22 | `hrm_formfield` | 5 | `fieldid`(字段id)、`fielddbtype`(字段数据库类型)、`fieldname`(字段名称)、`fieldlabel`(字段显示名labelid) 等共 5 个字段 | [hrm_formfield.md](./tables/人力资源/hrm_formfield.md) |
| 23 | `hrm_mobile_ca_cert` | 7 | `userid`(人员ID)、`uuid`(UUID)、`cert`(签名后数据)、`lastname`(姓名) 等共 7 个字段 | [hrm_mobile_ca_cert.md](./tables/人力资源/hrm_mobile_ca_cert.md) |
| 24 | `hrm_paid_leave` | 14 | `id`(ID序列号)、`delflag`(删除标识)、`field001`(流程)、`field002`(员工) 等共 14 个字段 | [hrm_paid_leave.md](./tables/人力资源/hrm_paid_leave.md) |
| 25 | `hrm_password_protection_set` | 3 | `id`(ID)、`user_id`(用户id)、`enabled`(是否开启) | [hrm_password_protection_set.md](./tables/人力资源/hrm_password_protection_set.md) |
| 26 | `hrm_piecerateinfo` | 10 | `id`(ID)、`subcompanyid`(分部id)、`departmentid`(部门id)、`pieceyear`(年) 等共 10 个字段 | [hrm_piecerateinfo.md](./tables/人力资源/hrm_piecerateinfo.md) |
| 27 | `hrm_pieceratesetting` | 7 | `id`(ID)、`subcompanyid`(分部id)、`piecerateno`(计件编号)、`pieceratename`(计件名称) 等共 7 个字段 | [hrm_pieceratesetting.md](./tables/人力资源/hrm_pieceratesetting.md) |
| 28 | `hrm_protection_question` | 5 | `id`(ID)、`user_id`(用户id)、`question`(问题描述value值)、`answer`(问题答案value值) 等共 5 个字段 | [hrm_protection_question.md](./tables/人力资源/hrm_protection_question.md) |
| 29 | `hrm_resource_export_template` | 9 | `id`(ID)、`name`(模板名称)、`fields`(所有字段)、`issystem`(是否是系统字段) 等共 9 个字段 | [hrm_resource_export_template.md](./tables/人力资源/hrm_resource_export_template.md) |
| 30 | `hrm_rp_sub_template` | 6 | `id`(ID)、`name`(模板名称)、`author`(创建人id)、`create_date`(创建时间) 等共 6 个字段 | [hrm_rp_sub_template.md](./tables/人力资源/hrm_rp_sub_template.md) |
| 31 | `hrm_rp_sub_template_con` | 9 | `id`(ID)、`template_id`(模板id)、`col_name`(字段名称)、`con_htmltype`(组件类型) 等共 9 个字段 | [hrm_rp_sub_template_con.md](./tables/人力资源/hrm_rp_sub_template_con.md) |
| 32 | `hrm_schedule_personnel` | 14 | `id`(ID)、`delflag`(是否删除)、`creater`(创建人)、`create_time`(创建时间) 等共 14 个字段 | [hrm_schedule_personnel.md](./tables/人力资源/hrm_schedule_personnel.md) |
| 33 | `hrm_schedule_personnel_val` | 4 | `id`(序列号)、`delflag`(删除标识)、`field001`(范围ID)、`field002`(对象ID) | [hrm_schedule_personnel_val.md](./tables/人力资源/hrm_schedule_personnel_val.md) |
| 34 | `hrm_schedule_resttime` | 9 | `id`(ID)、`worktimeid`(工作时间id)、`delflag`(删除标志)、`reststarttime`(休息开始时间) 等共 9 个字段 | [hrm_schedule_resttime.md](./tables/人力资源/hrm_schedule_resttime.md) |
| 35 | `hrm_schedule_set` | 11 | `id`(ID)、`delflag`(delflag)、`creater`(创建人)、`create_time`(创建时间) 等共 11 个字段 | [hrm_schedule_set.md](./tables/人力资源/hrm_schedule_set.md) |
| 36 | `hrm_schedule_set_detail` | 8 | `id`(ID)、`delflag`(delflag)、`field001`(班次)、`field002`(人员) 等共 8 个字段 | [hrm_schedule_set_detail.md](./tables/人力资源/hrm_schedule_set_detail.md) |
| 37 | `hrm_schedule_set_person` | 4 | `id`(ID)、`delflag`(删除标记)、`field001`(所属排班)、`field002`(排班人员) | [hrm_schedule_set_person.md](./tables/人力资源/hrm_schedule_set_person.md) |
| 38 | `hrm_schedule_shifts_detail` | 46 | `id`(ID)、`delflag`(删除标记)、`mfid`(mfid)、`d001`(1日) 等共 46 个字段 | [hrm_schedule_shifts_detail.md](./tables/人力资源/hrm_schedule_shifts_detail.md) |
| 39 | `hrm_schedule_shifts_set` | 14 | `id`(ID)、`delflag`(delflag)、`creater`(创建人)、`create_time`(创建时间) 等共 14 个字段 | [hrm_schedule_shifts_set.md](./tables/人力资源/hrm_schedule_shifts_set.md) |
| 40 | `hrm_schedule_shifts_wt` | 4 | `id`(ID)、`field001`(所属班次)、`field002`(工作时段)、`field003`(班次明细) | [hrm_schedule_shifts_wt.md](./tables/人力资源/hrm_schedule_shifts_wt.md) |
| 41 | `hrm_schedule_worktime` | 13 | `id`(ID)、`delflag`(delflag)、`creater`(创建人)、`create_time`(创建时间) 等共 13 个字段 | [hrm_schedule_worktime.md](./tables/人力资源/hrm_schedule_worktime.md) |
| 42 | `hrm_searchfield` | 12 | `fieldid`(字段id)、`fieldname`(数据库字段名)、`fieldlabel`(字段显示名)、`fieldhtmltype`(字段类型) 等共 12 个字段 | [hrm_searchfield.md](./tables/人力资源/hrm_searchfield.md) |
| 43 | `hrm_searchselectitem` | 7 | `id`(ID)、`fieldid`(字段id)、`selectvalue`(选项值)、`selectname`(选项名) 等共 7 个字段 | [hrm_searchselectitem.md](./tables/人力资源/hrm_searchselectitem.md) |
| 44 | `hrm_selectitem` | 12 | `fieldid`(选择框对应的字段id)、`isbill`(关联流程)、`selectvalue`(已选值)、`selectname`(已选名称) 等共 12 个字段 | [hrm_selectitem.md](./tables/人力资源/hrm_selectitem.md) |
| 45 | `hrm_sync_log` | 7 | `id`(ID)、`dataid`(数据id)、`outkey`(外部主键)、`datatype`(数据类型) 等共 7 个字段 | [hrm_sync_log.md](./tables/人力资源/hrm_sync_log.md) |
| 46 | `hrm_transfer_log` | 14 | `id`(ID)、`type`(类型)、`fromid`(来源id)、`toid`(转移目标id) 等共 14 个字段 | [hrm_transfer_log.md](./tables/人力资源/hrm_transfer_log.md) |
| 47 | `hrm_transfer_log_detail` | 7 | `id`(ID)、`log_id`(日志id)、`code_name`(权限代码)、`p_num`(关联数量) 等共 7 个字段 | [hrm_transfer_log_detail.md](./tables/人力资源/hrm_transfer_log_detail.md) |
| 48 | `hrm_transfer_set` | 7 | `id`(ID)、`type`(所属类型)、`name`(权限名称)、`code_name`(权限代码) 等共 7 个字段 | [hrm_transfer_set.md](./tables/人力资源/hrm_transfer_set.md) |
| 49 | `hrm_usb_auto_date` | 6 | `id`(ID)、`user_id`(用户id)、`need_auto`(是否使用)、`enable_date`(生效日期) 等共 6 个字段 | [hrm_usb_auto_date.md](./tables/人力资源/hrm_usb_auto_date.md) |
| 50 | `hrm_user_status` | 3 | `id`(ID)、`user_id`(用户id)、`online_flag`(在线状态) | [hrm_user_status.md](./tables/人力资源/hrm_user_status.md) |
| 51 | `hrmactivitiescompetency` | 3 | `id`(ID)、`jobactivityid`(对应的职责id)、`competencyid`(对应的技能id) | [hrmactivitiescompetency.md](./tables/人力资源/hrmactivitiescompetency.md) |
| 52 | `hrmannualbatchprocess` | 4 | `id`(ID)、`workingage`(工龄)、`annualdays`(年假天数)、`subcompanyid`(分部id) | [hrmannualbatchprocess.md](./tables/人力资源/hrmannualbatchprocess.md) |
| 53 | `hrmannualleaveinfo` | 12 | `id`(ID)、`requestid`(请求id)、`resourceid`(请假人)、`startdate`(开始日期) 等共 12 个字段 | [hrmannualleaveinfo.md](./tables/人力资源/hrmannualleaveinfo.md) |
| 54 | `hrmannualmanagement` | 5 | `id`(ID)、`resourceid`(用户id)、`annualyear`(年假年)、`annualdays`(年假天数) 等共 5 个字段 | [hrmannualmanagement.md](./tables/人力资源/hrmannualmanagement.md) |
| 55 | `hrmannualperiod` | 5 | `id`(ID)、`annualyear`(年假年)、`startdate`(年假开始日期)、`enddate`(年假结束日期) 等共 5 个字段 | [hrmannualperiod.md](./tables/人力资源/hrmannualperiod.md) |
| 56 | `hrmapplyremark` | 6 | `id`(ID)、`applyid`(关联id)、`remark`(详情)、`resourceid`(人员id) 等共 6 个字段 | [hrmapplyremark.md](./tables/人力资源/hrmapplyremark.md) |
| 57 | `hrmarrangeshift` | 7 | `id`(ID)、`shiftname`(排班名称)、`shiftbegintime`(开始时间)、`shiftendtime`(结束时间) 等共 7 个字段 | [hrmarrangeshift.md](./tables/人力资源/hrmarrangeshift.md) |
| 58 | `hrmarrangeshiftinfo` | 4 | `id`(ID)、`resourceid`(人员id)、`shiftdate`(排班日志)、`shiftid`(排班id) | [hrmarrangeshiftinfo.md](./tables/人力资源/hrmarrangeshiftinfo.md) |
| 59 | `hrmarrangeshiftset` | 6 | `id`(ID)、`resourceid`(人力资源id)、`sharetype`(分配类型)、`relatedid`(相关id) 等共 6 个字段 | [hrmarrangeshiftset.md](./tables/人力资源/hrmarrangeshiftset.md) |
| 60 | `hrmarrangeshifttype` | 3 | `resourceid`(人员id)、`currentdate`(当前时间)、`shifttypeid`(排班种类id) | [hrmarrangeshifttype.md](./tables/人力资源/hrmarrangeshifttype.md) |
| 61 | `hrmawardinfo` | 7 | `id`(ID)、`rptitle`(奖惩主题)、`rptypeid`(奖惩种类)、`rpdate`(奖惩日期) 等共 7 个字段 | [hrmawardinfo.md](./tables/人力资源/hrmawardinfo.md) |
| 62 | `hrmawardtype` | 5 | `id`(ID)、`name`(名称)、`awardtype`(奖惩类型)、`description`(描述) 等共 5 个字段 | [hrmawardtype.md](./tables/人力资源/hrmawardtype.md) |
| 63 | `hrmbank` | 3 | `id`(ID)、`bankname`(银行名称)、`bankdesc`(银行描述) | [hrmbank.md](./tables/人力资源/hrmbank.md) |
| 64 | `hrmbirthdayshare` | 16 | `seclevelto`(最高等级)、`jobtitleid`(岗位id)、`jobtitlelevel`(岗位等级)、`jobdepartment`(岗位所在部门) 等共 16 个字段 | [hrmbirthdayshare.md](./tables/人力资源/hrmbirthdayshare.md) |
| 65 | `hrmbirthremindmsg` | 4 | `id`(ID)、`title`(提醒内容)、`resources`(人员id字符串)、`reminddate`(提醒时间) | [hrmbirthremindmsg.md](./tables/人力资源/hrmbirthremindmsg.md) |
| 66 | `hrmbycheckpeople` | 8 | `id`(ID)、`checkid`(考核id)、`resourceid`(被考核人的id)、`checkercount`(考核人的id) 等共 8 个字段 | [hrmbycheckpeople.md](./tables/人力资源/hrmbycheckpeople.md) |
| 67 | `hrmcapitaluse` | 4 | `id`(ID)、`capitalid`(资产id)、`hrmid`(人员id)、`cptnum`(核算数量) | [hrmcapitaluse.md](./tables/人力资源/hrmcapitaluse.md) |
| 68 | `hrmcardinfo` | 6 | `id`(ID)、`stationid`(卡钟的台号)、`carddate`(打卡日期)、`cardtime`(打卡时间) 等共 6 个字段 | [hrmcardinfo.md](./tables/人力资源/hrmcardinfo.md) |
| 69 | `hrmcareerapply` | 114 | `folk`(民族)、`islabouunion`(是否为工会会员)、`tempresidentnumber`(暂住证号)、`nowstep`(当前所处阶段) 等共 114 个字段 | [hrmcareerapply.md](./tables/人力资源/hrmcareerapply.md) |
| 70 | `hrmcareerapplyotherinfo` | 3 | `id`(ID)、`applyid`(应聘者id)、`category`(应聘者类别) | [hrmcareerapplyotherinfo.md](./tables/人力资源/hrmcareerapplyotherinfo.md) |
| 71 | `hrmcareerinvite` | 6 | `id`(ID)、`careername`(职位名称)、`careerpeople`(招聘人数)、`careerage`(年龄) 等共 6 个字段 | [hrmcareerinvite.md](./tables/人力资源/hrmcareerinvite.md) |
| 72 | `hrmcareerinvitestep` | 9 | `id`(ID)、`inviteid`(招聘信息id)、`name`(步骤名称)、`startdate`(步骤开始日期) 等共 9 个字段 | [hrmcareerinvitestep.md](./tables/人力资源/hrmcareerinvitestep.md) |
| 73 | `hrmcareerplan` | 13 | `id`(ID)、`topic`(招聘主题)、`principalid`(负责人id)、`informmanid`(通知人id) 等共 13 个字段 | [hrmcareerplan.md](./tables/人力资源/hrmcareerplan.md) |
| 74 | `hrmcareerplaninform` | 5 | `id`(ID)、`careerplanid`(招聘计划id)、`resourceid`(人力资源id)、`type`(通知类型) 等共 5 个字段 | [hrmcareerplaninform.md](./tables/人力资源/hrmcareerplaninform.md) |
| 75 | `hrmcareerplanstep` | 5 | `id`(ID)、`planid`(招聘计划id)、`stepname`(步骤名称)、`stepstartdate`(步骤开始日期) 等共 5 个字段 | [hrmcareerplanstep.md](./tables/人力资源/hrmcareerplanstep.md) |
| 76 | `hrmcareerworkexp` | 7 | `id`(ID)、`ftime`(工作开始日期)、`ttime`(工作结束日期)、`company`(工作公司) 等共 7 个字段 | [hrmcareerworkexp.md](./tables/人力资源/hrmcareerworkexp.md) |
| 77 | `hrmcertification` | 6 | `id`(ID)、`resourceid`(人力资源id)、`datefrom`(开始日期)、`dateto`(结束日期) 等共 6 个字段 | [hrmcertification.md](./tables/人力资源/hrmcertification.md) |
| 78 | `hrmcheckactor` | 5 | `id`(ID)、`checktypeid`(考核种类id)、`typeid`(考核id)、`resourceid`(考核人) 等共 5 个字段 | [hrmcheckactor.md](./tables/人力资源/hrmcheckactor.md) |
| 79 | `hrmcheckgrade` | 5 | `id`(ID)、`checkpeopleid`(被考核人信息表的id)、`checkitemid`(考核项目id)、`result`(考核人对被考核人打的某一项的成绩) 等共 5 个字段 | [hrmcheckgrade.md](./tables/人力资源/hrmcheckgrade.md) |
| 80 | `hrmcheckitem` | 3 | `id`(ID)、`checkitemname`(考核项目名称)、`checkitemexplain`(考核项目说明) | [hrmcheckitem.md](./tables/人力资源/hrmcheckitem.md) |
| 81 | `hrmcheckkind` | 5 | `id`(ID)、`kindname`(考核种类名称)、`checkcycle`(考核周期)、`checkexpecd`(考核期) 等共 5 个字段 | [hrmcheckkind.md](./tables/人力资源/hrmcheckkind.md) |
| 82 | `hrmcheckkinditem` | 4 | `id`(ID)、`checktypeid`(考核种类的id)、`checkitemid`(考核项目的id)、`checkitemproportion`(考核项目的权重) | [hrmcheckkinditem.md](./tables/人力资源/hrmcheckkinditem.md) |
| 83 | `hrmchecklist` | 6 | `id`(ID)、`checkname`(每一次考核的名称)、`checktypeid`(考核种类的id)、`startdate`(考核的开始日期) 等共 6 个字段 | [hrmchecklist.md](./tables/人力资源/hrmchecklist.md) |
| 84 | `hrmcheckpost` | 5 | `id`(ID)、`checktypeid`(考核种类的id)、`jobid`(考核岗位的id)、`deptid`(部门id) 等共 5 个字段 | [hrmcheckpost.md](./tables/人力资源/hrmcheckpost.md) |
| 85 | `hrmcity` | 7 | `id`(ID)、`cityname`(城市名称)、`citylongitude`(城市经度)、`citylatitude`(城市纬度) 等共 7 个字段 | [hrmcity.md](./tables/人力资源/hrmcity.md) |
| 86 | `hrmcitytwo` | 6 | `id`(ID)、`cityname`(城市名称)、`citylongitude`(城市经度)、`citylatitude`(城市纬度) 等共 6 个字段 | [hrmcitytwo.md](./tables/人力资源/hrmcitytwo.md) |
| 87 | `hrmcompany` | 5 | `lastinittime`(上次初始化时间)、`id`(ID)、`companyname`(总部名称)、`companydesc`(总部描述) 等共 5 个字段 | [hrmcompany.md](./tables/人力资源/hrmcompany.md) |
| 88 | `hrmcompanyvirtual` | 8 | `id`(ID)、`companyname`(总部名称)、`companycode`(总部机构代码)、`companydesc`(总部描述) 等共 8 个字段 | [hrmcompanyvirtual.md](./tables/人力资源/hrmcompanyvirtual.md) |
| 89 | `hrmcompetency` | 4 | `id`(ID)、`competencymark`(备注)、`competencyname`(技能说明)、`competencyremark`(技能标识) | [hrmcompetency.md](./tables/人力资源/hrmcompetency.md) |
| 90 | `hrmcomponentstat` | 5 | `id`(ID)、`resourceid`(人力资源id)、`salarystat`(总金额)、`periodyear`(年) 等共 5 个字段 | [hrmcomponentstat.md](./tables/人力资源/hrmcomponentstat.md) |
| 91 | `hrmcontract` | 8 | `id`(ID)、`contractname`(合同名称)、`contractman`(合同人员)、`contracttypeid`(合同种类id) 等共 8 个字段 | [hrmcontract.md](./tables/人力资源/hrmcontract.md) |
| 92 | `hrmcontractshare` | 16 | `id`(ID)、`sharetype`(提醒类型)、`seclevel`(安全级别从)、`rolelevel`(角色级别) 等共 16 个字段 | [hrmcontractshare.md](./tables/人力资源/hrmcontractshare.md) |
| 93 | `hrmcontracttemplet` | 4 | `id`(ID)、`templetname`(合同模板名称)、`templetdocid`(合同模板文档id)、`subcompanyid`(合同模板所属分部id) | [hrmcontracttemplet.md](./tables/人力资源/hrmcontracttemplet.md) |
| 94 | `hrmcontracttype` | 8 | `id`(ID)、`typename`(合同种类名称)、`contracttempletid`(合同模板id)、`saveurl`(合同文档目录) 等共 8 个字段 | [hrmcontracttype.md](./tables/人力资源/hrmcontracttype.md) |
| 95 | `hrmcountry` | 4 | `id`(ID)、`countryname`(国家名称)、`countrydesc`(国家描述)、`canceled`(是否封存) | [hrmcountry.md](./tables/人力资源/hrmcountry.md) |
| 96 | `hrmdepartment` | 24 | `modified`(修改时间)、`modifier`(修改人)、`id`(ID)、`departmentmark`(部门标识) 等共 24 个字段 | [hrmdepartment.md](./tables/人力资源/hrmdepartment.md) |
| 97 | `hrmdepartmentvirtual` | 12 | `id`(ID)、`departmentname`(部门名称)、`departmentcode`(部门机构代码)、`departmentmark`(部门标识) 等共 12 个字段 | [hrmdepartmentvirtual.md](./tables/人力资源/hrmdepartmentvirtual.md) |
| 98 | `hrmeducationinfo` | 7 | `id`(ID)、`resourceid`(人力资源id)、`startdate`(开始时间)、`enddate`(结束时间) 等共 7 个字段 | [hrmeducationinfo.md](./tables/人力资源/hrmeducationinfo.md) |
| 99 | `hrmeducationlevel` | 3 | `id`(ID)、`name`(名称)、`description`(描述) | [hrmeducationlevel.md](./tables/人力资源/hrmeducationlevel.md) |
| 100 | `hrmfamilyinfo` | 7 | `id`(ID)、`resourceid`(人力资源id)、`member`(家庭成员)、`title`(称谓) 等共 7 个字段 | [hrmfamilyinfo.md](./tables/人力资源/hrmfamilyinfo.md) |
| 101 | `hrmgroup` | 6 | `id`(ID)、`name`(组名称)、`type`(组类型)、`owner`(创建人) 等共 6 个字段 | [hrmgroup.md](./tables/人力资源/hrmgroup.md) |
| 102 | `hrmgroupmembers` | 18 | `id`(ID)、`groupid`(自定义组id)、`sharetype`(共享类型)、`userid`(成员id) 等共 18 个字段 | [hrmgroupmembers.md](./tables/人力资源/hrmgroupmembers.md) |
| 103 | `hrmgroupshare` | 17 | `id`(ID)、`groupid`(组id)、`sharetype`(共享类型)、`seclevel`(安全级别) 等共 17 个字段 | [hrmgroupshare.md](./tables/人力资源/hrmgroupshare.md) |
| 104 | `hrmimporthistory` | 8 | `id`(ID)、`operator`(操作者)、`operatetime`(导入时间)、`clientaddress`(客户端地址) 等共 8 个字段 | [hrmimporthistory.md](./tables/人力资源/hrmimporthistory.md) |
| 105 | `hrmimporthistorydetail` | 7 | `logsmalltype`(日志类型)、`id`(ID)、`pid`(历史记录表id)、`rownums`(行号) 等共 7 个字段 | [hrmimporthistorydetail.md](./tables/人力资源/hrmimporthistorydetail.md) |
| 106 | `hrminfomaintenance` | 8 | `id`(ID)、`itemname`(入职维护项目名称)、`hrmid`(入职维护项目负责人)、`operateuserid`(操作者用户id) 等共 8 个字段 | [hrminfomaintenance.md](./tables/人力资源/hrminfomaintenance.md) |
| 107 | `hrminfostatus` | 4 | `id`(ID)、`itemid`(入职项目)、`status`(入职项目完成状态)、`hrmid`(入职人) | [hrminfostatus.md](./tables/人力资源/hrminfostatus.md) |
| 108 | `hrminterview` | 9 | `id`(ID)、`resourceid`(应聘人员id)、`stepid`(应聘人员所处步骤)、`date_n`(面试日期) 等共 9 个字段 | [hrminterview.md](./tables/人力资源/hrminterview.md) |
| 109 | `hrminterviewassess` | 7 | `id`(ID)、`resourceid`(应聘人员id)、`stepid`(应聘人员所处步骤)、`result`(考评结果) 等共 7 个字段 | [hrminterviewassess.md](./tables/人力资源/hrminterviewassess.md) |
| 110 | `hrminterviewresult` | 7 | `id`(ID)、`resourceid`(应聘人员id)、`stepid`(应聘人员所处步骤)、`result`(考核结果) 等共 7 个字段 | [hrminterviewresult.md](./tables/人力资源/hrminterviewresult.md) |
| 111 | `hrmjobactivities` | 10 | `id`(ID)、`jobactivitymark`(职责标识)、`jobactivityname`(职责描述)、`jobgroupid`(所属工作类型) 等共 10 个字段 | [hrmjobactivities.md](./tables/人力资源/hrmjobactivities.md) |
| 112 | `hrmjobcall` | 3 | `id`(ID)、`name`(名称)、`description`(描述) | [hrmjobcall.md](./tables/人力资源/hrmjobcall.md) |
| 113 | `hrmjobgroups` | 7 | `id`(ID)、`jobgroupname`(工作类型描述)、`jobgroupremark`(工作类型标识)、`created`(创建时间) 等共 7 个字段 | [hrmjobgroups.md](./tables/人力资源/hrmjobgroups.md) |
| 114 | `hrmjobtitles` | 16 | `created`(创建时间)、`creater`(创建人)、`modified`(修改时间)、`modifier`(修改人) 等共 16 个字段 | [hrmjobtitles.md](./tables/人力资源/hrmjobtitles.md) |
| 115 | `hrmjobtitlessysbak` | 12 | `id`(ID)、`jobtitlemark`(职位标识)、`jobtitlename`(职位描述)、`jobtitleremark`(备注) 等共 12 个字段 | [hrmjobtitlessysbak.md](./tables/人力资源/hrmjobtitlessysbak.md) |
| 116 | `hrmjobtitlestemplet` | 11 | `id`(ID)、`jobtitlemark`(职位标识)、`jobtitlename`(职位描述)、`jobtitleremark`(备注) 等共 11 个字段 | [hrmjobtitlestemplet.md](./tables/人力资源/hrmjobtitlestemplet.md) |
| 117 | `hrmjobtype` | 3 | `id`(ID)、`name`(名称)、`description`(描述) | [hrmjobtype.md](./tables/人力资源/hrmjobtype.md) |
| 118 | `hrmkpirevision` | 6 | `id`(ID)、`goalid`(目标id)、`operator`(操作者)、`operatetime`(操作时间) 等共 6 个字段 | [hrmkpirevision.md](./tables/人力资源/hrmkpirevision.md) |
| 119 | `hrmkpirevisiondetail` | 9 | `id`(ID)、`goalid`(系统模板id)、`operator`(操作者)、`operatetime`(操作时间) 等共 9 个字段 | [hrmkpirevisiondetail.md](./tables/人力资源/hrmkpirevisiondetail.md) |
| 120 | `hrmkpirevisionlog` | 27 | `id`(ID)、`goalname`(目标名称)、`objid`(负责单位)、`goalcode`(代码) 等共 27 个字段 | [hrmkpirevisionlog.md](./tables/人力资源/hrmkpirevisionlog.md) |
| 121 | `hrmkqsystemset` | 11 | `tosomeone`(收件人地址)、`timeinterval`(数据采集时间间隔(分钟))、`getdatatype`(数据采集方式)、`getdatavalue`(数据采集所得数据) 等共 11 个字段 | [hrmkqsystemset.md](./tables/人力资源/hrmkqsystemset.md) |
| 122 | `hrmlanguageability` | 4 | `id`(ID)、`resourceid`(人力资源id)、`language`(语种)、`level_n`(级别) | [hrmlanguageability.md](./tables/人力资源/hrmlanguageability.md) |
| 123 | `hrmlistvalidate` | 8 | `tab_label`(标签值)、`id`(ID)、`name`(人力资源功能项目名称)、`validate_n`(是否启用) 等共 8 个字段 | [hrmlistvalidate.md](./tables/人力资源/hrmlistvalidate.md) |
| 124 | `hrmlocations` | 11 | `id`(ID)、`locationname`(地址信息名称)、`locationdesc`(地址信息描述)、`address1`(地址1) 等共 11 个字段 | [hrmlocations.md](./tables/人力资源/hrmlocations.md) |
| 125 | `hrmmessagermsg` | 5 | `id`(ID)、`jidcurrent`(发送者)、`sendto`(接收人)、`msg`(信息) 等共 5 个字段 | [hrmmessagermsg.md](./tables/人力资源/hrmmessagermsg.md) |
| 126 | `hrmmessagersetting` | 3 | `id`(ID)、`name`(服务器名称)、`value`(服务器地址值) | [hrmmessagersetting.md](./tables/人力资源/hrmmessagersetting.md) |
| 127 | `hrmmessagertempmsg` | 5 | `id`(ID)、`loginid`(用户登陆id)、`fromjid`(表单id)、`body`(聊天内容) 等共 5 个字段 | [hrmmessagertempmsg.md](./tables/人力资源/hrmmessagertempmsg.md) |
| 128 | `hrmnetworksegstr` | 7 | `id`(ID)、`inceptipaddress`(起始ip地址)、`endipaddress`(截止ip地址)、`createrid`(创建人id) 等共 7 个字段 | [hrmnetworksegstr.md](./tables/人力资源/hrmnetworksegstr.md) |
| 129 | `hrmonlineavg` | 7 | `id`(ID)、`online_year`(在线时间-年)、`online_month`(在线时间-月)、`online_date`(在线日期) 等共 7 个字段 | [hrmonlineavg.md](./tables/人力资源/hrmonlineavg.md) |
| 130 | `hrmonlinecount` | 7 | `id`(ID)、`online_date`(在线日期)、`online_time`(在线时间)、`online_num`(在线次数) 等共 7 个字段 | [hrmonlinecount.md](./tables/人力资源/hrmonlinecount.md) |
| 131 | `hrmorggroup` | 5 | `id`(ID)、`orggroupname`(群组名称)、`orggroupdesc`(群组描述)、`showorder`(显示顺序) 等共 5 个字段 | [hrmorggroup.md](./tables/人力资源/hrmorggroup.md) |
| 132 | `hrmorggrouprelated` | 10 | `id`(ID)、`orggroupid`(群组id)、`type`(关联类型)、`content`(关联对象) 等共 10 个字段 | [hrmorggrouprelated.md](./tables/人力资源/hrmorggrouprelated.md) |
| 133 | `hrmotherinfotype` | 3 | `id`(ID)、`typename`(种类描述)、`typeremark`(备注) | [hrmotherinfotype.md](./tables/人力资源/hrmotherinfotype.md) |
| 134 | `hrmothersettings` | 16 | `remindperiod`(密码变更提醒周期)、`valid`(密码变更提醒功能是否有效)、`birthremindperiod`(生日提醒周期)、`birthvalid`(生日提醒功能是否有效) 等共 16 个字段 | [hrmothersettings.md](./tables/人力资源/hrmothersettings.md) |
| 135 | `hrmoutinterfacelog` | 3 | `id`(ID)、`memo`(描述)、`created`(创建时间) | [hrmoutinterfacelog.md](./tables/人力资源/hrmoutinterfacelog.md) |
| 136 | `hrmpassword` | 4 | `id`(ID)、`loginid`(登录id)、`password`(密码)、`salt`(加盐) | [hrmpassword.md](./tables/人力资源/hrmpassword.md) |
| 137 | `hrmperformancealert` | 30 | `id`(ID)、`type_a`(类型)、`yearcondition1`(年度提醒开)、`yearcondition2`(年度提醒前后) 等共 30 个字段 | [hrmperformancealert.md](./tables/人力资源/hrmperformancealert.md) |
| 138 | `hrmperformancealertcheck` | 7 | `id`(ID)、`alertname`(提醒流程名称)、`cycle`(提醒周期)、`performancedate`(时间) 等共 7 个字段 | [hrmperformancealertcheck.md](./tables/人力资源/hrmperformancealertcheck.md) |
| 139 | `hrmperformanceappendrule` | 14 | `id`(ID)、`rulename`(规则名称)、`memo`(规则定义)、`conditions`(条件) 等共 14 个字段 | [hrmperformanceappendrule.md](./tables/人力资源/hrmperformanceappendrule.md) |
| 140 | `hrmperformancebeforepoint` | 3 | `id`(ID)、`planid`(计划id)、`point1`(得分) | [hrmperformancebeforepoint.md](./tables/人力资源/hrmperformancebeforepoint.md) |
| 141 | `hrmperformancecheckdetail` | 10 | `id`(ID)、`checkid`(考核表id)、`targetname`(考核叶子节点名称)、`percent_n`(父节点名称) 等共 10 个字段 | [hrmperformancecheckdetail.md](./tables/人力资源/hrmperformancecheckdetail.md) |
| 142 | `hrmperformancecheckflow` | 5 | `id`(ID)、`objid`(对象id)、`objtype`(对象类型)、`goalflowid`(目标审批流程id) 等共 5 个字段 | [hrmperformancecheckflow.md](./tables/人力资源/hrmperformancecheckflow.md) |
| 143 | `hrmperformancecheckpoint` | 16 | `id`(ID)、`cycle`(考核周期)、`checktype`(考核类型)、`checkdate`(考核日期) 等共 16 个字段 | [hrmperformancecheckpoint.md](./tables/人力资源/hrmperformancecheckpoint.md) |
| 144 | `hrmperformancecheckpointdetail` | 12 | `id`(ID)、`checkid`(自定义考核方案id)、`targetname`(名称)、`percent_n`(上级名称) 等共 12 个字段 | [hrmperformancecheckpointdetail.md](./tables/人力资源/hrmperformancecheckpointdetail.md) |
| 145 | `hrmperformancecheckrule` | 4 | `id`(ID)、`rulename`(权重名称)、`memo`(规则定义)、`status`(是否启用) | [hrmperformancecheckrule.md](./tables/人力资源/hrmperformancecheckrule.md) |
| 146 | `hrmperformancecheckscheme` | 12 | `id`(ID)、`schemename`(名称)、`memo`(描述)、`checkbranchid`(考核对象分部id) 等共 12 个字段 | [hrmperformancecheckscheme.md](./tables/人力资源/hrmperformancecheckscheme.md) |
| 147 | `hrmperformancecheckstd` | 4 | `id`(ID)、`checkdetailid`(考核方案id)、`stdname`(指标名称)、`point`(分值) | [hrmperformancecheckstd.md](./tables/人力资源/hrmperformancecheckstd.md) |
| 148 | `hrmperformancecustom` | 4 | `id`(ID)、`unitname`(单位名)、`memo`(描述)、`status`(状态) | [hrmperformancecustom.md](./tables/人力资源/hrmperformancecustom.md) |
| 149 | `hrmperformancediycheckpoint` | 12 | `id`(ID)、`checkid`(考核id)、`targetname`(名称)、`percent_n`(上级名称) 等共 12 个字段 | [hrmperformancediycheckpoint.md](./tables/人力资源/hrmperformancediycheckpoint.md) |
| 150 | `hrmperformanceflow` | 3 | `id`(ID)、`type_1`(所属类型)、`relatingflow`(关联流程id) | [hrmperformanceflow.md](./tables/人力资源/hrmperformanceflow.md) |
| 151 | `hrmperformancegoal` | 27 | `id`(ID)、`goalname`(目标名称)、`objid`(负责单位)、`goalcode`(代码) 等共 27 个字段 | [hrmperformancegoal.md](./tables/人力资源/hrmperformancegoal.md) |
| 152 | `hrmperformancegoalstd` | 4 | `id`(ID)、`goalid`(目标id)、`stdname`(名称)、`point`(分值) | [hrmperformancegoalstd.md](./tables/人力资源/hrmperformancegoalstd.md) |
| 153 | `hrmperformancegrade` | 5 | `id`(ID)、`gradename`(等级名称)、`source`(数据源)、`memo`(描述) 等共 5 个字段 | [hrmperformancegrade.md](./tables/人力资源/hrmperformancegrade.md) |
| 154 | `hrmperformancegradedetail` | 5 | `id`(ID)、`gradeid`(目标id)、`grade`(目标名称)、`condition1`(数据源1) 等共 5 个字段 | [hrmperformancegradedetail.md](./tables/人力资源/hrmperformancegradedetail.md) |
| 155 | `hrmperformancenodepoint` | 13 | `id`(ID)、`cycle`(考核周期)、`reportid`(报告id)、`checktype`(考核类型) 等共 13 个字段 | [hrmperformancenodepoint.md](./tables/人力资源/hrmperformancenodepoint.md) |
| 156 | `hrmperformanceplancheck` | 6 | `id`(ID)、`planmodulid`(计划模板id)、`cycle`(周期)、`plandate`(计划日期) 等共 6 个字段 | [hrmperformanceplancheck.md](./tables/人力资源/hrmperformanceplancheck.md) |
| 157 | `hrmperformanceplandown` | 5 | `id`(ID)、`planid`(计划id)、`objid`(对象id)、`status`(是否启用) 等共 5 个字段 | [hrmperformanceplandown.md](./tables/人力资源/hrmperformanceplandown.md) |
| 158 | `hrmperformanceplaneffort` | 4 | `id`(ID)、`planid`(计划id)、`effortname`(要求名称)、`viewsort`(顺序) | [hrmperformanceplaneffort.md](./tables/人力资源/hrmperformanceplaneffort.md) |
| 159 | `hrmperformanceplaneffortmodul` | 4 | `id`(ID)、`planid`(计划id)、`effortname`(模板名称)、`viewsort`(显示顺序) | [hrmperformanceplaneffortmodul.md](./tables/人力资源/hrmperformanceplaneffortmodul.md) |
| 160 | `hrmperformanceplankey` | 4 | `id`(ID)、`planid`(计划id)、`keyname`(关键点名称)、`viewsort`(显示顺序) | [hrmperformanceplankey.md](./tables/人力资源/hrmperformanceplankey.md) |
| 161 | `hrmperformanceplankeymodul` | 4 | `id`(ID)、`planid`(计划id)、`keyname`(名称)、`viewsort`(显示顺序) | [hrmperformanceplankeymodul.md](./tables/人力资源/hrmperformanceplankeymodul.md) |
| 162 | `hrmperformanceplankind` | 4 | `id`(ID)、`headers`(标题)、`planname`(名称)、`sort`(排序) | [hrmperformanceplankind.md](./tables/人力资源/hrmperformanceplankind.md) |
| 163 | `hrmperformanceplankinddetail` | 5 | `id`(ID)、`planid`(计划id)、`headers`(标题)、`planname`(名称) 等共 5 个字段 | [hrmperformanceplankinddetail.md](./tables/人力资源/hrmperformanceplankinddetail.md) |
| 164 | `hrmperformanceplanmodul` | 72 | `principal`(负责人)、`ruletag`(规则标记)、`ruleregex`(重复规则)、`nextdate`(下一个日期点) 等共 72 个字段 | [hrmperformanceplanmodul.md](./tables/人力资源/hrmperformanceplanmodul.md) |
| 165 | `hrmperformancepointadjust` | 7 | `id`(ID)、`pointid`(计划id)、`content`(内容)、`adjustdate`(修正时间) 等共 7 个字段 | [hrmperformancepointadjust.md](./tables/人力资源/hrmperformancepointadjust.md) |
| 166 | `hrmperformancepointrule` | 6 | `id`(ID)、`minpoint`(最小得分)、`maxpoint`(最大得分)、`pointmethod`(得分方式) 等共 6 个字段 | [hrmperformancepointrule.md](./tables/人力资源/hrmperformancepointrule.md) |
| 167 | `hrmperformancereport` | 13 | `id`(ID)、`reportgroupid`(分组id)、`planid`(计划id)、`objid`(对象id) 等共 13 个字段 | [hrmperformancereport.md](./tables/人力资源/hrmperformancereport.md) |
| 168 | `hrmperformancereportlog` | 7 | `id`(ID)、`reportname`(报告名字)、`reportlog`(报告备注)、`cycle`(考核周期) 等共 7 个字段 | [hrmperformancereportlog.md](./tables/人力资源/hrmperformancereportlog.md) |
| 169 | `hrmperformanceschemecontent` | 5 | `id`(ID)、`schemeid`(考核基本信息表id)、`type_c`(考核类型)、`percent_n`(考核对象) 等共 5 个字段 | [hrmperformanceschemecontent.md](./tables/人力资源/hrmperformanceschemecontent.md) |
| 170 | `hrmperformanceschemedetail` | 5 | `id`(ID)、`contentid`(考核项)、`item`(工作计划)、`checkflow`(workflow_base的id字段) 等共 5 个字段 | [hrmperformanceschemedetail.md](./tables/人力资源/hrmperformanceschemedetail.md) |
| 171 | `hrmperformanceschemepercent` | 7 | `id`(ID)、`itemid`(工作计划id)、`nodeid`(节点id)、`groupid`(分组id) 等共 7 个字段 | [hrmperformanceschemepercent.md](./tables/人力资源/hrmperformanceschemepercent.md) |
| 172 | `hrmperformancetargetdetail` | 13 | `id`(ID)、`targetid`(人力资源指标id)、`targetname`(指标名称)、`targetcode`(指标编码) 等共 13 个字段 | [hrmperformancetargetdetail.md](./tables/人力资源/hrmperformancetargetdetail.md) |
| 173 | `hrmperformancetargetstd` | 4 | `id`(ID)、`targetdetailid`(指标详情id)、`stdname`(名称)、`point`(分数) | [hrmperformancetargetstd.md](./tables/人力资源/hrmperformancetargetstd.md) |
| 174 | `hrmperformancetargettype` | 4 | `id`(ID)、`targetname`(名称)、`memo`(定义)、`num`(数量) | [hrmperformancetargettype.md](./tables/人力资源/hrmperformancetargettype.md) |
| 175 | `hrmperiod` | 3 | `departmentid`(部门id)、`periodyear`(年)、`periodmonth`(月) | [hrmperiod.md](./tables/人力资源/hrmperiod.md) |
| 176 | `hrmplancolor` | 4 | `resourceid`(人力资源id)、`basictype`(类型)、`colorid1`(颜色代码1)、`colorid2`(颜色代码2) | [hrmplancolor.md](./tables/人力资源/hrmplancolor.md) |
| 177 | `hrmprivacysetting` | 7 | `id`(ID)、`fieldid`(字段ID)、`fieldname`(字段名)、`fieldlabel`(字段显示名) 等共 7 个字段 | [hrmprivacysetting.md](./tables/人力资源/hrmprivacysetting.md) |
| 178 | `hrmprovince` | 5 | `id`(ID)、`provincename`(省份名称)、`provincedesc`(省份描述)、`countryid`(国家id) 等共 5 个字段 | [hrmprovince.md](./tables/人力资源/hrmprovince.md) |
| 179 | `hrmpslbatchprocess` | 5 | `id`(ID)、`workingage`(工龄)、`psldays`(天数)、`subcompanyid`(分部id) 等共 5 个字段 | [hrmpslbatchprocess.md](./tables/人力资源/hrmpslbatchprocess.md) |
| 180 | `hrmpslmanagement` | 6 | `id`(ID)、`resourceid`(人员id)、`pslyear`(有效期年)、`psldays`(有效期天) 等共 6 个字段 | [hrmpslmanagement.md](./tables/人力资源/hrmpslmanagement.md) |
| 181 | `hrmpslperiod` | 6 | `id`(ID)、`pslyear`(有效期年份)、`startdate`(开始日期)、`enddate`(结束日期) 等共 6 个字段 | [hrmpslperiod.md](./tables/人力资源/hrmpslperiod.md) |
| 182 | `hrmpubholiday` | 6 | `id`(ID)、`countryid`(所在国家id)、`holidaydate`(公众假日)、`holidayname`(公众假日描述) 等共 6 个字段 | [hrmpubholiday.md](./tables/人力资源/hrmpubholiday.md) |
| 183 | `hrmrefuseavg` | 6 | `id`(ID)、`refuse_date`(拒绝日期)、`refuse_year`(拒绝时间年份)、`refuse_month`(月份) 等共 6 个字段 | [hrmrefuseavg.md](./tables/人力资源/hrmrefuseavg.md) |
| 184 | `hrmrefusecount` | 6 | `id`(ID)、`refuse_date`(拒绝日期)、`refuse_year`(年份)、`refuse_month`(月份) 等共 6 个字段 | [hrmrefusecount.md](./tables/人力资源/hrmrefusecount.md) |
| 185 | `hrmremindhistory` | 3 | `type`(类型)、`reminddate`(提醒时间)、`remindedresourceid`(人员id) | [hrmremindhistory.md](./tables/人力资源/hrmremindhistory.md) |
| 186 | `hrmremindmsg` | 5 | `id`(ID)、`remindtype`(提醒类型)、`resourceid`(人员id)、`reminddate`(提醒日期) 等共 5 个字段 | [hrmremindmsg.md](./tables/人力资源/hrmremindmsg.md) |
| 187 | `hrmresource` | 24 | `haschangepwd`(密码是否已经改过)、`created`(创建时间)、`creater`(创建人id)、`modified`(修改时间) 等共 24 个字段 | [hrmresource.md](./tables/人力资源/hrmresource.md) |
| 188 | `hrmresource_online` | 4 | `user_id`(人员id)、`date_time`(时间戳)、`online_flag`(人员在线标识)、`serverip`(服务地址IP) | [hrmresource_online.md](./tables/人力资源/hrmresource_online.md) |
| 189 | `hrmresource_trigger` | 6 | `id`(ID)、`managerid`(经理id)、`departmentid`(部门id)、`subcompanyid1`(分部id) 等共 6 个字段 | [hrmresource_trigger.md](./tables/人力资源/hrmresource_trigger.md) |
| 190 | `hrmresourcebasetab` | 10 | `id`(ID)、`groupname`(分组名称)、`grouplabel`(分组label)、`dsporder`(序列号) 等共 10 个字段 | [hrmresourcebasetab.md](./tables/人力资源/hrmresourcebasetab.md) |
| 191 | `hrmresourcecompetency` | 9 | `id`(ID)、`resourceid`(人力资源id)、`competencyid`(技能id)、`lastgrade`(前一次分数) 等共 9 个字段 | [hrmresourcecompetency.md](./tables/人力资源/hrmresourcecompetency.md) |
| 192 | `hrmresourcecomponent` | 19 | `id`(ID)、`resourceid`(人力资源id)、`componentid`(财务要素id)、`componentmark`(详细标识) 等共 19 个字段 | [hrmresourcecomponent.md](./tables/人力资源/hrmresourcecomponent.md) |
| 193 | `hrmresourcefile` | 9 | `id`(ID)、`resourceid`(人员id)、`fieldid`(文件id)、`docid`(文档id) 等共 9 个字段 | [hrmresourcefile.md](./tables/人力资源/hrmresourcefile.md) |
| 194 | `hrmresourcemanager` | 25 | `id`(ID)、`loginid`(系统登陆帐号)、`password`(系统登陆密码)、`firstname`(姓) 等共 25 个字段 | [hrmresourcemanager.md](./tables/人力资源/hrmresourcemanager.md) |
| 195 | `hrmresourceotherinfo` | 13 | `id`(ID)、`resourceid`(人力资源id)、`infoname`(信息主题)、`startdate`(相关起始日期) 等共 13 个字段 | [hrmresourceotherinfo.md](./tables/人力资源/hrmresourceotherinfo.md) |
| 196 | `hrmresourceout` | 12 | `id`(ID)、`resourceid`(人员id)、`wxname`(微信昵称)、`wxopenid`(用户微信) 等共 12 个字段 | [hrmresourceout.md](./tables/人力资源/hrmresourceout.md) |
| 197 | `hrmresourcerpdefine` | 5 | `id`(ID)、`resourceid`(人员id)、`colname`(列名)、`showorder`(显示顺序) 等共 5 个字段 | [hrmresourcerpdefine.md](./tables/人力资源/hrmresourcerpdefine.md) |
| 198 | `hrmresourceselectrecord` | 3 | `id`(ID)、`selectid`(所选人员id)、`resourceid`(登录人id) | [hrmresourceselectrecord.md](./tables/人力资源/hrmresourceselectrecord.md) |
| 199 | `hrmresourceskill` | 3 | `id`(ID)、`resourceid`(人力资源id)、`skilldesc`(技能描述) | [hrmresourceskill.md](./tables/人力资源/hrmresourceskill.md) |
| 200 | `hrmresourcetemp` | 117 | `textfield5`(自定义文本5)、`tinyintfield1`(自定义判断1)、`tinyintfield2`(自定义判断2)、`tinyintfield3`(自定义判断3) 等共 117 个字段 | [hrmresourcetemp.md](./tables/人力资源/hrmresourcetemp.md) |
| 201 | `hrmresourcevirtual` | 7 | `id`(ID)、`resourceid`(人员id)、`managerid`(上级id)、`subcompanyid`(分部id) 等共 7 个字段 | [hrmresourcevirtual.md](./tables/人力资源/hrmresourcevirtual.md) |
| 202 | `hrmrewardbeforework` | 5 | `id`(ID)、`resourceid`(人力资源id)、`rewardname`(奖励名称)、`rewarddate`(奖励时间) 等共 5 个字段 | [hrmrewardbeforework.md](./tables/人力资源/hrmrewardbeforework.md) |
| 203 | `hrmrewardsrecord` | 11 | `id`(ID)、`resourceid`(人力资源id)、`rewardsdate`(奖惩时间)、`rewardstype`(奖惩类型) 等共 11 个字段 | [hrmrewardsrecord.md](./tables/人力资源/hrmrewardsrecord.md) |
| 204 | `hrmrewardstype` | 2 | `id`(ID)、`flag`(奖惩类别) | [hrmrewardstype.md](./tables/人力资源/hrmrewardstype.md) |
| 205 | `hrmrightcardinfo` | 7 | `id`(ID)、`resourceid`(人员id)、`carddate`(打卡日期)、`cardtime`(打卡时间) 等共 7 个字段 | [hrmrightcardinfo.md](./tables/人力资源/hrmrightcardinfo.md) |
| 206 | `hrmrolemembers` | 12 | `resourceidbak`(人员id副本)、`resourcetype`(人员类型)、`alllevel`(所有级别)、`seclevelfrom`(级别开始值) 等共 12 个字段 | [hrmrolemembers.md](./tables/人力资源/hrmrolemembers.md) |
| 207 | `hrmrolemembers_tri` | 3 | `roleid`(角色id)、`resourceid`(人力资源id)、`rolelevel`(角色级别) | [hrmrolemembers_tri.md](./tables/人力资源/hrmrolemembers_tri.md) |
| 208 | `hrmroles` | 8 | `id`(ID)、`rolesmark`(角色标识)、`rolesname`(角色描述)、`docid`(相关文档id) 等共 8 个字段 | [hrmroles.md](./tables/人力资源/hrmroles.md) |
| 209 | `hrmroles_module` | 7 | `id`(ID)、`rolesmark`(角色标识)、`rolesname`(角色描述)、`docid`(相关文档id) 等共 7 个字段 | [hrmroles_module.md](./tables/人力资源/hrmroles_module.md) |
| 210 | `hrmrpsubdefine` | 7 | `id`(ID)、`scopeid`(分组id)、`resourceid`(人员id)、`colname`(列表名称) 等共 7 个字段 | [hrmrpsubdefine.md](./tables/人力资源/hrmrpsubdefine.md) |
| 211 | `hrmsalarycalbench` | 3 | `id`(ID)、`itemid`(薪酬设置id)、`scopetype`(公式类型) | [hrmsalarycalbench.md](./tables/人力资源/hrmsalarycalbench.md) |
| 212 | `hrmsalarycalrate` | 7 | `id`(ID)、`benchid`(公式id)、`timescope`(时间范围)、`condition`(条件) 等共 7 个字段 | [hrmsalarycalrate.md](./tables/人力资源/hrmsalarycalrate.md) |
| 213 | `hrmsalarycalscope` | 3 | `itemid`(薪酬设置id)、`benchid`(公式id)、`objectid`(对象id) | [hrmsalarycalscope.md](./tables/人力资源/hrmsalarycalscope.md) |
| 214 | `hrmsalarychange` | 10 | `id`(ID)、`multresourceid`(多人员id)、`itemid`(薪酬设置id)、`changedate`(变更日期) 等共 10 个字段 | [hrmsalarychange.md](./tables/人力资源/hrmsalarychange.md) |
| 215 | `hrmsalarycomponent` | 13 | `id`(ID)、`componentname`(名称)、`countryid`(国家id)、`jobactivityid`(职务id) 等共 13 个字段 | [hrmsalarycomponent.md](./tables/人力资源/hrmsalarycomponent.md) |
| 216 | `hrmsalarycomponentdetail` | 5 | `componentid`(人力资源原有工资类型id)、`detailmark`(明细名称)、`joblevel`(岗位级别)、`salarysum`(工资总金额) 等共 5 个字段 | [hrmsalarycomponentdetail.md](./tables/人力资源/hrmsalarycomponentdetail.md) |
| 217 | `hrmsalarycomponenttypes` | 5 | `id`(ID)、`typemark`(类型描述)、`typename`(类型名称)、`colorid`(类型颜色id) 等共 5 个字段 | [hrmsalarycomponenttypes.md](./tables/人力资源/hrmsalarycomponenttypes.md) |
| 218 | `hrmsalarycreateinfo` | 7 | `id`(ID)、`currentdate`(当前时间)、`salarybegindate`(工资生成开始时间)、`salaryenddate`(工资生成结束时间) 等共 7 个字段 | [hrmsalarycreateinfo.md](./tables/人力资源/hrmsalarycreateinfo.md) |
| 219 | `hrmsalarydiffdetail` | 9 | `itemid`(薪酬设置id)、`resourceid`(被考勤人id)、`payid`(工资id)、`diffid`(考勤id) 等共 9 个字段 | [hrmsalarydiffdetail.md](./tables/人力资源/hrmsalarydiffdetail.md) |
| 220 | `hrmsalaryhistory` | 5 | `id`(ID)、`hrmid`(人员id)、`currentdate`(当前时间)、`itemid`(工资单规则id) 等共 5 个字段 | [hrmsalaryhistory.md](./tables/人力资源/hrmsalaryhistory.md) |
| 221 | `hrmsalaryitem` | 18 | `id`(ID)、`itemname`(薪酬项名称)、`itemcode`(薪酬项代码)、`itemtype`(类型) 等共 18 个字段 | [hrmsalaryitem.md](./tables/人力资源/hrmsalaryitem.md) |
| 222 | `hrmsalarypay` | 3 | `id`(ID)、`paydate`(生成日期)、`isvalidate`(是否发送) | [hrmsalarypay.md](./tables/人力资源/hrmsalarypay.md) |
| 223 | `hrmsalarypaydetail` | 11 | `payid`(工资月份id)、`itemid`(薪酬id)、`hrmid`(人力资源)、`salary`(工资项金额) 等共 11 个字段 | [hrmsalarypaydetail.md](./tables/人力资源/hrmsalarypaydetail.md) |
| 224 | `hrmsalarypaylog` | 10 | `id`(ID)、`changid`(更改人id)、`userid`(用户id)、`changedate`(更改日期) 等共 10 个字段 | [hrmsalarypaylog.md](./tables/人力资源/hrmsalarypaylog.md) |
| 225 | `hrmsalarypersonality` | 4 | `id`(ID)、`itemid`(薪酬id)、`hrmid`(人员id)、`salary`(工资) | [hrmsalarypersonality.md](./tables/人力资源/hrmsalarypersonality.md) |
| 226 | `hrmsalaryrank` | 7 | `id`(ID)、`itemid`(薪酬id)、`jobid`(岗位id)、`joblevelfrom`(职级开始) 等共 7 个字段 | [hrmsalaryrank.md](./tables/人力资源/hrmsalaryrank.md) |
| 227 | `hrmsalaryratebase` | 3 | `id`(ID)、`name`(名称)、`taxrate`(税率) | [hrmsalaryratebase.md](./tables/人力资源/hrmsalaryratebase.md) |
| 228 | `hrmsalaryresourcepay` | 5 | `id`(ID)、`itemid`(薪酬设置项id)、`resourceid`(人员id)、`resourcepay`(金额) 等共 5 个字段 | [hrmsalaryresourcepay.md](./tables/人力资源/hrmsalaryresourcepay.md) |
| 229 | `hrmsalaryschedule` | 3 | `id`(ID)、`itemid`(薪酬id)、`diffid`(关联id) | [hrmsalaryschedule.md](./tables/人力资源/hrmsalaryschedule.md) |
| 230 | `hrmsalaryshiftpay` | 4 | `id`(ID)、`itemid`(薪酬id)、`shiftid`(出勤id)、`shiftpay`(出勤关联金额) | [hrmsalaryshiftpay.md](./tables/人力资源/hrmsalaryshiftpay.md) |
| 231 | `hrmsalarytaxbench` | 4 | `id`(ID)、`itemid`(薪酬id)、`cityid`(城市id)、`taxbenchmark`(描述信息) | [hrmsalarytaxbench.md](./tables/人力资源/hrmsalarytaxbench.md) |
| 232 | `hrmsalarytaxrate` | 7 | `id`(ID)、`benchid`(税收基本信息id)、`ranknum`(税收金额)、`ranklow`(最低纳税金额) 等共 7 个字段 | [hrmsalarytaxrate.md](./tables/人力资源/hrmsalarytaxrate.md) |
| 233 | `hrmsalarytaxscope` | 4 | `itemid`(薪酬id)、`benchid`(税收信息id)、`scopetype`(类型)、`objectid`(对象id) | [hrmsalarytaxscope.md](./tables/人力资源/hrmsalarytaxscope.md) |
| 234 | `hrmsalarywelfarerate` | 5 | `id`(ID)、`itemid`(薪酬id)、`cityid`(城市id)、`personwelfarerate`(个人费率) 等共 5 个字段 | [hrmsalarywelfarerate.md](./tables/人力资源/hrmsalarywelfarerate.md) |
| 235 | `hrmschedule` | 32 | `id`(ID)、`relatedid`(相关的id)、`monstarttime1`(星期1上午开始时间)、`monendtime1`(星期1上午结束时间) 等共 32 个字段 | [hrmschedule.md](./tables/人力资源/hrmschedule.md) |
| 236 | `hrmscheduleapplication` | 4 | `onedayworkhours`(一天工作时间)、`id`(ID)、`unit`(单位)、`type`(类型) | [hrmscheduleapplication.md](./tables/人力资源/hrmscheduleapplication.md) |
| 237 | `hrmschedulediff` | 15 | `id`(ID)、`diffname`(考勤种类名称)、`diffdesc`(考勤种类描述)、`difftype`(非一致种类) 等共 15 个字段 | [hrmschedulediff.md](./tables/人力资源/hrmschedulediff.md) |
| 238 | `hrmschedulemaintance` | 16 | `id`(ID)、`diffid`(考勤种类id)、`resourceid`(人力资源id)、`startdate`(开始日期) 等共 16 个字段 | [hrmschedulemaintance.md](./tables/人力资源/hrmschedulemaintance.md) |
| 239 | `hrmschedulemonth` | 5 | `hrmid`(被考勤人id)、`difftype`(考勤种类)、`hours`(考勤时间)、`theyear`(年度) 等共 5 个字段 | [hrmschedulemonth.md](./tables/人力资源/hrmschedulemonth.md) |
| 240 | `hrmschedulesignset` | 11 | `datasourceid`(来源id)、`importtype`(导入类型)、`tablename`(数据表名称)、`workcode`(编号) 等共 11 个字段 | [hrmschedulesignset.md](./tables/人力资源/hrmschedulesignset.md) |
| 241 | `hrmsearchmould` | 70 | `column_0_148`(无)、`column_0_149`(无)、`column_0_165`(无)、`column_0_147`(无) 等共 70 个字段 | [hrmsearchmould.md](./tables/人力资源/hrmsearchmould.md) |
| 242 | `hrmsettings` | 86 | `congratulation`(生日祝词)、`usercode`(用户代码)、`brithalarmscope`(提醒范围)、`congratulation1`(生日祝词(弹窗)) 等共 86 个字段 | [hrmsettings.md](./tables/人力资源/hrmsettings.md) |
| 243 | `hrmsex` | 2 | `id`(ID)、`sexname`(性别名称) | [hrmsex.md](./tables/人力资源/hrmsex.md) |
| 244 | `hrmshare` | 2 | `hrmid`(授权人 id)、`applyid`(应聘人员id) | [hrmshare.md](./tables/人力资源/hrmshare.md) |
| 245 | `hrmspeciality` | 3 | `id`(ID)、`name`(名称)、`description`(描述) | [hrmspeciality.md](./tables/人力资源/hrmspeciality.md) |
| 246 | `hrmstatushistory` | 27 | `id`(ID)、`resourceid`(人力资源id)、`changedate`(调整生效日期)、`changeenddate`(调整截至日期) 等共 27 个字段 | [hrmstatushistory.md](./tables/人力资源/hrmstatushistory.md) |
| 247 | `hrmsubcompany` | 18 | `created`(创建时间)、`creater`(创建人)、`modified`(修改时间)、`modifier`(修改人) 等共 18 个字段 | [hrmsubcompany.md](./tables/人力资源/hrmsubcompany.md) |
| 248 | `hrmsubcompanyvirtual` | 11 | `id`(ID)、`subcompanyname`(分部名称)、`subcompanycode`(分部编码)、`subcompanydesc`(分部描述) 等共 11 个字段 | [hrmsubcompanyvirtual.md](./tables/人力资源/hrmsubcompanyvirtual.md) |
| 249 | `hrmsynprivacysetting` | 7 | `id`(ID)、`fieldid`(字段id)、`fieldname`(字段名)、`fieldlabel`(字段标签) 等共 7 个字段 | [hrmsynprivacysetting.md](./tables/人力资源/hrmsynprivacysetting.md) |
| 250 | `hrmsysmaintenancelog` | 13 | `id`(ID)、`relatedid`(相关id)、`relatedname`(相关名称)、`operatetype`(操作类型) 等共 13 个字段 | [hrmsysmaintenancelog.md](./tables/人力资源/hrmsysmaintenancelog.md) |
| 251 | `hrmtimecardinfo` | 5 | `resourceid`(用户id)、`timecarddate`(打卡时间)、`intime`(签到时间)、`outtime`(签退时间) 等共 5 个字段 | [hrmtimecardinfo.md](./tables/人力资源/hrmtimecardinfo.md) |
| 252 | `hrmtimecarduser` | 2 | `resourceid`(用户id)、`usercode`(用户编码) | [hrmtimecarduser.md](./tables/人力资源/hrmtimecarduser.md) |
| 253 | `hrmtrain` | 17 | `id`(ID)、`name`(名称)、`planid`(培训计划id)、`organizer`(组织人) 等共 17 个字段 | [hrmtrain.md](./tables/人力资源/hrmtrain.md) |
| 254 | `hrmtrainactor` | 4 | `id`(ID)、`resourceid`(人员id)、`traindayid`(培训信息id)、`isattend`(是否参加) | [hrmtrainactor.md](./tables/人力资源/hrmtrainactor.md) |
| 255 | `hrmtrainassess` | 6 | `id`(ID)、`trainid`(培训信息id)、`resourceid`(人员id)、`assessdate`(培训评估日期) 等共 6 个字段 | [hrmtrainassess.md](./tables/人力资源/hrmtrainassess.md) |
| 256 | `hrmtrainbeforework` | 7 | `id`(ID)、`resourceid`(人员id)、`trainname`(培训名称)、`trainresource`(培训单位) 等共 7 个字段 | [hrmtrainbeforework.md](./tables/人力资源/hrmtrainbeforework.md) |
| 257 | `hrmtrainday` | 9 | `id`(ID)、`trainid`(培训信息id)、`traindate`(培训日期)、`daytraincontent`(培训日程内容) 等共 9 个字段 | [hrmtrainday.md](./tables/人力资源/hrmtrainday.md) |
| 258 | `hrmtrainlayout` | 9 | `id`(ID)、`layoutname`(规划名称)、`typeid`(培训类型id)、`layoutstartdate`(开始日期) 等共 9 个字段 | [hrmtrainlayout.md](./tables/人力资源/hrmtrainlayout.md) |
| 259 | `hrmtrainlayoutassess` | 7 | `id`(ID)、`layoutid`(培训信息id)、`assessorid`(考官id)、`assessdate`(考评日期) 等共 7 个字段 | [hrmtrainlayoutassess.md](./tables/人力资源/hrmtrainlayoutassess.md) |
| 260 | `hrmtrainplan` | 17 | `id`(ID)、`planname`(名称)、`layoutid`(培训规划id)、`planorganizer`(培训安排组织人) 等共 17 个字段 | [hrmtrainplan.md](./tables/人力资源/hrmtrainplan.md) |
| 261 | `hrmtrainplanday` | 7 | `id`(ID)、`planid`(培训安排id)、`plandate`(培训日期)、`plandaycontent`(培训安排内容) 等共 7 个字段 | [hrmtrainplanday.md](./tables/人力资源/hrmtrainplanday.md) |
| 262 | `hrmtrainplanrange` | 6 | `id`(ID)、`planid`(计划id)、`type_n`(培训公开范围类型)、`resourceid`(人力资源) 等共 6 个字段 | [hrmtrainplanrange.md](./tables/人力资源/hrmtrainplanrange.md) |
| 263 | `hrmtrainrecord` | 8 | `id`(ID)、`resourceid`(人员id)、`trainstartdate`(培训开始时间)、`trainenddate`(培训结束时间) 等共 8 个字段 | [hrmtrainrecord.md](./tables/人力资源/hrmtrainrecord.md) |
| 264 | `hrmtrainresource` | 6 | `id`(ID)、`name`(名称)、`type_n`(类型)、`fare`(费用) 等共 6 个字段 | [hrmtrainresource.md](./tables/人力资源/hrmtrainresource.md) |
| 265 | `hrmtraintest` | 7 | `id`(ID)、`trainid`(培训信息id)、`resourceid`(人员id)、`testdate`(考核日期) 等共 7 个字段 | [hrmtraintest.md](./tables/人力资源/hrmtraintest.md) |
| 266 | `hrmtraintype` | 8 | `typeaim`(目标)、`typedocurl`(文档url)、`typetesturl`(考核url)、`typeoperator`(负责人) 等共 8 个字段 | [hrmtraintype.md](./tables/人力资源/hrmtraintype.md) |
| 267 | `hrmusedemand` | 12 | `id`(ID)、`demandjobtitle`(岗位)、`demandnum`(数量)、`demandkind`(用工性质) 等共 12 个字段 | [hrmusedemand.md](./tables/人力资源/hrmusedemand.md) |
| 268 | `hrmusekind` | 3 | `id`(ID)、`name`(名称)、`description`(描述) | [hrmusekind.md](./tables/人力资源/hrmusekind.md) |
| 269 | `hrmusergroupstatictics` | 4 | `id`(ID)、`userid`(人员id)、`groupid`(分组id)、`clickcnt`(点击次数) | [hrmusergroupstatictics.md](./tables/人力资源/hrmusergroupstatictics.md) |
| 270 | `hrmusermenustatictics` | 4 | `id`(ID)、`userid`(用户id)、`menuid`(菜单id)、`clickcnt`(点击次数) | [hrmusermenustatictics.md](./tables/人力资源/hrmusermenustatictics.md) |
| 271 | `hrmvalidatecardinfo` | 6 | `id`(ID)、`stationid`(打卡机号)、`carddate`(打卡日期)、`cardtime`(打开时间) 等共 6 个字段 | [hrmvalidatecardinfo.md](./tables/人力资源/hrmvalidatecardinfo.md) |
| 272 | `hrmwelfare` | 16 | `id`(ID)、`resourceid`(人员id)、`datefrom`(开始时间)、`dateto`(结束时间) 等共 16 个字段 | [hrmwelfare.md](./tables/人力资源/hrmwelfare.md) |
| 273 | `hrmworkresume` | 8 | `id`(ID)、`resourceid`(人力资源id)、`startdate`(开始时间)、`enddate`(结束时间) 等共 8 个字段 | [hrmworkresume.md](./tables/人力资源/hrmworkresume.md) |
| 274 | `hrmworkresumein` | 13 | `lastmoddate`(最后修改日期)、`lastmodtime`(最后修改时间)、`id`(ID)、`resourceid`(人力资源id) 等共 13 个字段 | [hrmworkresumein.md](./tables/人力资源/hrmworkresumein.md) |
| 275 | `hrmworktimecount` | 5 | `id`(ID)、`resourceid`(人力资源id)、`workdate`(工作日期)、`shiftid`(排班信息id) 等共 5 个字段 | [hrmworktimecount.md](./tables/人力资源/hrmworktimecount.md) |
| 276 | `hrmworktimewarp` | 11 | `id`(ID)、`diffid`(人力资源考勤id)、`resourceid`(人力资源id)、`diffdate`(日期) 等共 11 个字段 | [hrmworktimewarp.md](./tables/人力资源/hrmworktimewarp.md) |
| 277 | `kq_fixedschedulce` | 5 | `id`(主键ID)、`weekday`(星期几)、`serialid`(班次)、`groupid`(考勤组) 等共 5 个字段 | [kq_fixedschedulce.md](./tables/人力资源/kq_fixedschedulce.md) |
| 278 | `kq_format_detail` | 26 | `resourceid`(人员ID)、`kqdate`(考勤日期)、`groupid`(考勤组ID)、`serialid`(班次ID) 等共 26 个字段 | [kq_format_detail.md](./tables/人力资源/kq_format_detail.md) |
| 279 | `kq_format_pool` | 5 | `id`(主键ID)、`resourceid`(人员ID)、`kqdate`(考勤日期)、`status`(状态) 等共 5 个字段 | [kq_format_pool.md](./tables/人力资源/kq_format_pool.md) |
| 280 | `kq_format_total` | 26 | `resourceid`(人员ID)、`kqdate`(考勤日期)、`subcompanyid`(分部ID)、`departmentid`(部门ID) 等共 26 个字段 | [kq_format_total.md](./tables/人力资源/kq_format_total.md) |
| 281 | `kq_group` | 22 | `id`(主键ID)、`groupname`(组名称)、`subcompanyid`(所属分部)、`kqtype`(考勤组类型) 等共 22 个字段 | [kq_group.md](./tables/人力资源/kq_group.md) |
| 282 | `kq_groupmember` | 10 | `id`(主键ID)、`type`(成员类型)、`typevalue`(成员类型值)、`alllevel`(包含下级) 等共 10 个字段 | [kq_groupmember.md](./tables/人力资源/kq_groupmember.md) |
| 283 | `kq_location` | 6 | `id`(主键ID)、`locationname`(办公地点名称)、`longitude`(经度)、`latitude`(纬度) 等共 6 个字段 | [kq_location.md](./tables/人力资源/kq_location.md) |
| 284 | `kq_report_check` | 2 | `id`(主键ID)、`check_date`(执行日期) | [kq_report_check.md](./tables/人力资源/kq_report_check.md) |
| 285 | `kq_report_field` | 12 | `id`(主键ID)、`fieldname`(字段名)、`fieldlabel`(字段显示名)、`width`(列宽) 等共 12 个字段 | [kq_report_field.md](./tables/人力资源/kq_report_field.md) |
| 286 | `kq_shiftschedule` | 6 | `id`(主键ID)、`kqdate`(考勤日期)、`serialid`(班次ID)、`resourceid`(人员ID) 等共 6 个字段 | [kq_shiftschedule.md](./tables/人力资源/kq_shiftschedule.md) |
| 287 | `kq_wifi` | 4 | `id`(主键ID)、`wifiname`(wifi名称)、`mac`(mac地址)、`groupid`(考勤组ID) | [kq_wifi.md](./tables/人力资源/kq_wifi.md) |
| 288 | `matrixfieldinfo` | 10 | `id`(ID)、`matrixid`(矩阵id)、`browsertypeid`(浏览按钮类型id)、`browservalue`(浏览按钮值) 等共 10 个字段 | [matrixfieldinfo.md](./tables/人力资源/matrixfieldinfo.md) |
| 289 | `matrixinfo` | 8 | `id`(ID)、`name`(名称)、`descr`(描述)、`priority`(优先级) 等共 8 个字段 | [matrixinfo.md](./tables/人力资源/matrixinfo.md) |
| 290 | `matrixinit` | 3 | `id`(ID)、`deptinit`(部门初始化)、`companyinit`(分部初始化) | [matrixinit.md](./tables/人力资源/matrixinit.md) |
| 291 | `matrixmaintinfo` | 10 | `id`(ID)、`matrixid`(矩阵id)、`type`(类型)、`resourceid`(人员id) 等共 10 个字段 | [matrixmaintinfo.md](./tables/人力资源/matrixmaintinfo.md) |
| 292 | `subcompanydefinefield` | 17 | `id`(ID)、`billid`(对应流程id)、`fieldname`(字段名称)、`fieldlabel`(字段label id) 等共 17 个字段 | [subcompanydefinefield.md](./tables/人力资源/subcompanydefinefield.md) |
| 293 | `sysrolesubcomright` | 4 | `id`(ID)、`roleid`(角色id)、`subcompanyid`(分部id)、`rightlevel`(操作级别) | [sysrolesubcomright.md](./tables/人力资源/sysrolesubcomright.md) |
| 294 | `t_inputreporthrm` | 6 | `id`(ID)、`inprepid`(报表id)、`crmid`(客户id)、`hrmid`(人员id) 等共 6 个字段 | [t_inputreporthrm.md](./tables/人力资源/t_inputreporthrm.md) |
| 295 | `t_inputreporthrmfields` | 3 | `id`(ID)、`reporthrmid`(报表id)、`fieldid`(字段id) | [t_inputreporthrmfields.md](./tables/人力资源/t_inputreporthrmfields.md) |

### 工作流程

> 本模块共收录 `236` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `shareinnerwfcreate` | 7 | `id`(ID)、`gid`(操作者明细表id)、`workflowid`(流程id)、`content`(相关对象id) 等共 7 个字段 | [shareinnerwfcreate.md](./tables/工作流程/shareinnerwfcreate.md) |
| 2 | `user_defaultorder_setting` | 8 | `id`(id)、`userid`(用户uid)、`usertype`(用户类型)、`columnkey`(列键名) 等共 8 个字段 | [user_defaultorder_setting.md](./tables/工作流程/user_defaultorder_setting.md) |
| 3 | `wfnodegeneralmode` | 6 | `id`(ID)、`modename`(模块名称)、`formid`(表单id)、`isbill`(是否单据) 等共 6 个字段 | [wfnodegeneralmode.md](./tables/工作流程/wfnodegeneralmode.md) |
| 4 | `workflow_addinoperate` | 19 | `operateorder`(顺序)、`isdisable`(是否启用)、`drawbackflag`(退回触发)、`id`(ID) 等共 19 个字段 | [workflow_addinoperate.md](./tables/工作流程/workflow_addinoperate.md) |
| 5 | `workflow_agent` | 23 | `agentid`(代理id)、`workflowid`(工作流id)、`beagenterid`(被代理人)、`agenterid`(代理人) 等共 23 个字段 | [workflow_agent.md](./tables/工作流程/workflow_agent.md) |
| 6 | `workflow_agentconditionset` | 29 | `agentid`(代理id主键)、`bagentuid`(被代理人)、`agentuid`(代理人)、`id`(ID) 等共 29 个字段 | [workflow_agentconditionset.md](./tables/工作流程/workflow_agentconditionset.md) |
| 7 | `workflow_agentpersons` | 4 | `requestid`(请求id)、`receivedpersons`(依次会签的操作人id)、`groupdetailid`(操作组实际i)、`coadjutants`(依次会签的协办人id) | [workflow_agentpersons.md](./tables/工作流程/workflow_agentpersons.md) |
| 8 | `workflow_agenttemplate` | 11 | `id`(id)、`name`(名字)、`beagenterid`(被代理人id)、`agenterid`(代理人id) 等共 11 个字段 | [workflow_agenttemplate.md](./tables/工作流程/workflow_agenttemplate.md) |
| 9 | `workflow_approveerrorlog` | 4 | `requestid`(请求ID)、`nodeid`(节点ID)、`operator`(操作人)、`errorremark`(提交报错messagecontent内容) | [workflow_approveerrorlog.md](./tables/工作流程/workflow_approveerrorlog.md) |
| 10 | `workflow_approvelog` | 6 | `requestid`(请求ID)、`nodeid`(节点ID)、`operator`(操作者)、`remark`(意见内容) 等共 6 个字段 | [workflow_approvelog.md](./tables/工作流程/workflow_approvelog.md) |
| 11 | `workflow_barcodeset` | 11 | `id`(ID)、`workflowid`(工作流id)、`isuse`(是否启用)、`measureunit`(单位) 等共 11 个字段 | [workflow_barcodeset.md](./tables/工作流程/workflow_barcodeset.md) |
| 12 | `workflow_barcodesetdetail` | 4 | `id`(ID)、`barcodesetid`(二维条码设置id)、`dataelementid`(数据元素id)、`fieldid`(字段id) | [workflow_barcodesetdetail.md](./tables/工作流程/workflow_barcodesetdetail.md) |
| 13 | `workflow_base` | 135 | `isshowsrc`(显示意见来源)、`sendtomessagetype`(消息类型)、`islockworkflow`(流程锁定)、`limitvalue`(限制附件上传格式) 等共 135 个字段 | [workflow_base.md](./tables/工作流程/workflow_base.md) |
| 14 | `workflow_bdf_config` | 4 | `browsertype`(浏览按钮类型)、`hasadvancecondition`(是否含有高级搜索)、`hassetdataranage`(是否含有数据范围限定)、`hassettab`(是否含有设置tab) | [workflow_bdf_config.md](./tables/工作流程/workflow_bdf_config.md) |
| 15 | `workflow_bdf_dataranage` | 14 | `id`(ID)、`workflowid`(流程ID)、`fieldid`(字段ID)、`type`(类型) 等共 14 个字段 | [workflow_bdf_dataranage.md](./tables/工作流程/workflow_bdf_dataranage.md) |
| 16 | `workflow_bdf_dr_matrix` | 3 | `dataranageid`(外键Id)、`matrix`(矩阵ID)、`value_field`(取值字段) | [workflow_bdf_dr_matrix.md](./tables/工作流程/workflow_bdf_dr_matrix.md) |
| 17 | `workflow_bdf_dr_matrixdetail` | 5 | `dataranageid`(主表id)、`condition_field`(条件字段id)、`workflow_field`(字段id)、`workflow_objid`(objid) 等共 5 个字段 | [workflow_bdf_dr_matrixdetail.md](./tables/工作流程/workflow_bdf_dr_matrixdetail.md) |
| 18 | `workflow_bdf_tab` | 6 | `workflowid`(流程ID)、`fieldid`(字段ID)、`tabkey`(浏览框tab唯一key)、`showtab`(是否显示) 等共 6 个字段 | [workflow_bdf_tab.md](./tables/工作流程/workflow_bdf_tab.md) |
| 19 | `workflow_bill` | 17 | `clazz`(系统单据继承类)、`id`(ID)、`namelabel`(单据显示名称)、`tablename`(对应的主表名称) 等共 17 个字段 | [workflow_bill.md](./tables/工作流程/workflow_bill.md) |
| 20 | `workflow_billdetailtable` | 5 | `id`(ID)、`billid`(单号id)、`tablename`(表名)、`title`(标题) 等共 5 个字段 | [workflow_billdetailtable.md](./tables/工作流程/workflow_billdetailtable.md) |
| 21 | `workflow_billfield` | 7 | `fieldshowtypes`(显示类型)、`id`(ID)、`billid`(单据id)、`fieldname`(数据库表字段名称) 等共 7 个字段 | [workflow_billfield.md](./tables/工作流程/workflow_billfield.md) |
| 22 | `workflow_billfunctionlist` | 4 | `billid`(单据id)、`indaffirmance`(是否支持提交确认)、`indmouldtype`(是否支持图形化)、`indshowchart`(是否支持提交后显示流程图) | [workflow_billfunctionlist.md](./tables/工作流程/workflow_billfunctionlist.md) |
| 23 | `workflow_browdef` | 5 | `workflowid`(流程id)、`fieldid`(字段id)、`viewtype`(字段种类)、`fieldtype`(字段类型) 等共 5 个字段 | [workflow_browdef.md](./tables/工作流程/workflow_browdef.md) |
| 24 | `workflow_browdef_field` | 10 | `configid`(配置id)、`workflowid`(流程id)、`fieldid`(字段id)、`viewtype`(字段种类) 等共 10 个字段 | [workflow_browdef_field.md](./tables/工作流程/workflow_browdef_field.md) |
| 25 | `workflow_browdef_fieldconf` | 10 | `id`(ID)、`fieldtype`(字段类型)、`fieldname`(字段名称)、`namelabel`(标签名称) 等共 10 个字段 | [workflow_browdef_fieldconf.md](./tables/工作流程/workflow_browdef_fieldconf.md) |
| 26 | `workflow_browdef_selitemconf` | 8 | `configid`(配置id)、`namelabel`(标签名称)、`value`(值)、`showorder`(显示顺序) 等共 8 个字段 | [workflow_browdef_selitemconf.md](./tables/工作流程/workflow_browdef_selitemconf.md) |
| 27 | `workflow_browsertype` | 6 | `labelid`(标签ID)、`id`(ID)、`labelname`(标签名称)、`useable`(是否可用) 等共 6 个字段 | [workflow_browsertype.md](./tables/工作流程/workflow_browsertype.md) |
| 28 | `workflow_browserurl` | 11 | `id`(ID)、`labelid`(浏览框显示名称)、`fielddbtype`(数据库表字段类型)、`browserurl`(页面链接url) 等共 11 个字段 | [workflow_browserurl.md](./tables/工作流程/workflow_browserurl.md) |
| 29 | `workflow_coadjutant` | 7 | `requestid`(请求id)、`organizedid`(抄送人)、`coadjutantid`(协办人)、`issubmitdesc`(主办人提交前协办人可提交意见) 等共 7 个字段 | [workflow_coadjutant.md](./tables/工作流程/workflow_coadjutant.md) |
| 30 | `workflow_code` | 7 | `formid`(表单/单据id)、`flowid`(流程id)、`codefieldid`(编号字段id)、`isuse`(是否起用) 等共 7 个字段 | [workflow_code.md](./tables/工作流程/workflow_code.md) |
| 31 | `workflow_codedetail` | 6 | `mainid`(主表id)、`showid`(编号规则显示内容)、`codevalue`(编号规则的值)、`codeorder`(编号规则排序) 等共 6 个字段 | [workflow_codedetail.md](./tables/工作流程/workflow_codedetail.md) |
| 32 | `workflow_coderegulate` | 10 | `id`(ID)、`formid`(表单id)、`showid`(显示id)、`showtype`(显示类型) 等共 10 个字段 | [workflow_coderegulate.md](./tables/工作流程/workflow_coderegulate.md) |
| 33 | `workflow_codeseq` | 13 | `id`(ID)、`departmentid`(部门id)、`yearid`(年份id)、`sequenceid`(流水号id) 等共 13 个字段 | [workflow_codeseq.md](./tables/工作流程/workflow_codeseq.md) |
| 34 | `workflow_codeseqrecord` | 6 | `id`(ID)、`requestid`(请求id)、`codeseqid`(流程编号流水号表id)、`sequenceid`(参数在sql中的位置) 等共 6 个字段 | [workflow_codeseqrecord.md](./tables/工作流程/workflow_codeseqrecord.md) |
| 35 | `workflow_codeseqreserved` | 7 | `id`(ID)、`codeseqid`(流程编号流水号表id)、`reservedid`(预留号)、`reserveddesc`(预留号描述) 等共 7 个字段 | [workflow_codeseqreserved.md](./tables/工作流程/workflow_codeseqreserved.md) |
| 36 | `workflow_codeset` | 3 | `id`(ID)、`showname`(编号规则显示内容)、`showtype`(编号规则类型) | [workflow_codeset.md](./tables/工作流程/workflow_codeset.md) |
| 37 | `workflow_communicationapprove` | 2 | `contentid`(被点赞内容ID)、`approveuser`(点赞用户) | [workflow_communicationapprove.md](./tables/工作流程/workflow_communicationapprove.md) |
| 38 | `workflow_communicationbase` | 4 | `id`(id)、`requestid`(requestid)、`workflowid`(workflowid)、`communicationname`(交流名称(扩展)) | [workflow_communicationbase.md](./tables/工作流程/workflow_communicationbase.md) |
| 39 | `workflow_communicationcontent` | 18 | `id`(id)、`communicationid`(相关交流主表ID)、`showremark`(显示内容)、`quoteremark`(引用内容) 等共 18 个字段 | [workflow_communicationcontent.md](./tables/工作流程/workflow_communicationcontent.md) |
| 40 | `workflow_communicationmessage` | 5 | `id`(id)、`communicationid`(相关交流主表id)、`contentid`(相关交流内容表id)、`reminduser`(被提醒人) 等共 5 个字段 | [workflow_communicationmessage.md](./tables/工作流程/workflow_communicationmessage.md) |
| 41 | `workflow_communicationquote` | 4 | `id`(id)、`communicationid`(相关交流ID)、`quotecontent`(引用内容ID)、`bequotecontent`(被引用内容ID) | [workflow_communicationquote.md](./tables/工作流程/workflow_communicationquote.md) |
| 42 | `workflow_communicationreadlog` | 3 | `id`(id)、`communicationid`(相关交流主表ID)、`readuser`(读取人) | [workflow_communicationreadlog.md](./tables/工作流程/workflow_communicationreadlog.md) |
| 43 | `workflow_communicationreply` | 8 | `id`(id)、`contentid`(被回复内容id)、`remark`(内容)、`createuser`(创建人) 等共 8 个字段 | [workflow_communicationreply.md](./tables/工作流程/workflow_communicationreply.md) |
| 44 | `workflow_communicationset` | 8 | `doc`(相关文档)、`wf`(相关流程)、`custom`(相关客户)、`project`(相关项目) 等共 8 个字段 | [workflow_communicationset.md](./tables/工作流程/workflow_communicationset.md) |
| 45 | `workflow_config` | 4 | `name`(参数名称)、`des`(参数描述)、`type`(参数所属功能)、`value`(参数值) | [workflow_config.md](./tables/工作流程/workflow_config.md) |
| 46 | `workflow_createflowset` | 6 | `id`(id)、`nodeid`(节点id)、`workflowid`(流程id)、`fieldid`(字段id) 等共 6 个字段 | [workflow_createflowset.md](./tables/工作流程/workflow_createflowset.md) |
| 47 | `workflow_createplan` | 15 | `id`(ID)、`wfid`(工作流id)、`nodeid`(节点id)、`changetime`(转换时间) 等共 15 个字段 | [workflow_createplan.md](./tables/工作流程/workflow_createplan.md) |
| 48 | `workflow_createplandetail` | 6 | `id`(ID)、`createplanid`(workflow_createplan表主键)、`wffieldid`(流程字段id)、`isdetail`(是否明细字段) 等共 6 个字段 | [workflow_createplandetail.md](./tables/工作流程/workflow_createplandetail.md) |
| 49 | `workflow_createplangroup` | 4 | `id`(ID)、`createplanid`(workflow_createplan表主键)、`groupid`(分组id)、`isused`(是否开启转换) | [workflow_createplangroup.md](./tables/工作流程/workflow_createplangroup.md) |
| 50 | `workflow_createtask` | 8 | `id`(ID)、`wfid`(流程id)、`nodeid`(节点id)、`changetime`(转化时间) 等共 8 个字段 | [workflow_createtask.md](./tables/工作流程/workflow_createtask.md) |
| 51 | `workflow_createtaskdetail` | 7 | `id`(ID)、`createtaskid`(创建任务id)、`wffieldid`(流程字段id)、`isdetail`(是否为明细字段) 等共 7 个字段 | [workflow_createtaskdetail.md](./tables/工作流程/workflow_createtaskdetail.md) |
| 52 | `workflow_createtaskgroup` | 4 | `id`(ID)、`createtaskid`(创建任务id)、`groupid`(组id)、`isused`(是否启用) | [workflow_createtaskgroup.md](./tables/工作流程/workflow_createtaskgroup.md) |
| 53 | `workflow_crmcssfile` | 5 | `id`(ID)、`cssname`(css文件显示名)、`realfilename`(css文件在服务器上的名字)、`realpath`(css在服务器上的存储全路径) 等共 5 个字段 | [workflow_crmcssfile.md](./tables/工作流程/workflow_crmcssfile.md) |
| 54 | `workflow_cssdetail` | 22 | `detailid`(id)、`outerbordercolor`(外边框颜色)、`outerbordersize`(外边框宽度)、`requestnamesize`(流程标题字号) 等共 22 个字段 | [workflow_cssdetail.md](./tables/工作流程/workflow_cssdetail.md) |
| 55 | `workflow_currentoperator` | 13 | `isprocessing`(流程异步处理状态)、`processuser`(实际操作人)、`autodate`(无)、`autodatetime`(无) 等共 13 个字段 | [workflow_currentoperator.md](./tables/工作流程/workflow_currentoperator.md) |
| 56 | `workflow_curroperator_dellog` | 40 | `autodate`(参考workflow_curroperator表)、`autodatetime`(参考workflow_curroperator表)、`isbereject`(参考workflow_curroperator表)、`isprocessing`(参考workflow_curroperator表) 等共 40 个字段 | [workflow_curroperator_dellog.md](./tables/工作流程/workflow_curroperator_dellog.md) |
| 57 | `workflow_custfieldname` | 5 | `workflowid`(工作流id)、`nodeid`(节点id)、`languageid`(系统语言)、`fieldname`(类型标识名称) 等共 5 个字段 | [workflow_custfieldname.md](./tables/工作流程/workflow_custfieldname.md) |
| 58 | `workflow_custom` | 8 | `id`(ID)、`formid`(表单/单据id)、`isbill`(是否单据)、`querytypeid`(自定义查询种类) 等共 8 个字段 | [workflow_custom.md](./tables/工作流程/workflow_custom.md) |
| 59 | `workflow_customdspfield` | 7 | `id`(ID)、`customid`(流程自定义查询主明细表id)、`fieldid`(字段id)、`ifquery`(是否作为查询条件) 等共 7 个字段 | [workflow_customdspfield.md](./tables/工作流程/workflow_customdspfield.md) |
| 60 | `workflow_customlevel` | 6 | `id`(编号)、`defaultname`(默认名称)、`customname`(自定义名称)、`isfc`(是否封存) 等共 6 个字段 | [workflow_customlevel.md](./tables/工作流程/workflow_customlevel.md) |
| 61 | `workflow_customquerytype` | 4 | `id`(ID)、`typename`(种类名称)、`typenamemark`(种类说明)、`showorder`(显示顺序) | [workflow_customquerytype.md](./tables/工作流程/workflow_customquerytype.md) |
| 62 | `workflow_customreport` | 10 | `id`(主键ID)、`reportname`(报表名称)、`formid`(表单ID)、`isbill`(单据还是表单) 等共 10 个字段 | [workflow_customreport.md](./tables/工作流程/workflow_customreport.md) |
| 63 | `workflow_customreport_field` | 10 | `reportid`(报表ID)、`fieldid`(字段ID)、`tablename`(字段所属表名)、`isdetail`(是否明细字段) 等共 10 个字段 | [workflow_customreport_field.md](./tables/工作流程/workflow_customreport_field.md) |
| 64 | `workflow_customreport_project` | 8 | `id`(主键ID)、`reportid`(报表ID)、`projectname`(公式名称)、`formula`(公式) 等共 8 个字段 | [workflow_customreport_project.md](./tables/工作流程/workflow_customreport_project.md) |
| 65 | `workflow_customreport_share` | 7 | `id`(主键ID)、`reportid`(报表ID)、`sharetype`(共享类型)、`sharedobj`(共享类型对象ID) 等共 7 个字段 | [workflow_customreport_share.md](./tables/工作流程/workflow_customreport_share.md) |
| 66 | `workflow_customreport_template` | 4 | `id`(主键ID)、`reportid`(报表ID)、`templatename`(模板名称)、`owner`(模板所有者) | [workflow_customreport_template.md](./tables/工作流程/workflow_customreport_template.md) |
| 67 | `workflow_customreport_tfield` | 6 | `templateid`(模板ID)、`fieldid`(字段ID)、`opt1`(第一个下拉框选项)、`value1`(对应值) 等共 6 个字段 | [workflow_customreport_tfield.md](./tables/工作流程/workflow_customreport_tfield.md) |
| 68 | `workflow_datainput_condition` | 5 | `id`(id)、`datainputid`(数据输入id)、`fieldname`(字段名称)、`connection`(连接) 等共 5 个字段 | [workflow_datainput_condition.md](./tables/工作流程/workflow_datainput_condition.md) |
| 69 | `workflow_datainput_entry` | 8 | `isdel`(是否删除已有数据)、`enable`(是否启用)、`id`(ID)、`workflowid`(工作流id) 等共 8 个字段 | [workflow_datainput_entry.md](./tables/工作流程/workflow_datainput_entry.md) |
| 70 | `workflow_datainput_field` | 8 | `conditions`(属于还是等于)、`id`(ID)、`datainputid`(触发表id)、`tableid`(关联数据表id) 等共 8 个字段 | [workflow_datainput_field.md](./tables/工作流程/workflow_datainput_field.md) |
| 71 | `workflow_datainput_main` | 8 | `orderstr`(排序语句)、`condtion`(条件)、`id`(ID)、`entryid`(触发表id) 等共 8 个字段 | [workflow_datainput_main.md](./tables/工作流程/workflow_datainput_main.md) |
| 72 | `workflow_datainput_table` | 5 | `id`(ID)、`datainputid`(触发表id)、`tablename`(关联数据表名)、`alias`(关联数据表名-别名) 等共 5 个字段 | [workflow_datainput_table.md](./tables/工作流程/workflow_datainput_table.md) |
| 73 | `workflow_deptabbr` | 8 | `id`(ID)、`workflowid`(流程id)、`formid`(表单或单据id)、`isbill`(是否单据) 等共 8 个字段 | [workflow_deptabbr.md](./tables/工作流程/workflow_deptabbr.md) |
| 74 | `workflow_deptabbrdef` | 3 | `id`(ID)、`departmentid`(部门id)、`abbr`(简称) | [workflow_deptabbrdef.md](./tables/工作流程/workflow_deptabbrdef.md) |
| 75 | `workflow_dimension` | 16 | `id`(id)、`typeid`(待办维度id)、`typename`(待办维度类型名称)、`typetitle`(待办维度显示名称) 等共 16 个字段 | [workflow_dimension.md](./tables/工作流程/workflow_dimension.md) |
| 76 | `workflow_distributionsummary` | 15 | `id`(ID)、`mainwfid`(主流程id)、`mainformid`(主流程表单id)、`mainfieldid`(主流程字段id) 等共 15 个字段 | [workflow_distributionsummary.md](./tables/工作流程/workflow_distributionsummary.md) |
| 77 | `workflow_docprop` | 6 | `id`(ID)、`workflowid`(流程id)、`selectitemid`(选择框可选项id)、`seccategoryid`(文档子目录id) 等共 6 个字段 | [workflow_docprop.md](./tables/工作流程/workflow_docprop.md) |
| 78 | `workflow_docpropdetail` | 4 | `id`(ID)、`docpropid`(文档属性页设置id)、`docpropfieldid`(文档属性页字段id)、`workflowfieldid`(流程字段id) | [workflow_docpropdetail.md](./tables/工作流程/workflow_docpropdetail.md) |
| 79 | `workflow_docshareinfo` | 8 | `id`(ID)、`docid`(文档id)、`workflowid`(流程id)、`requestid`(请求id) 等共 8 个字段 | [workflow_docshareinfo.md](./tables/工作流程/workflow_docshareinfo.md) |
| 80 | `workflow_docsource` | 7 | `id`(ID)、`requestid`(请求id)、`nodeid`(节点id)、`fieldid`(字段id) 等共 7 个字段 | [workflow_docsource.md](./tables/工作流程/workflow_docsource.md) |
| 81 | `workflow_encrypt_datas` | 11 | `id`(主键)、`requestid`(请求id)、`logid`(日志id)、`configstr`(配置信息) 等共 11 个字段 | [workflow_encrypt_datas.md](./tables/工作流程/workflow_encrypt_datas.md) |
| 82 | `workflow_fielddata_cache` | 6 | `id`(ID)、`requestid`(请求ID)、`fieldid`(字段ID)、`detailid`(明细ID) 等共 6 个字段 | [workflow_fielddata_cache.md](./tables/工作流程/workflow_fielddata_cache.md) |
| 83 | `workflow_fielddata_cache_prop` | 3 | `openrefreshthread`(开启表单自定义浏览框数据缓存)、`refreshtimeinterval`(线程执行间隔)、`openreqfromcache`(开启表单自定义浏览框数据缓存) | [workflow_fielddata_cache_prop.md](./tables/工作流程/workflow_fielddata_cache_prop.md) |
| 84 | `workflow_fieldlable` | 5 | `formid`(表单id)、`fieldid`(表单字段id)、`fieldlable`(表单字段显示名)、`langurageid`(显示语言) 等共 5 个字段 | [workflow_fieldlable.md](./tables/工作流程/workflow_fieldlable.md) |
| 85 | `workflow_fieldtrans` | 3 | `id`(ID)、`typename`(简介)、`classname`(需要反射的类) | [workflow_fieldtrans.md](./tables/工作流程/workflow_fieldtrans.md) |
| 86 | `workflow_fieldtype` | 7 | `id`(ID)、`typename`(字段显示名)、`namelabel`(字段显示名的标签id)、`classname`(流程字段html代码生成类) 等共 7 个字段 | [workflow_fieldtype.md](./tables/工作流程/workflow_fieldtype.md) |
| 87 | `workflow_fieldyear` | 4 | `id`(ID)、`yearid`(年id)、`yearname`(年名称)、`yeardesc`(年描述) | [workflow_fieldyear.md](./tables/工作流程/workflow_fieldyear.md) |
| 88 | `workflow_filetypeicon` | 3 | `extendname`(扩展名)、`iconpath`(图标路径)、`describe`(描述) | [workflow_filetypeicon.md](./tables/工作流程/workflow_filetypeicon.md) |
| 89 | `workflow_fileupload` | 8 | `workflowid`(流程ID)、`fieldid`(字段ID)、`catelogtype`(目录类型)、`doccategory`(目录) 等共 8 个字段 | [workflow_fileupload.md](./tables/工作流程/workflow_fileupload.md) |
| 90 | `workflow_flownode` | 31 | `remarkcolumn`(-)、`isapprovalprocess`(-)、`showdesc`(-)、`selectformat`(-) 等共 31 个字段 | [workflow_flownode.md](./tables/工作流程/workflow_flownode.md) |
| 91 | `workflow_flownode_dellog` | 131 | `remarkcolumn`(参考workflow_flownode)、`isapprovalprocess`(参考workflow_flownode)、`showdesc`(参考workflow_flownode)、`selectformat`(参考workflow_flownode) 等共 131 个字段 | [workflow_flownode_dellog.md](./tables/工作流程/workflow_flownode_dellog.md) |
| 92 | `workflow_flownodehtml` | 3 | `workflowid`(流程id)、`nodeid`(节点id)、`colsperrow`(每行的列数) | [workflow_flownodehtml.md](./tables/工作流程/workflow_flownodehtml.md) |
| 93 | `workflow_flownodehtml_form` | 3 | `formid`(表单id)、`isbill`(是否是单独)、`colsperrow`(初始化行数) | [workflow_flownodehtml_form.md](./tables/工作流程/workflow_flownodehtml_form.md) |
| 94 | `workflow_formbase` | 9 | `id`(ID)、`formname`(表单名称)、`formdesc`(表单描述)、`securelevel`(安全级别) 等共 9 个字段 | [workflow_formbase.md](./tables/工作流程/workflow_formbase.md) |
| 95 | `workflow_formdetailinfo` | 4 | `formid`(表单id)、`rowcalstr`(行规则)、`colcalstr`(列规则)、`maincalstr`(主规则) | [workflow_formdetailinfo.md](./tables/工作流程/workflow_formdetailinfo.md) |
| 96 | `workflow_formdict` | 6 | `fieldshowtypes`(下拉开显示类型)、`istemplate`(是否模板)、`id`(ID)、`fieldname`(字段名称) 等共 6 个字段 | [workflow_formdict.md](./tables/工作流程/workflow_formdict.md) |
| 97 | `workflow_formdictdetail` | 15 | `istemplate`(模板)、`fieldshowtypes`(下拉框字段显示类型)、`id`(ID)、`fieldname`(字段名称) 等共 15 个字段 | [workflow_formdictdetail.md](./tables/工作流程/workflow_formdictdetail.md) |
| 98 | `workflow_formfield` | 9 | `formid`(表单id)、`fieldid`(字段id)、`fieldparameter`(字段显示参数)、`needcheck`(是否需要 script检验) 等共 9 个字段 | [workflow_formfield.md](./tables/工作流程/workflow_formfield.md) |
| 99 | `workflow_formmode` | 6 | `id`(ID)、`formid`(表单id)、`isbill`(是否为单据)、`isprint`(是否打印模板) 等共 6 个字段 | [workflow_formmode.md](./tables/工作流程/workflow_formmode.md) |
| 100 | `workflow_formprop` | 12 | `formid`(表单id)、`objid`(对象id)、`objtype`(对象类型)、`fieldid`(字段id) 等共 12 个字段 | [workflow_formprop.md](./tables/工作流程/workflow_formprop.md) |
| 101 | `workflow_formsignatureimglog` | 3 | `id`(ID)、`requestlogid`(日志id)、`imagefileid`(图片id) | [workflow_formsignatureimglog.md](./tables/工作流程/workflow_formsignatureimglog.md) |
| 102 | `workflow_formsignaturelog` | 8 | `id`(ID)、`workflowrequestlogid`(日志id)、`fieldname`(控件名称)、`markname`(印章名称) 等共 8 个字段 | [workflow_formsignaturelog.md](./tables/工作流程/workflow_formsignaturelog.md) |
| 103 | `workflow_formsignremark` | 4 | `id`(ID)、`requestlogid`(日志id)、`imagefileid`(图片id)、`remark`(表单签章数据) | [workflow_formsignremark.md](./tables/工作流程/workflow_formsignremark.md) |
| 104 | `workflow_formula` | 8 | `desclabel`(多语言描述信息)、`description`(描述信息)、`filename`(自定义函数文件名)、`showorder`(显示顺序) 等共 8 个字段 | [workflow_formula.md](./tables/工作流程/workflow_formula.md) |
| 105 | `workflow_formula_db` | 10 | `id`(主键编码)、`name`(函数名)、`desclabel`(多语言描述信息)、`description`(描述信息) 等共 10 个字段 | [workflow_formula_db.md](./tables/工作流程/workflow_formula_db.md) |
| 106 | `workflow_formula_trigger` | 6 | `showorder`(显示顺序)、`id`(主键编码)、`actionname`(触发动作名称)、`description`(描述信息) 等共 6 个字段 | [workflow_formula_trigger.md](./tables/工作流程/workflow_formula_trigger.md) |
| 107 | `workflow_formula_type` | 4 | `id`(主键编码)、`languageid`(多语言描述信息)、`description`(描述信息)、`showorder`(显示顺序) | [workflow_formula_type.md](./tables/工作流程/workflow_formula_type.md) |
| 108 | `workflow_forward` | 17 | `requestid`(请求id)、`forwardid`(转发人)、`beforwardid`(被转发人)、`ispendingforward`(是否允许待办事宜转发) 等共 17 个字段 | [workflow_forward.md](./tables/工作流程/workflow_forward.md) |
| 109 | `workflow_freeright` | 3 | `nodeid`(节点id)、`isroutedit`(路径是否可编辑)、`istableedit`(表是否可编辑) | [workflow_freeright.md](./tables/工作流程/workflow_freeright.md) |
| 110 | `workflow_function_manage` | 10 | `workflowid`(工作流id)、`typeview`(流程状态查看)、`dataview`(流程数据查看)、`automatism`(自动催办) 等共 10 个字段 | [workflow_function_manage.md](./tables/工作流程/workflow_function_manage.md) |
| 111 | `workflow_fwadvanced` | 5 | `id`(id)、`wfid`(流程id)、`nodeid`(节点id)、`fwtype`(类型) 等共 5 个字段 | [workflow_fwadvanced.md](./tables/工作流程/workflow_fwadvanced.md) |
| 112 | `workflow_fwlimitset` | 9 | `id`(id)、`wfid`(流程id)、`nodeid`(节点id)、`fwtype`(类型) 等共 9 个字段 | [workflow_fwlimitset.md](./tables/工作流程/workflow_fwlimitset.md) |
| 113 | `workflow_fwoperadvanced` | 10 | `id`(id)、`mainid`(主表Id)、`objtype`(接收人类型)、`objid`(內容) 等共 10 个字段 | [workflow_fwoperadvanced.md](./tables/工作流程/workflow_fwoperadvanced.md) |
| 114 | `workflow_fwrecadvanced` | 10 | `id`(id)、`mainid`(主表id)、`objtype`(接收人类型)、`objid`(接收人id) 等共 10 个字段 | [workflow_fwrecadvanced.md](./tables/工作流程/workflow_fwrecadvanced.md) |
| 115 | `workflow_fwrecsimple` | 10 | `id`(id)、`mainid`(主表id)、`objtype`(类型)、`objid`(值) 等共 10 个字段 | [workflow_fwrecsimple.md](./tables/工作流程/workflow_fwrecsimple.md) |
| 116 | `workflow_groupdetail` | 24 | `id`(ID)、`groupid`(操作者组id)、`objid`(相关对象id)、`level_n`(相关级别) 等共 24 个字段 | [workflow_groupdetail.md](./tables/工作流程/workflow_groupdetail.md) |
| 117 | `workflow_groupdetail_matrix` | 3 | `groupdetailid`(组明细id)、`matrix`(矩阵)、`value_field`(字段值) | [workflow_groupdetail_matrix.md](./tables/工作流程/workflow_groupdetail_matrix.md) |
| 118 | `workflow_groupinfo` | 8 | `id`(ID)、`workflowid`(流程id)、`groupname`(组名称)、`direction`(发生额方向) 等共 8 个字段 | [workflow_groupinfo.md](./tables/工作流程/workflow_groupinfo.md) |
| 119 | `workflow_hrmoperator` | 6 | `type`(类型)、`objid`(人员id)、`signorder`(操作类型)、`orders`(排序) 等共 6 个字段 | [workflow_hrmoperator.md](./tables/工作流程/workflow_hrmoperator.md) |
| 120 | `workflow_initialization` | 3 | `id`(ID)、`wfid`(流程ID)、`orderid`(排序) | [workflow_initialization.md](./tables/工作流程/workflow_initialization.md) |
| 121 | `workflow_interfaces` | 5 | `id`(ID)、`name`(名称)、`deploy_status`(部署状态)、`memo`(备注) 等共 5 个字段 | [workflow_interfaces.md](./tables/工作流程/workflow_interfaces.md) |
| 122 | `workflow_keyword` | 7 | `id`(ID)、`keywordname`(主题词名称)、`keyworddesc`(主题词描述)、`parentid`(父节点id) 等共 7 个字段 | [workflow_keyword.md](./tables/工作流程/workflow_keyword.md) |
| 123 | `workflow_logviewnode` | 3 | `viewnodeids`(可查看节点数)、`workflowid`(流程id)、`nodeid`(节点id) | [workflow_logviewnode.md](./tables/工作流程/workflow_logviewnode.md) |
| 124 | `workflow_logviewusers` | 2 | `logid`(日志ID)、`userid`(用户ID) | [workflow_logviewusers.md](./tables/工作流程/workflow_logviewusers.md) |
| 125 | `workflow_margin` | 8 | `workflowid`(路径Id)、`id`(id)、`nodeid`(节点类型)、`type`(雷旭) 等共 8 个字段 | [workflow_margin.md](./tables/工作流程/workflow_margin.md) |
| 126 | `workflow_matrixdetail` | 5 | `groupdetailid`(组明细id)、`condition_field`(条件字段)、`workflow_field`(流转字段)、`workflow_objid`(字段值) 等共 5 个字段 | [workflow_matrixdetail.md](./tables/工作流程/workflow_matrixdetail.md) |
| 127 | `workflow_mgms` | 10 | `id`(ID)、`requestid`(请求id)、`userid`(用户id)、`receivedate`(接收日期) 等共 10 个字段 | [workflow_mgms.md](./tables/工作流程/workflow_mgms.md) |
| 128 | `workflow_mgmsusers` | 1 | `userid`(用户id) | [workflow_mgmsusers.md](./tables/工作流程/workflow_mgmsusers.md) |
| 129 | `workflow_mgmsworkflows` | 1 | `workflowid`(流程id) | [workflow_mgmsworkflows.md](./tables/工作流程/workflow_mgmsworkflows.md) |
| 130 | `workflow_modeview` | 7 | `formid`(表单id或单据id)、`nodeid`(节点id)、`isbill`(是否是单据)、`fieldid`(字段id) 等共 7 个字段 | [workflow_modeview.md](./tables/工作流程/workflow_modeview.md) |
| 131 | `workflow_monitor_bound` | 13 | `monitorhrmid`(监控人id)、`workflowid`(流程id)、`operatordate`(操作日期)、`operatortime`(操作时间) 等共 13 个字段 | [workflow_monitor_bound.md](./tables/工作流程/workflow_monitor_bound.md) |
| 132 | `workflow_monitor_detail` | 13 | `infoid`(流程监控信息表id)、`workflowid`(流程id)、`operatordate`(操作日期)、`operatortime`(操作时间) 等共 13 个字段 | [workflow_monitor_detail.md](./tables/工作流程/workflow_monitor_detail.md) |
| 133 | `workflow_monitor_dt_wfid` | 7 | `id`(id)、`infoid`(主表id)、`objtype`(监控类型)、`objvalue`(监控类型值) 等共 7 个字段 | [workflow_monitor_dt_wfid.md](./tables/工作流程/workflow_monitor_dt_wfid.md) |
| 134 | `workflow_monitor_info` | 10 | `id`(ID)、`monitortype`(监控类型)、`flowcount`(流程数量)、`operatordate`(操作日期) 等共 10 个字段 | [workflow_monitor_info.md](./tables/工作流程/workflow_monitor_info.md) |
| 135 | `workflow_monitortype` | 4 | `id`(ID)、`typename`(类型名称)、`typedesc`(类型描述)、`typeorder`(显示顺序) | [workflow_monitortype.md](./tables/工作流程/workflow_monitortype.md) |
| 136 | `workflow_msg_info` | 6 | `requestid`(requestid)、`msgtype`(消息类型)、`msgtypedesc`(消息描述)、`targetid`(目标id) 等共 6 个字段 | [workflow_msg_info.md](./tables/工作流程/workflow_msg_info.md) |
| 137 | `workflow_node_fix_flowtime` | 20 | `groupid`(操作人组ID)、`requestid`(请求ID)、`workflowid`(流程ID)、`nodeid`(节点ID) 等共 20 个字段 | [workflow_node_fix_flowtime.md](./tables/工作流程/workflow_node_fix_flowtime.md) |
| 138 | `workflow_node_flowtime` | 20 | `groupid`(操作人组ID)、`overflowtime`(超时时间)、`isremark`(操作类型)、`islasttimes`(最后一次操作) 等共 20 个字段 | [workflow_node_flowtime.md](./tables/工作流程/workflow_node_flowtime.md) |
| 139 | `workflow_nodebase` | 11 | `drawstyle`(流程图样式)、`id`(ID)、`nodename`(节点名称)、`isstart`(当前节点是否为创建节点) 等共 11 个字段 | [workflow_nodebase.md](./tables/工作流程/workflow_nodebase.md) |
| 140 | `workflow_nodecustomnewmenu` | 14 | `newcustommessage`(自定义消息)、`orderid`(排序)、`id`(ID)、`wfid`(工作流id) 等共 14 个字段 | [workflow_nodecustomnewmenu.md](./tables/工作流程/workflow_nodecustomnewmenu.md) |
| 141 | `workflow_nodecustomrcmenu` | 108 | `forsubsign`(批注默认意见)、`ccsubsign`(抄送默认意见)、`taksign`(回复默认意见)、`forwardbackname7`(转发收回按钮中文) 等共 108 个字段 | [workflow_nodecustomrcmenu.md](./tables/工作流程/workflow_nodecustomrcmenu.md) |
| 142 | `workflow_nodefieldattr` | 10 | `id`(ID)、`fieldid`(字段id)、`formid`(表单id)、`isbill`(是否单据) 等共 10 个字段 | [workflow_nodefieldattr.md](./tables/工作流程/workflow_nodefieldattr.md) |
| 143 | `workflow_nodeform` | 10 | `isalonerow`(独占一行)、`isorder`(是否排序字段)、`ordertype`(排序类型)、`orderindex`(排序字段顺序) 等共 10 个字段 | [workflow_nodeform.md](./tables/工作流程/workflow_nodeform.md) |
| 144 | `workflow_nodeform_form` | 8 | `formid`(表单id)、`isbill`(是否是单据)、`fieldid`(字段id)、`isview`(是否可查看) 等共 8 个字段 | [workflow_nodeform_form.md](./tables/工作流程/workflow_nodeform_form.md) |
| 145 | `workflow_nodeformgroup` | 12 | `nodeid`(节点id)、`groupid`(组id)、`isadd`(是否允许新增明细)、`isedit`(是否允许修改已有明细) 等共 12 个字段 | [workflow_nodeformgroup.md](./tables/工作流程/workflow_nodeformgroup.md) |
| 146 | `workflow_nodeformgroup_form` | 13 | `formid`(表单id)、`isbill`(是否是单据)、`groupid`(组id)、`isadd`(是否允许新增已有明细) 等共 13 个字段 | [workflow_nodeformgroup_form.md](./tables/工作流程/workflow_nodeformgroup_form.md) |
| 147 | `workflow_nodegroup` | 4 | `id`(ID)、`nodeid`(节点id)、`groupname`(节点操作者组名称)、`canview`(是否可跟踪) | [workflow_nodegroup.md](./tables/工作流程/workflow_nodegroup.md) |
| 148 | `workflow_nodehtmllayout` | 19 | `scriptstr`(e9代码块)、`stylestr`(e9样式块)、`id`(ID)、`workflowid`(流程id) 等共 19 个字段 | [workflow_nodehtmllayout.md](./tables/工作流程/workflow_nodehtmllayout.md) |
| 149 | `workflow_nodelink` | 73 | `drawstyle`(新版流程图的样式)、`e9points`(e9出口方向)、`id`(ID)、`workflowid`(工作流id) 等共 73 个字段 | [workflow_nodelink.md](./tables/工作流程/workflow_nodelink.md) |
| 150 | `workflow_nodelinkotfield` | 6 | `id`(ID)、`overtimeid`(超时提醒设置id)、`tofieldid`(赋值字段id)、`tofieldname`(赋值字段名) 等共 6 个字段 | [workflow_nodelinkotfield.md](./tables/工作流程/workflow_nodelinkotfield.md) |
| 151 | `workflow_nodelinkovertime` | 21 | `id`(ID)、`linkid`(出口id)、`workflowid`(工作流id)、`remindname`(提醒名称) 等共 21 个字段 | [workflow_nodelinkovertime.md](./tables/工作流程/workflow_nodelinkovertime.md) |
| 152 | `workflow_nodemode` | 7 | `id`(ID)、`workflowid`(流程id)、`formid`(表单id)、`nodeid`(节点id) 等共 7 个字段 | [workflow_nodemode.md](./tables/工作流程/workflow_nodemode.md) |
| 153 | `workflow_nodeovertime` | 15 | `id`(主键id)、`workflowid`(路径id)、`nodeid`(节点id)、`requestid`(流程请求id) 等共 15 个字段 | [workflow_nodeovertime.md](./tables/工作流程/workflow_nodeovertime.md) |
| 154 | `workflow_nodeovertime_detail` | 21 | `id`(id)、`workflowid`(流程id)、`nodeid`(节点id)、`remindName`(提醒名称) 等共 21 个字段 | [workflow_nodeovertime_detail.md](./tables/工作流程/workflow_nodeovertime_detail.md) |
| 155 | `workflow_nownode` | 4 | `requestid`(请求id)、`nownodeid`(当前节点id)、`nownodetype`(当前节点类型)、`nownodeattribute`(当前节点属性) | [workflow_nownode.md](./tables/工作流程/workflow_nownode.md) |
| 156 | `workflow_nownode_dellog` | 5 | `nownodeattribute`(当前节点属性)、`isvalid`(是否有效)、`requestid`(流程id)、`nownodeid`(节点id) 等共 5 个字段 | [workflow_nownode_dellog.md](./tables/工作流程/workflow_nownode_dellog.md) |
| 157 | `workflow_otheroperator` | 6 | `id`(ID)、`requestid`(请求id)、`userid`(用户id)、`usertype`(用户类型) 等共 6 个字段 | [workflow_otheroperator.md](./tables/工作流程/workflow_otheroperator.md) |
| 158 | `workflow_penetratelog` | 27 | `id`(ID)、`requestid`(请求id)、`workflowid`(流程id)、`nodeid`(节点id) 等共 27 个字段 | [workflow_penetratelog.md](./tables/工作流程/workflow_penetratelog.md) |
| 159 | `workflow_printset` | 19 | `id`(id)、`workflowid`(workflowid)、`nodeid`(nodeid)、`modeid`(模板id) 等共 19 个字段 | [workflow_printset.md](./tables/工作流程/workflow_printset.md) |
| 160 | `workflow_process_relative` | 5 | `id`(ID)、`workflowid`(流程id)、`nodeids`(节点ids)、`officaltype`(设置发文类型：发文/收文/签报) 等共 5 个字段 | [workflow_process_relative.md](./tables/工作流程/workflow_process_relative.md) |
| 161 | `workflow_processinst` | 6 | `id`(ID)、`pd_id`(短语描述id)、`phrasedesc`(短语描述)、`phraseshort`(短语) 等共 6 个字段 | [workflow_processinst.md](./tables/工作流程/workflow_processinst.md) |
| 162 | `workflow_remarkdisplay` | 9 | `isprint`(是否打印)、`workflowid`(流程ID)、`nodeid`(节点ID)、`isshow`(是否显示模板) 等共 9 个字段 | [workflow_remarkdisplay.md](./tables/工作流程/workflow_remarkdisplay.md) |
| 163 | `workflow_report` | 9 | `id`(ID)、`reportname`(工作流报表名称)、`reporttype`(工作流报表种类)、`reportwfid`(报表相关工作流id) 等共 9 个字段 | [workflow_report.md](./tables/工作流程/workflow_report.md) |
| 164 | `workflow_report_competence` | 16 | `id`(主键ID)、`formid`(表单ID)、`isbill`(单据还是表单)、`type`(赋权对象类型) 等共 16 个字段 | [workflow_report_competence.md](./tables/工作流程/workflow_report_competence.md) |
| 165 | `workflow_reportdspfield` | 17 | `id`(ID)、`reportid`(工作流报表id)、`fieldid`(工作流字段id)、`isstat`(是否进行统计) 等共 17 个字段 | [workflow_reportdspfield.md](./tables/工作流程/workflow_reportdspfield.md) |
| 166 | `workflow_reporttype` | 5 | `typeorder`(显示顺序)、`id`(ID)、`typename`(报表种类名称)、`typedesc`(报表种类描述) 等共 5 个字段 | [workflow_reporttype.md](./tables/工作流程/workflow_reporttype.md) |
| 167 | `workflow_reqbrowextrainfo` | 7 | `id`(ID)、`requestid`(请求id)、`fieldid`(字段id)、`type`(类型) 等共 7 个字段 | [workflow_reqbrowextrainfo.md](./tables/工作流程/workflow_reqbrowextrainfo.md) |
| 168 | `workflow_request_fix_flowtime` | 14 | `requestid`(请求ID)、`workflowid`(流程ID)、`workflowtype`(流程类型)、`createdate`(创建日期) 等共 14 个字段 | [workflow_request_fix_flowtime.md](./tables/工作流程/workflow_request_fix_flowtime.md) |
| 169 | `workflow_request_flowtime` | 14 | `onlysave`(只是新建保存)、`requestid`(请求ID)、`workflowid`(流程ID)、`workflowtype`(流程类型) 等共 14 个字段 | [workflow_request_flowtime.md](./tables/工作流程/workflow_request_flowtime.md) |
| 170 | `workflow_requestbase` | 19 | `totalgroups`(总共需要的操作者组数)、`requestname`(请求名称)、`creater`(创建人)、`createdate`(创建日期) 等共 19 个字段 | [workflow_requestbase.md](./tables/工作流程/workflow_requestbase.md) |
| 171 | `workflow_requestbase_dellog` | 40 | `isvalid`(是否有效)、`requestid`(请求id)、`workflowid`(流程id)、`lastnodeid`(最后操作节点id) 等共 40 个字段 | [workflow_requestbase_dellog.md](./tables/工作流程/workflow_requestbase_dellog.md) |
| 172 | `workflow_requestdeletelog` | 10 | `isold`(是否老数据)、`isvalid`(是否恢复)、`request_id`(请求id)、`request_name`(请求名称) 等共 10 个字段 | [workflow_requestdeletelog.md](./tables/工作流程/workflow_requestdeletelog.md) |
| 173 | `workflow_requestexception` | 7 | `keyid`(自增ID)、`requestid`(请求ID)、`nodeid`(节点ID)、`destnodeid`(目标节点ID) 等共 7 个字段 | [workflow_requestexception.md](./tables/工作流程/workflow_requestexception.md) |
| 174 | `workflow_requestlog` | 1 | `issubmitdirect`(退回后再提交直达本节点) | [workflow_requestlog.md](./tables/工作流程/workflow_requestlog.md) |
| 175 | `workflow_requestlog_dellog` | 33 | `isvalid`(是否有效)、`issubmitdirect`(是否启用提交至退回节点)、`remarkquote`(签字意见引用)、`fulltextannotation`(全文批注) 等共 33 个字段 | [workflow_requestlog_dellog.md](./tables/工作流程/workflow_requestlog_dellog.md) |
| 176 | `workflow_requestlogatinfo` | 11 | `id`(ID)、`requestid`(请求id)、`workflowid`(流程id)、`nodeid`(节点id) 等共 11 个字段 | [workflow_requestlogatinfo.md](./tables/工作流程/workflow_requestlogatinfo.md) |
| 177 | `workflow_requestlogsequence` | 1 | `requestlogid`(当前最大工作流日志id) | [workflow_requestlogsequence.md](./tables/工作流程/workflow_requestlogsequence.md) |
| 178 | `workflow_requestoperatelog` | 12 | `detailinfo`(明细JSON数据)、`retype`(操作类型)、`reoperatorid`(被代理人ID)、`id`(ID) 等共 12 个字段 | [workflow_requestoperatelog.md](./tables/工作流程/workflow_requestoperatelog.md) |
| 179 | `workflow_requestoperatelog_dtl` | 3 | `requestid`(请求id)、`optlogid`(操作日志主表（workflow_requestoperatelog）id)、`entitytype`(实体表) | [workflow_requestoperatelog_dtl.md](./tables/工作流程/workflow_requestoperatelog_dtl.md) |
| 180 | `workflow_requestoperatelog_oi` | 3 | `requestid`(请求id)、`optlogid`(操作日志主表（workflow_requestoperatelog）id)、`entitytype`(实体表) | [workflow_requestoperatelog_oi.md](./tables/工作流程/workflow_requestoperatelog_oi.md) |
| 181 | `workflow_requestsequence` | 1 | `requestid`(当前最大工作流id) | [workflow_requestsequence.md](./tables/工作流程/workflow_requestsequence.md) |
| 182 | `workflow_requestsign` | 8 | `id`(ID)、`requestid`(请求id)、`nodeid`(节点id)、`userid`(用户id) 等共 8 个字段 | [workflow_requestsign.md](./tables/工作流程/workflow_requestsign.md) |
| 183 | `workflow_requestuserdefault` | 24 | `wfspaopenwindow`(流程spa默认弹框)、`signdefault`(默认意见)、`addwfdefaultselectedtab`(新建流程默认选中tab)、`addwfmulitcol`(新建流程默认显示类型) 等共 24 个字段 | [workflow_requestuserdefault.md](./tables/工作流程/workflow_requestuserdefault.md) |
| 184 | `workflow_requestviewlog` | 9 | `id`(ID)、`viewer`(查看人)、`viewdate`(查看日期)、`viewtime`(查看时间) 等共 9 个字段 | [workflow_requestviewlog.md](./tables/工作流程/workflow_requestviewlog.md) |
| 185 | `workflow_rulesystemvar` | 4 | `id`(id)、`mark`(标识)、`varname`(名字的lableid)、`description`(描述的labelid) | [workflow_rulesystemvar.md](./tables/工作流程/workflow_rulesystemvar.md) |
| 186 | `workflow_secondauth_freesecret` | 4 | `userid`(用户id)、`usertype`(用户类型)、`authtype`(二次认证的类型)、`freesecrettime`(免密时间) | [workflow_secondauth_freesecret.md](./tables/工作流程/workflow_secondauth_freesecret.md) |
| 187 | `workflow_secondauth_password` | 5 | `userid`(用户id)、`usertype`(用户类型)、`dyncmiapassword`(动态密码)、`salt`(盐值) 等共 5 个字段 | [workflow_secondauth_password.md](./tables/工作流程/workflow_secondauth_password.md) |
| 188 | `workflow_selectitem` | 13 | `fieldid`(字段id)、`isbill`(是否为单据)、`selectvalue`(下拉框的值)、`selectname`(下拉框名称) 等共 13 个字段 | [workflow_selectitem.md](./tables/工作流程/workflow_selectitem.md) |
| 189 | `workflow_selectitemobj` | 8 | `id`(ID)、`fieldid`(字段id)、`isbill`(是否为单据)、`selectvalue`(可选择的值) 等共 8 个字段 | [workflow_selectitemobj.md](./tables/工作流程/workflow_selectitemobj.md) |
| 190 | `workflow_settings` | 6 | `id`(id)、`isOpen`(超时是否开启)、`scanRate`(超时扫描频率)、`isSkipWorkingDay`(是否跳过非工作日) 等共 6 个字段 | [workflow_settings.md](./tables/工作流程/workflow_settings.md) |
| 191 | `workflow_settitle` | 11 | `id`(ID)、`xh`(标题字段序号)、`fieldtype`(字段类型)、`fieldvalue`(字段值) 等共 11 个字段 | [workflow_settitle.md](./tables/工作流程/workflow_settitle.md) |
| 192 | `workflow_sharedscope` | 26 | `currentid`(流程状态表ID)、`jobobjid`(岗位)、`id`(id)、`wfid`(流程id) 等共 26 个字段 | [workflow_sharedscope.md](./tables/工作流程/workflow_sharedscope.md) |
| 193 | `workflow_shortnamesetting` | 7 | `id`(ID)、`workflowid`(流程id)、`formid`(表单或单据id)、`isbill`(是否单据) 等共 7 个字段 | [workflow_shortnamesetting.md](./tables/工作流程/workflow_shortnamesetting.md) |
| 194 | `workflow_specialfield` | 7 | `id`(ID)、`fieldid`(字段的id)、`displayname`(显示名)、`linkaddress`(链接地址) 等共 7 个字段 | [workflow_specialfield.md](./tables/工作流程/workflow_specialfield.md) |
| 195 | `workflow_subcomabbr` | 8 | `id`(ID)、`workflowid`(流程id)、`formid`(表单或单据id)、`isbill`(是否单据) 等共 8 个字段 | [workflow_subcomabbr.md](./tables/工作流程/workflow_subcomabbr.md) |
| 196 | `workflow_subcomabbrdef` | 3 | `id`(ID)、`subcompanyid`(分部id)、`abbr`(简称) | [workflow_subcomabbrdef.md](./tables/工作流程/workflow_subcomabbrdef.md) |
| 197 | `workflow_subwfrequest` | 4 | `subwfid`(子流程id)、`subrequestid`(子流程请求id)、`mainrequestid`(主流程请求id)、`issame`(是否相同) | [workflow_subwfrequest.md](./tables/工作流程/workflow_subwfrequest.md) |
| 198 | `workflow_subwfset` | 11 | `issplitdetail`(明细拆分触发)、`id`(子流程设置表id)、`mainworkflowid`(主流程id)、`subworkflowid`(子流程id) 等共 11 个字段 | [workflow_subwfset.md](./tables/工作流程/workflow_subwfset.md) |
| 199 | `workflow_subwfsetdetail` | 9 | `id`(ID)、`subwfsetid`(子流程设置表id)、`subworkflowfieldid`(子流程字段id)、`mainworkflowfieldid`(主流程字段id) 等共 9 个字段 | [workflow_subwfsetdetail.md](./tables/工作流程/workflow_subwfsetdetail.md) |
| 200 | `workflow_superviseoperator` | 12 | `id`(id)、`requestid`(流程)、`workflowid`(路径)、`workflowtype`(路径类型) 等共 12 个字段 | [workflow_superviseoperator.md](./tables/工作流程/workflow_superviseoperator.md) |
| 201 | `workflow_supsubcomabbr` | 8 | `id`(ID)、`workflowid`(流程id)、`formid`(表单或单据id)、`isbill`(是否单据) 等共 8 个字段 | [workflow_supsubcomabbr.md](./tables/工作流程/workflow_supsubcomabbr.md) |
| 202 | `workflow_sysworkflow` | 3 | `id`(ID)、`name`(系统工作流名称)、`workflowid`(工作流id) | [workflow_sysworkflow.md](./tables/工作流程/workflow_sysworkflow.md) |
| 203 | `workflow_tabstyle` | 25 | `styleid`(样式id)、`stylename`(样式名称)、`image_bg`(背景图片)、`image_sep`(分隔图片) 等共 25 个字段 | [workflow_tabstyle.md](./tables/工作流程/workflow_tabstyle.md) |
| 204 | `workflow_testlog` | 6 | `id`(日志ID)、`requestid`(请求ID)、`workflowid`(流程ID)、`testtime`(测试时间) 等共 6 个字段 | [workflow_testlog.md](./tables/工作流程/workflow_testlog.md) |
| 205 | `workflow_textinfo` | 7 | `id`(id)、`workflowid`(流程id)、`x`(x坐标)、`y`(y坐标) 等共 7 个字段 | [workflow_textinfo.md](./tables/工作流程/workflow_textinfo.md) |
| 206 | `workflow_titleset` | 3 | `flowid`(流程id)、`fieldid`(字段id)、`gradation`(排序字段) | [workflow_titleset.md](./tables/工作流程/workflow_titleset.md) |
| 207 | `workflow_track` | 19 | `id`(ID)、`optkind`(日志操作类型)、`requestid`(请求对应的id)、`nodeid`(节点名称) 等共 19 个字段 | [workflow_track.md](./tables/工作流程/workflow_track.md) |
| 208 | `workflow_trackdetail` | 22 | `id`(ID)、`sn`(sn)、`optkind`(日志操作类型)、`opttype`(日志操作类型) 等共 22 个字段 | [workflow_trackdetail.md](./tables/工作流程/workflow_trackdetail.md) |
| 209 | `workflow_tridiffwfdifffield` | 16 | `issplitdetail`(明细拆分触发)、`triggertype`(触发类型)、`triggeroperation`(触发操作)、`enable`(使能操作) 等共 16 个字段 | [workflow_tridiffwfdifffield.md](./tables/工作流程/workflow_tridiffwfdifffield.md) |
| 210 | `workflow_tridiffwfsubwf` | 15 | `id`(ID)、`tridiffwfdifffieldid`(触发不同流程可区分字段表id)、`subworkflowid`(子流程id)、`subwfcreatortype`(子流程创建人类型) 等共 15 个字段 | [workflow_tridiffwfsubwf.md](./tables/工作流程/workflow_tridiffwfsubwf.md) |
| 211 | `workflow_tridiffwfsubwffield` | 8 | `id`(ID)、`tridiffwfsubwfid`(触发不同流程子流程设置表id)、`subworkflowfieldid`(子流程字段id)、`mainworkflowfieldid`(主流程字段id) 等共 8 个字段 | [workflow_tridiffwfsubwffield.md](./tables/工作流程/workflow_tridiffwfsubwffield.md) |
| 212 | `workflow_trisubwfbuttonname` | 8 | `id`(ID)、`workflowid`(流程id)、`nodeid`(节点id)、`subwfsettablename`(设置表名称) 等共 8 个字段 | [workflow_trisubwfbuttonname.md](./tables/工作流程/workflow_trisubwfbuttonname.md) |
| 213 | `workflow_type` | 5 | `dsporder`(显示顺序)、`iconkey`(流程类型图标ID)、`id`(ID)、`typename`(工作流种类名称) 等共 5 个字段 | [workflow_type.md](./tables/工作流程/workflow_type.md) |
| 214 | `workflow_updatecolumnlenlog` | 3 | `tablename`(表名)、`tablecolumn`(列明)、`columnlength`(长度) | [workflow_updatecolumnlenlog.md](./tables/工作流程/workflow_updatecolumnlenlog.md) |
| 215 | `workflow_urger_matrix` | 3 | `groupdetailid`(groupid)、`matrix`(矩阵)、`value_field`(字段id) | [workflow_urger_matrix.md](./tables/工作流程/workflow_urger_matrix.md) |
| 216 | `workflow_urger_matrix_detail` | 5 | `groupdetailid`(groupid)、`condition_field`(条件字段)、`workflow_field`(流程字段)、`workflow_objid`(objid) 等共 5 个字段 | [workflow_urger_matrix_detail.md](./tables/工作流程/workflow_urger_matrix_detail.md) |
| 217 | `workflow_urgerdetail` | 13 | `bhxj`(包含下级)、`virtualid`(虚拟机构)、`isforceover`(强制收回)、`id`(ID) 等共 13 个字段 | [workflow_urgerdetail.md](./tables/工作流程/workflow_urgerdetail.md) |
| 218 | `workflow_userref` | 5 | `keyid`(主键)、`name`(名称)、`pwd`(密码)、`userids`(用户ids) 等共 5 个字段 | [workflow_userref.md](./tables/工作流程/workflow_userref.md) |
| 219 | `workflow_versioninfo` | 2 | `wfid`(工作流id)、`wfversionid`(工作流相关版本id) | [workflow_versioninfo.md](./tables/工作流程/workflow_versioninfo.md) |
| 220 | `workflow_versionnoderelation` | 2 | `nodeid`(节点id)、`parentnodeid`(父节点id) | [workflow_versionnoderelation.md](./tables/工作流程/workflow_versionnoderelation.md) |
| 221 | `workflow_viewattrlinkage` | 7 | `isbelong`(运算关系)、`workflowid`(流程id)、`nodeid`(节点id)、`selectfieldid`(下拉框选择的字段id) 等共 7 个字段 | [workflow_viewattrlinkage.md](./tables/工作流程/workflow_viewattrlinkage.md) |
| 222 | `workflow_viewlog` | 12 | `id`(ID)、`p_nodeid`(节点id)、`p_opteruid`(操作用户id)、`p_date`(日期) 等共 12 个字段 | [workflow_viewlog.md](./tables/工作流程/workflow_viewlog.md) |
| 223 | `workflowactionset` | 12 | `drawbackflag`(退回时触发)、`id`(ID)、`actionname`(action名称)、`workflowid`(流程id) 等共 12 个字段 | [workflowactionset.md](./tables/工作流程/workflowactionset.md) |
| 224 | `workflowblacklist` | 3 | `id`(ID)、`userid`(用户id)、`workflowid`(流程id) | [workflowblacklist.md](./tables/工作流程/workflowblacklist.md) |
| 225 | `workflowplandetail` | 6 | `id`(ID)、`userid`(用户id)、`autotype`(触发频率)、`flowdate`(触发时间) 等共 6 个字段 | [workflowplandetail.md](./tables/工作流程/workflowplandetail.md) |
| 226 | `workflowplanset` | 8 | `id`(ID)、`status`(状态)、`frequencyt`(流程频率)、`datetype`(时间类型) 等共 8 个字段 | [workflowplanset.md](./tables/工作流程/workflowplanset.md) |
| 227 | `workflowreportcustom` | 2 | `userid`(人员id)、`wfreportnumperpage`(定义报表每页显示条数) | [workflowreportcustom.md](./tables/工作流程/workflowreportcustom.md) |
| 228 | `workflowreportshare` | 5 | `id`(id)、`reportid`(报表id)、`sharetype`(共享类型)、`seclevelbak`(的) 等共 5 个字段 | [workflowreportshare.md](./tables/工作流程/workflowreportshare.md) |
| 229 | `workflowreportsharedetail` | 5 | `reportid`(报表id)、`userid`(共享用户)、`usertype`(共享用户类型)、`sharelevel`(共享级别) 等共 5 个字段 | [workflowreportsharedetail.md](./tables/工作流程/workflowreportsharedetail.md) |
| 230 | `workflowrptcondmould` | 4 | `id`(ID)、`mouldname`(模板名称)、`userid`(用户id)、`reportid`(报表id) | [workflowrptcondmould.md](./tables/工作流程/workflowrptcondmould.md) |
| 231 | `workflowrptcondmoulddetail` | 14 | `id`(ID)、`mouldid`(模板id)、`fieldid`(字段id)、`ismain`(是否主字段) 等共 14 个字段 | [workflowrptcondmoulddetail.md](./tables/工作流程/workflowrptcondmoulddetail.md) |
| 232 | `workflowsigntxstatus` | 2 | `userid`(用户id)、`status`(状态) | [workflowsigntxstatus.md](./tables/工作流程/workflowsigntxstatus.md) |
| 233 | `workflowtodocprop` | 3 | `id`(ID)、`workflowid`(流程id)、`seccategoryid`(子目录id) | [workflowtodocprop.md](./tables/工作流程/workflowtodocprop.md) |
| 234 | `workflowtodocpropdetail` | 4 | `id`(ID)、`docpropid`(文档属性id)、`docpropfieldid`(文档属性字段id)、`workflowfieldid`(流程字段id) | [workflowtodocpropdetail.md](./tables/工作流程/workflowtodocpropdetail.md) |
| 235 | `workflowtofinanceurlold` | 12 | `id`(id)、`guid1`(guid1)、`sendurl`(sendurl)、`requestid`(requestid) 等共 12 个字段 | [workflowtofinanceurlold.md](./tables/工作流程/workflowtofinanceurlold.md) |
| 236 | `workflowusecount` | 3 | `wfid`(流程id)、`userid`(创建者id)、`count`(创建次数) | [workflowusecount.md](./tables/工作流程/workflowusecount.md) |

### 集成模块

> 本模块共收录 `136` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `ESB_EVENT_LOG` | 7 | `batchkey`(批次号)、`eventid`(事件标识)、`eventtime`(触发时间)、`eventsate`(触发状态) 等共 7 个字段 | [ESB_EVENT_LOG.md](./tables/集成模块/ESB_EVENT_LOG.md) |
| 2 | `Int_FieldMapper` | 7 | `id`(标识)、`scope`(配置类型)、`type`(字段类型)、`src_field_inf`(源字段配置) 等共 7 个字段 | [Int_FieldMapper.md](./tables/集成模块/Int_FieldMapper.md) |
| 3 | `Int_Field_TransAdapter` | 10 | `id`(标识)、`adapter_name`(名称)、`adapter_label`(标签)、`input_str`(输入数据) 等共 10 个字段 | [Int_Field_TransAdapter.md](./tables/集成模块/Int_Field_TransAdapter.md) |
| 4 | `Int_Field_TransGroup` | 12 | `id`(标识)、`scope`(使用范围)、`groupname`(组名称)、`grouplabel`(组标签) 等共 12 个字段 | [Int_Field_TransGroup.md](./tables/集成模块/Int_Field_TransGroup.md) |
| 5 | `Int_Observers` | 6 | `id`(标识)、`scope`(配置类型)、`type`(二级类型)、`observer_clazz`(观察者类) 等共 6 个字段 | [Int_Observers.md](./tables/集成模块/Int_Observers.md) |
| 6 | `Int_Service_Persistence_Log` | 6 | `id`(标识)、`org_filename`(原始文件名)、`to_filename`(重命名的文件名)、`opttime`(操作时间) 等共 6 个字段 | [Int_Service_Persistence_Log.md](./tables/集成模块/Int_Service_Persistence_Log.md) |
| 7 | `Int_Wftrigger_Log` | 11 | `id`(标识)、`trgid`(触发设置标识)、`wfid`(流程标识)、`requestid`(触发出来的流程请求标识) 等共 11 个字段 | [Int_Wftrigger_Log.md](./tables/集成模块/Int_Wftrigger_Log.md) |
| 8 | `QQMailDefaultPwd` | 6 | `id`(标识)、`userid`(用户id)、`loginid`(登录名)、`lastname`(姓名) 等共 6 个字段 | [QQMailDefaultPwd.md](./tables/集成模块/QQMailDefaultPwd.md) |
| 9 | `QQMailEleSetting` | 3 | `id`(标识)、`eid`(元素标识)、`setting`(设置信息) | [QQMailEleSetting.md](./tables/集成模块/QQMailEleSetting.md) |
| 10 | `QQMailLog` | 8 | `id`(标识)、`LogDate`(日志发生日期)、`LogTime`(日志发生时间)、`operateRemark`(同步对象) 等共 8 个字段 | [QQMailLog.md](./tables/集成模块/QQMailLog.md) |
| 11 | `QQMailMap` | 6 | `qqid`(腾讯方对象标识)、`qqpid`(腾讯方上级对象标识)、`weaverid`(泛微方对象标识)、`weavertype`(泛微方对象类型) 等共 6 个字段 | [QQMailMap.md](./tables/集成模块/QQMailMap.md) |
| 12 | `QQMailSetting` | 8 | `id`(标识)、`corpid`(企业秘钥)、`corpsecret`(通讯录秘钥)、`isuse`(是否启用) 等共 8 个字段 | [QQMailSetting.md](./tables/集成模块/QQMailSetting.md) |
| 13 | `SSO_LOGIN_OA` | 6 | `id`(标识)、`appid`(应用标识)、`loginid`(登录账号)、`isuse`(是否使用) 等共 6 个字段 | [SSO_LOGIN_OA.md](./tables/集成模块/SSO_LOGIN_OA.md) |
| 14 | `WEAVER_SSO_LOGIN_LOG` | 9 | `id`(标识)、`appid`(应用标识)、`loginid`(登录账号)、`apploginid`(应用账号) 等共 9 个字段 | [WEAVER_SSO_LOGIN_LOG.md](./tables/集成模块/WEAVER_SSO_LOGIN_LOG.md) |
| 15 | `WEAVER_SSO_USER_MAPPING` | 9 | `id`(标识)、`appid`(应用标识)、`userid`(用户标识)、`loginid`(登录账号) 等共 9 个字段 | [WEAVER_SSO_USER_MAPPING.md](./tables/集成模块/WEAVER_SSO_USER_MAPPING.md) |
| 16 | `actionexecutelog` | 11 | `modifydate`(修改日期)、`modifytime`(修改时间)、`clientip`(客户端IP)、`actiondbid`(未知字段) 等共 11 个字段 | [actionexecutelog.md](./tables/集成模块/actionexecutelog.md) |
| 17 | `actionsetting` | 10 | `id`(主键)、`actionname`(接口动作名称)、`actionclass`(接口动作类文件)、`typename`(接口类型名称) 等共 10 个字段 | [actionsetting.md](./tables/集成模块/actionsetting.md) |
| 18 | `actionsettingdetail` | 5 | `id`(主键)、`actionid`(接口动作名称)、`attrname`(参数名称)、`attrvalue`(参数值) 等共 5 个字段 | [actionsettingdetail.md](./tables/集成模块/actionsettingdetail.md) |
| 19 | `addepmap` | 8 | `id`(主键)、`dep`(组织架构名称)、`pguid`(上级组织架构guid)、`distin`(组织架构DN) 等共 8 个字段 | [addepmap.md](./tables/集成模块/addepmap.md) |
| 20 | `compatibleoldadguid` | 1 | `isnewguid`(兼容标识) | [compatibleoldadguid.md](./tables/集成模块/compatibleoldadguid.md) |
| 21 | `coremaillog` | 8 | `id`(主键id)、`datatype`(数据类型)、`operatedata`(关联数据)、`operatetype`(操作类型) 等共 8 个字段 | [coremaillog.md](./tables/集成模块/coremaillog.md) |
| 22 | `coremailsetting` | 8 | `isuse`(是否启用)、`systemaddress`(邮件系统地址)、`orgid`(邮件系统组织架构标识)、`providerid`(邮件系统供应商ID) 等共 8 个字段 | [coremailsetting.md](./tables/集成模块/coremailsetting.md) |
| 23 | `datasearchparam` | 6 | `id`(自增长主键)、`mainid`(浏览框基本信息id)、`fieldname`(字段名称)、`searchname`(查询字段显示名称) 等共 6 个字段 | [datasearchparam.md](./tables/集成模块/datasearchparam.md) |
| 24 | `datashowexecutelog` | 7 | `id`(ID)、`datashowname`(自定义浏览框标识)、`datashowcount`(自定义浏览框运行次数)、`createdate`(创建日期) 等共 7 个字段 | [datashowexecutelog.md](./tables/集成模块/datashowexecutelog.md) |
| 25 | `datashowparam` | 7 | `id`(ID)、`mainid`(主表id)、`fieldname`(数据字段名称)、`searchname`(查询字段显示名称) 等共 7 个字段 | [datashowparam.md](./tables/集成模块/datashowparam.md) |
| 26 | `datashowset` | 34 | `modifydate`(修改日期)、`modifytime`(修改时间)、`sqltext1`(条件1查询)、`sqltext2`(条件2查询) 等共 34 个字段 | [datashowset.md](./tables/集成模块/datashowset.md) |
| 27 | `datasource_type` | 10 | `id`(主键)、`dbtype`(数据库类型)、`dbname`(数据库名称)、`driverclass`(数据库驱动程序) 等共 10 个字段 | [datasource_type.md](./tables/集成模块/datasource_type.md) |
| 28 | `datasourcesetting` | 18 | `usepool`(是否使用连接池)、`id`(主键)、`pointid`(数据源名称)、`classpath`(数据源类路径) 等共 18 个字段 | [datasourcesetting.md](./tables/集成模块/datasourcesetting.md) |
| 29 | `dmlactionfieldmap` | 3 | `id`(ID)、`actionsqlsetid`(dml接口动作详细信息id)、`maptype`(操作类型) | [dmlactionfieldmap.md](./tables/集成模块/dmlactionfieldmap.md) |
| 30 | `dmlactionset` | 9 | `id`(ID)、`dmlactionname`(名称)、`dmlorder`(执行顺序)、`workflowid`(流程类型id) 等共 9 个字段 | [dmlactionset.md](./tables/集成模块/dmlactionset.md) |
| 31 | `dmlactionsqlset` | 17 | `id`(ID)、`actionid`(dml接口动作主id)、`actiontable`(数据源表)、`dmlformid`(外部主表) 等共 17 个字段 | [dmlactionsqlset.md](./tables/集成模块/dmlactionsqlset.md) |
| 32 | `esb_category` | 10 | `CATEGORYID`(类别标识)、`CATEGORYNAME`(类别名称)、`SUPCATEGORYID`(上级类别)、`DESCRIPTION`(描述说明) 等共 10 个字段 | [esb_category.md](./tables/集成模块/esb_category.md) |
| 33 | `esb_const` | 9 | `constcode`(常量标识)、`constname`(常量名称)、`productcode`(产品标识)、`consttype`(常量类别) 等共 9 个字段 | [esb_const.md](./tables/集成模块/esb_const.md) |
| 34 | `esb_event` | 15 | `EVENTID`(事件标识)、`EVENTNAME`(事件名称)、`EVENTTYPE`(事件类型)、`CONFIG`(配置参数) 等共 15 个字段 | [esb_event.md](./tables/集成模块/esb_event.md) |
| 35 | `esb_event_params` | 13 | `PARAMNAME`(参数名称)、`PARAMTYPE`(参数类型)、`ARRAY`(明细)、`REQUIRED`(必须) 等共 13 个字段 | [esb_event_params.md](./tables/集成模块/esb_event_params.md) |
| 36 | `esb_log` | 9 | `publishid`(发布标识)、`triggerid`(触发标识)、`runtime`(运行时间)、`starttime`(开始时间) 等共 9 个字段 | [esb_log.md](./tables/集成模块/esb_log.md) |
| 37 | `esb_module_setting` | 11 | `MODULECODE`(模块标识)、`MODULENAME`(模块名称)、`SUPMODULECODE`(上级模块)、`DESCRIPTION`(描述) 等共 11 个字段 | [esb_module_setting.md](./tables/集成模块/esb_module_setting.md) |
| 38 | `esb_product_security_setting` | 17 | `ID`(主键)、`APPKEY`(App Key)、`ISAUTH`(认证)、`USERNAME`(用户名) 等共 17 个字段 | [esb_product_security_setting.md](./tables/集成模块/esb_product_security_setting.md) |
| 39 | `esb_product_setting` | 10 | `ID`(主键)、`PRODUCTCODE`(产品编码)、`PRODUCTNAME`(产品名称)、`ORGANIZATION`(所属机构) 等共 10 个字段 | [esb_product_setting.md](./tables/集成模块/esb_product_setting.md) |
| 40 | `esb_publish` | 9 | `publishid`(发布服务标识)、`publishname`(发布服务名称)、`publishtype`(发布服务类型)、`state`(状态) 等共 9 个字段 | [esb_publish.md](./tables/集成模块/esb_publish.md) |
| 41 | `esb_publish_response` | 9 | `publishid`(应用标识)、`eventid`(事件标识)、`paramkey`(参数key)、`assigntype`(映射类型) 等共 9 个字段 | [esb_publish_response.md](./tables/集成模块/esb_publish_response.md) |
| 42 | `esb_resources` | 9 | `resid`(资源标识)、`resname`(资源名称)、`restype`(资源类型)、`resstatus`(资源状态) 等共 9 个字段 | [esb_resources.md](./tables/集成模块/esb_resources.md) |
| 43 | `esb_route` | 6 | `publishid`(发布服务标识)、`routeid`(路由标识)、`serviceid`(服务标识)、`runlevel`(运行级别) 等共 6 个字段 | [esb_route.md](./tables/集成模块/esb_route.md) |
| 44 | `esb_route_alias_params` | 5 | `publishid`(发布服务标识)、`routeid`(路由标识)、`serviceid`(服务标识)、`transmittype`(参数类别) 等共 5 个字段 | [esb_route_alias_params.md](./tables/集成模块/esb_route_alias_params.md) |
| 45 | `esb_route_params` | 9 | `publishid`(发布服务标识)、`routeid`(路由标识)、`serviceid`(服务标识)、`paramkey`(参数标识) 等共 9 个字段 | [esb_route_params.md](./tables/集成模块/esb_route_params.md) |
| 46 | `esb_route_type` | 4 | `routeid`(路由标识)、`publishid`(发布服务标识)、`routetype`(路由类型)、`params`(参数信息) | [esb_route_type.md](./tables/集成模块/esb_route_type.md) |
| 47 | `esb_service_config` | 4 | `type`(接口类别)、`clazz`(接口执行类)、`titleLable`(接口显示名多语言标记)、`description`(说明) | [esb_service_config.md](./tables/集成模块/esb_service_config.md) |
| 48 | `esb_service_log` | 12 | `publishid`(发布服务标识)、`serviceid`(注册服务标识)、`resourceid`(资源标识)、`triggerid`(触发标识) 等共 12 个字段 | [esb_service_log.md](./tables/集成模块/esb_service_log.md) |
| 49 | `esb_transform` | 8 | `transformCode`(转换规则标识)、`transformName`(转换规则名称)、`productCode`(产品标识)、`moduleCode`(模块标识) 等共 8 个字段 | [esb_transform.md](./tables/集成模块/esb_transform.md) |
| 50 | `esb_transform_config` | 4 | `id`(主键)、`productCode`(产品标识)、`transformCode`(转换规则标识)、`matchData`(匹配数据) | [esb_transform_config.md](./tables/集成模块/esb_transform_config.md) |
| 51 | `esb_transform_config_params` | 7 | `configId`(转换规则使用映射ID)、`paramKey`(参数标识)、`ASSIGNTYPE`(映射类别)、`assignValue`(映射内容) 等共 7 个字段 | [esb_transform_config_params.md](./tables/集成模块/esb_transform_config_params.md) |
| 52 | `esb_transform_params` | 8 | `transformCode`(转换规则标识)、`productCode`(产品标识)、`paramKey`(参数标识)、`paramName`(参数名称) 等共 8 个字段 | [esb_transform_params.md](./tables/集成模块/esb_transform_params.md) |
| 53 | `esb_trigger` | 12 | `triggerid`(触发标识)、`publishid`(发布服务标识)、`triggertype`(触发类型)、`resourceid`(资源标识) 等共 12 个字段 | [esb_trigger.md](./tables/集成模块/esb_trigger.md) |
| 54 | `esb_trigger_map` | 5 | `publishid`(发布服务标识)、`triggerid`(服务方式标识)、`paramkey`(参数名)、`fieldvalue`(参数值) 等共 5 个字段 | [esb_trigger_map.md](./tables/集成模块/esb_trigger_map.md) |
| 55 | `esb_variable` | 5 | `variablecode`(变量标识)、`variablename`(变量名称)、`description`(说明)、`variabletype`(变量类别) 等共 5 个字段 | [esb_variable.md](./tables/集成模块/esb_variable.md) |
| 56 | `esbformactionset` | 13 | `id`(主键ID)、`actionname`(接口名称)、`showname`(显示名)、`formid`(流程表单ID) 等共 13 个字段 | [esbformactionset.md](./tables/集成模块/esbformactionset.md) |
| 57 | `esbmethodparamvalue` | 13 | `id`(主键ID)、`actionid`(ESB接口配置主键)、`paramname`(参数名)、`showname`(参数显示名) 等共 13 个字段 | [esbmethodparamvalue.md](./tables/集成模块/esbmethodparamvalue.md) |
| 58 | `esbreturnassign` | 13 | `id`(主键ID)、`actionid`(ESB接口ID)、`fieldname`(字段名)、`fieldtype`(字段类型) 等共 13 个字段 | [esbreturnassign.md](./tables/集成模块/esbreturnassign.md) |
| 59 | `esbreturnrule` | 6 | `id`(主键ID)、`setid`(ESB接口主键)、`rulename`(规则名称)、`condition`(规则条件内容) 等共 6 个字段 | [esbreturnrule.md](./tables/集成模块/esbreturnrule.md) |
| 60 | `esbreturnrule_expressionbase` | 20 | `id`(主键ID)、`ruleid`(规则ID)、`datafield`(数据字段)、`datafieldtext`(数据字段文本信息) 等共 20 个字段 | [esbreturnrule_expressionbase.md](./tables/集成模块/esbreturnrule_expressionbase.md) |
| 61 | `esbreturnrule_expressions` | 5 | `id`(主键ID)、`ruleid`(规则主键)、`relation`(规则之间的关系)、`expids`(表达式ID) 等共 5 个字段 | [esbreturnrule_expressions.md](./tables/集成模块/esbreturnrule_expressions.md) |
| 62 | `esbreturnrule_mapitem` | 9 | `id`(主键ID)、`ruleid`(规则ID)、`rulesrc`(源规则)、`linkid`(链接ID) 等共 9 个字段 | [esbreturnrule_mapitem.md](./tables/集成模块/esbreturnrule_mapitem.md) |
| 63 | `esbreturnrule_maplist` | 9 | `id`(主键ID)、`wfid`(流程ID)、`linkid`(链接ID)、`ruleid`(规则ID) 等共 9 个字段 | [esbreturnrule_maplist.md](./tables/集成模块/esbreturnrule_maplist.md) |
| 64 | `esbreturnrule_variablebase` | 5 | `id`(主键ID)、`name`(名称)、`ruleid`(规则ID)、`fieldtype`(字段类型) 等共 5 个字段 | [esbreturnrule_variablebase.md](./tables/集成模块/esbreturnrule_variablebase.md) |
| 65 | `exp_dbdetail` | 7 | `id`(主键)、`name`(方案名称)、`resoure`(数据源名称)、`maintable`(主表名称) 等共 7 个字段 | [exp_dbdetail.md](./tables/集成模块/exp_dbdetail.md) |
| 66 | `exp_dbdetailtablesetting` | 9 | `id`(主键)、`dbsettingid`(数据库方案id)、`columnname`(字段名称)、`columntype`(字段类型) 等共 9 个字段 | [exp_dbdetailtablesetting.md](./tables/集成模块/exp_dbdetailtablesetting.md) |
| 67 | `exp_dbmaintablesetting` | 8 | `id`(主键)、`dbsettingid`(数据库方案id)、`columnname`(字段名称)、`columntype`(字段类型) 等共 8 个字段 | [exp_dbmaintablesetting.md](./tables/集成模块/exp_dbmaintablesetting.md) |
| 68 | `exp_dbprosettings` | 31 | `dwdmapfiletype`(流程表单文档)、`mwdmapfiletype`(流程表单多文档)、`remarkwdmapfiletype`(流转意见文档)、`remarkfjmapfiletype`(流转意见附件) 等共 31 个字段 | [exp_dbprosettings.md](./tables/集成模块/exp_dbprosettings.md) |
| 69 | `exp_fieldmap_cs` | 6 | `id`(主键)、`rgworkflowid`(注册流程列表里的id)、`fieldmapid`(转换规则id)、`fieldvalue`(值) 等共 6 个字段 | [exp_fieldmap_cs.md](./tables/集成模块/exp_fieldmap_cs.md) |
| 70 | `exp_ftpdetail` | 9 | `id`(主键)、`name`(ftp方案名称)、`adress`(ftp服务器地址)、`port`(ftp端口) 等共 9 个字段 | [exp_ftpdetail.md](./tables/集成模块/exp_ftpdetail.md) |
| 71 | `exp_localdetail` | 5 | `id`(主键)、`name`(方案名称)、`path`(文件保存路径)、`createdate`(方案创建日期) 等共 5 个字段 | [exp_localdetail.md](./tables/集成模块/exp_localdetail.md) |
| 72 | `exp_logdetail` | 10 | `id`(主键)、`requestname`(请求标题)、`requestid`(请求id)、`workflowid`(流程id) 等共 10 个字段 | [exp_logdetail.md](./tables/集成模块/exp_logdetail.md) |
| 73 | `exp_prolist` | 5 | `id`(主键)、`proname`(方案名称)、`proid`(方案信息表id)、`protype`(方案类型) 等共 5 个字段 | [exp_prolist.md](./tables/集成模块/exp_prolist.md) |
| 74 | `exp_wfdbmainfixfield` | 6 | `id`(主键)、`rgworkflowid`(注册流程列表里的id)、`expfieldname`(导出字段名称)、`expfieldtype`(导出字段类型) 等共 6 个字段 | [exp_wfdbmainfixfield.md](./tables/集成模块/exp_wfdbmainfixfield.md) |
| 75 | `exp_workflowdetail` | 7 | `id`(主键)、`workflowid`(流程id)、`workflowname`(流程名称)、`workflowtype`(流程类型) 等共 7 个字段 | [exp_workflowdetail.md](./tables/集成模块/exp_workflowdetail.md) |
| 76 | `exp_workflowfielddbmap` | 10 | `id`(主键)、`rgworkflowid`(注册流程列表里的id)、`fieldid`(流程表单字段id)、`fieldhtmltype`(表单字段html类型) 等共 10 个字段 | [exp_workflowfielddbmap.md](./tables/集成模块/exp_workflowfielddbmap.md) |
| 77 | `exp_workflowfieldxmlmap` | 8 | `id`(主键)、`rgworkflowid`(注册流程列表里的id)、`fieldid`(流程表单字段id)、`fieldhtmltype`(表单字段html类型) 等共 8 个字段 | [exp_workflowfieldxmlmap.md](./tables/集成模块/exp_workflowfieldxmlmap.md) |
| 78 | `exp_workflowxml` | 3 | `id`(主键)、`rgworkflowid`(注册流程列表里的id)、`xmltext`(xml格式内容) | [exp_workflowxml.md](./tables/集成模块/exp_workflowxml.md) |
| 79 | `exp_xmlprosettings` | 25 | `id`(主键)、`name`(方案名称)、`filesavetype`(文件保存方式)、`regittype`(方案类型) 等共 25 个字段 | [exp_xmlprosettings.md](./tables/集成模块/exp_xmlprosettings.md) |
| 80 | `formactionfieldmap` | 8 | `transttype`(规则转换类型)、`extrainfo`(规则转换补充值)、`id`(主键)、`actionsqlsetid`(接口id) 等共 8 个字段 | [formactionfieldmap.md](./tables/集成模块/formactionfieldmap.md) |
| 81 | `formactionsqlset` | 18 | `id`(主键)、`actionid`(接口id)、`actiontable`(表名)、`dmlformid`(表单id) 等共 18 个字段 | [formactionsqlset.md](./tables/集成模块/formactionsqlset.md) |
| 82 | `hrm_synts` | 3 | `id`(主键)、`synts`(上次同步时间)、`descstr`(同步详情描述) | [hrm_synts.md](./tables/集成模块/hrm_synts.md) |
| 83 | `hrmplancheck` | 4 | `id`(主键)、`type`(同步类型)、`cycle`(同步周期)、`plandate`(计划同步日期) | [hrmplancheck.md](./tables/集成模块/hrmplancheck.md) |
| 84 | `hrsyncset` | 35 | `pwdsynctype`(密码同步规则)、`issynrtx`(是否同步到rtx)、`id`(主键)、`isuselhr`(isuselhr) 等共 35 个字段 | [hrsyncset.md](./tables/集成模块/hrsyncset.md) |
| 85 | `hrsyncsetaddfield` | 4 | `id`(主键)、`tablename`(表名)、`fieldname`(字段名)、`labelid`(标签id) | [hrsyncsetaddfield.md](./tables/集成模块/hrsyncsetaddfield.md) |
| 86 | `hrsyncsetparam` | 13 | `id`(主键)、`type`(类型)、`oafield`(OA字段)、`outfield`(外部字段) 等共 13 个字段 | [hrsyncsetparam.md](./tables/集成模块/hrsyncsetparam.md) |
| 87 | `hrsyndetail` | 9 | `id`(主键)、`synid`(同步id)、`syntype`(同步类型)、`outpk`(中间表主键) 等共 9 个字段 | [hrsyndetail.md](./tables/集成模块/hrsyndetail.md) |
| 88 | `hrsynlog` | 8 | `id`(主键)、`startdate`(同步开始时间)、`enddate`(同步结束时间)、`synresult`(同步结果) 等共 8 个字段 | [hrsynlog.md](./tables/集成模块/hrsynlog.md) |
| 89 | `int_cas_exclueurl` | 3 | `id`(标识)、`ExcludeUrl`(排除地址)、`ExcludeDescription`(说明) | [int_cas_exclueurl.md](./tables/集成模块/int_cas_exclueurl.md) |
| 90 | `int_cas_exclueurl_sys` | 3 | `id`(标识)、`ExcludeUrl`(排除地址)、`ExcludeDescription`(说明) | [int_cas_exclueurl_sys.md](./tables/集成模块/int_cas_exclueurl_sys.md) |
| 91 | `int_cas_setting` | 9 | `IsUse`(启用)、`CasServerUrl`(CAS Server地址)、`CasServerLoginPage`(CAS Server登录地址)、`CasServerLogoutPage`(CAS Server退出地址) 等共 9 个字段 | [int_cas_setting.md](./tables/集成模块/int_cas_setting.md) |
| 92 | `int_webseal_exclueurl` | 4 | `Id`(标识)、`ExcludeUrl`(排除地址)、`ExcludeDescription`(说明)、`IsCustom`(是否自定义排出地址) | [int_webseal_exclueurl.md](./tables/集成模块/int_webseal_exclueurl.md) |
| 93 | `int_webseal_securityrules` | 3 | `Id`(标识)、`SecurityRule`(过滤地址)、`RuleDescription`(说明) | [int_webseal_securityrules.md](./tables/集成模块/int_webseal_securityrules.md) |
| 94 | `int_webseal_setting` | 7 | `IsUse`(启用)、`WebSealParamMethod`(WebSEAL参数获取方法)、`WebSealParamName`(参数名称)、`EcologyLoginPage`(Ecology登录地址) 等共 7 个字段 | [int_webseal_setting.md](./tables/集成模块/int_webseal_setting.md) |
| 95 | `ldap_formart` | 6 | `formartid`(标识)、`formartclass`(插件类名称)、`formartparams`(调用参数)、`formartname`(插件显示名称) 等共 6 个字段 | [ldap_formart.md](./tables/集成模块/ldap_formart.md) |
| 96 | `ldap_mapping` | 8 | `id`(主键)、`ldapid`(LDAP标识)、`attributename`(属性名)、`attributetype`(类别) 等共 8 个字段 | [ldap_mapping.md](./tables/集成模块/ldap_mapping.md) |
| 97 | `ldap_mapping_template` | 8 | `templateid`(标识)、`fieldkey`(字段标识)、`fieldname`(字段显示名称)、`datatype`(数据类型) 等共 8 个字段 | [ldap_mapping_template.md](./tables/集成模块/ldap_mapping_template.md) |
| 98 | `ldap_schedule` | 7 | `ldapid`(LDAP标识)、`synctype`(定时任务类型)、`lastsyncdate`(最后同步时间)、`scheduleid`(计划任务ID) 等共 7 个字段 | [ldap_schedule.md](./tables/集成模块/ldap_schedule.md) |
| 99 | `ldap_setting` | 23 | `ldapid`(标识)、`ldapname`(显示名称)、`isused`(是否启用)、`isadaccount`(是否开启LDAP认证) 等共 23 个字段 | [ldap_setting.md](./tables/集成模块/ldap_setting.md) |
| 100 | `ldap_sync` | 11 | `id`(主键)、`ldapid`(LDAP标识)、`syncorg`(是否同步组织架构)、`syncuser`(是否同步人员) 等共 11 个字段 | [ldap_sync.md](./tables/集成模块/ldap_sync.md) |
| 101 | `ldap_sync_data` | 6 | `ldapid`(LDAP标识)、`uuid`(LDAP数据唯一标识)、`rdn`(LDAP域地址)、`oaid`(OA唯一标识) 等共 6 个字段 | [ldap_sync_data.md](./tables/集成模块/ldap_sync_data.md) |
| 102 | `ldap_sync_logs` | 9 | `logId`(日志ID)、`ldapId`(LDAP标识)、`syncType`(同步类型)、`syncMode`(同步方式) 等共 9 个字段 | [ldap_sync_logs.md](./tables/集成模块/ldap_sync_logs.md) |
| 103 | `ldapimporttime` | 1 | `usertime`(上次同步时间) | [ldapimporttime.md](./tables/集成模块/ldapimporttime.md) |
| 104 | `ldapset` | 29 | `isnewguid`(是否用新guid)、`ldapsyncmethod`(同步方式)、`id`(主键)、`isuseldap`(是否启用) 等共 29 个字段 | [ldapset.md](./tables/集成模块/ldapset.md) |
| 105 | `ldapsetdepparam` | 3 | `id`(主键)、`depattr`(部门字段名称)、`ldapdepattr`(ldap属性名称) | [ldapsetdepparam.md](./tables/集成模块/ldapsetdepparam.md) |
| 106 | `ldapsetdetail` | 5 | `id`(主键)、`subcompanycode`(分部编码)、`subcomusertodepcode`(subcomusertodepcode)、`subcompanydomain`(同步域) 等共 5 个字段 | [ldapsetdetail.md](./tables/集成模块/ldapsetdetail.md) |
| 107 | `ldapsetoutype` | 4 | `id`(主键)、`ouattr`(LDAP组织架构类型属性)、`subcompany`(分部值)、`department`(部门值) | [ldapsetoutype.md](./tables/集成模块/ldapsetoutype.md) |
| 108 | `ldapsetsubparam` | 3 | `id`(主键)、`subattr`(分部字段名称)、`ldapsubattr`(ad里属性名称) | [ldapsetsubparam.md](./tables/集成模块/ldapsetsubparam.md) |
| 109 | `ofs_sendinfo` | 6 | `id`(流水号)、`syscode`(系统编号)、`serverurl`(系统访问地址)、`classimpl`(推送实现类) 等共 6 个字段 | [ofs_sendinfo.md](./tables/集成模块/ofs_sendinfo.md) |
| 110 | `ofs_sendinfodetail` | 4 | `id`(流水号)、`mainid`(推送设置ID)、`paramname`(参数名)、`paramvalue`(参数值) | [ofs_sendinfodetail.md](./tables/集成模块/ofs_sendinfodetail.md) |
| 111 | `ofs_senduser` | 7 | `id`(流水号)、`mainid`(推送设置ID)、`type`(对象类型)、`objid`(对象值) 等共 7 个字段 | [ofs_senduser.md](./tables/集成模块/ofs_senduser.md) |
| 112 | `ofs_sendworkflow` | 3 | `id`(流水号)、`mainid`(推送设置ID)、`workflowid`(流程ID) | [ofs_sendworkflow.md](./tables/集成模块/ofs_sendworkflow.md) |
| 113 | `ofs_setting` | 15 | `messagetypeid`(消息类型)、`remindemessage`(emessage消息推送开关)、`remindebridge`(ebridge消息推送开关)、`remindebridgetemplate`(ebridge消息消息模板) 等共 15 个字段 | [ofs_setting.md](./tables/集成模块/ofs_setting.md) |
| 114 | `ofs_sysinfo` | 22 | `pcouterfixurl`(异构系统外网访问地址)、`pcentranceurl`(pc中转页面地址)、`appentranceurl`(app中转页面地址)、`timezone_`(时区) 等共 22 个字段 | [ofs_sysinfo.md](./tables/集成模块/ofs_sysinfo.md) |
| 115 | `ofs_todo_data` | 29 | `receivets`(时间戳)、`pcurlsrc`(异构系统pc访问地址)、`appurlsrc`(异构系统移动端访问地址)、`isremark`(流程处理状态) 等共 29 个字段 | [ofs_todo_data.md](./tables/集成模块/ofs_todo_data.md) |
| 116 | `ofs_workflow` | 11 | `workflowid`(自增长序列（负增长）)、`sysid`(异构系统id)、`workflowname`(异构系统流程类型名称)、`receivewfdata`(接收流程数据) 等共 11 个字段 | [ofs_workflow.md](./tables/集成模块/ofs_workflow.md) |
| 117 | `outerdatawfdetail` | 6 | `outermaintable`(外部主表名称)、`mainid`(主键列名称)、`workflowid`(流程id)、`requestid`(请求id) 等共 6 个字段 | [outerdatawfdetail.md](./tables/集成模块/outerdatawfdetail.md) |
| 118 | `outerdatawflog` | 8 | `id`(自增长主键)、`outerdatawfid`(outerdatawset表id)、`outkey`(外部主键)、`workflowid`(流程id) 等共 8 个字段 | [outerdatawflog.md](./tables/集成模块/outerdatawflog.md) |
| 119 | `outerdatawfperiodset` | 10 | `periodvalue`(分钟值)、`scope`(触发周期应用范围)、`type`(周期类型)、`val2`(小时值) 等共 10 个字段 | [outerdatawfperiodset.md](./tables/集成模块/outerdatawfperiodset.md) |
| 120 | `outerdatawfset` | 27 | `id`(ID)、`setname`(名称)、`workflowid`(触发流程id)、`outermaintable`(外部主表名称) 等共 27 个字段 | [outerdatawfset.md](./tables/集成模块/outerdatawfset.md) |
| 121 | `outerdatawfsetdetail` | 17 | `id`(ID)、`mainid`(outerdatawfset表的id)、`wffieldid`(字段id)、`wffieldname`(字段数据库名) 等共 17 个字段 | [outerdatawfsetdetail.md](./tables/集成模块/outerdatawfsetdetail.md) |
| 122 | `outter_account` | 10 | `modifytime`(修改时间)、`pc_url`(pc端跳转地址)、`sysid`(标识)、`userid`(用户id) 等共 10 个字段 | [outter_account.md](./tables/集成模块/outter_account.md) |
| 123 | `outter_encryptclass` | 10 | `id`(主键)、`encryptclass`(算法类名)、`encryptmethod`(算法方法名)、`datatype`(数据类型) 等共 10 个字段 | [outter_encryptclass.md](./tables/集成模块/outter_encryptclass.md) |
| 124 | `outter_params` | 4 | `sysid`(标识)、`userid`(用户id)、`paramname`(参数表)、`paramvalue`(参数值) | [outter_params.md](./tables/集成模块/outter_params.md) |
| 125 | `outter_sys` | 48 | `id`(ID)、`isautosso`(是否自动单点登录)、`pc_url`(pc端url)、`sysid`(标识) 等共 48 个字段 | [outter_sys.md](./tables/集成模块/outter_sys.md) |
| 126 | `outter_sysparam` | 9 | `sysid`(标识)、`paramname`(参数名)、`paramvalue`(参数值)、`labelname`(标签名) 等共 9 个字段 | [outter_sysparam.md](./tables/集成模块/outter_sysparam.md) |
| 127 | `rtxsetting` | 18 | `rtxserverip`(RTX服务器地址)、`rtxserveroutip`(RTX服务器对外地址)、`rtxserverport`(RTX中间件端口号)、`domainname`(域名) 等共 18 个字段 | [rtxsetting.md](./tables/集成模块/rtxsetting.md) |
| 128 | `schedulesetting` | 9 | `id`(主键)、`pointid`(计划任务标识)、`classpath`(计划任务类)、`cronexpr`(定时时间) 等共 9 个字段 | [schedulesetting.md](./tables/集成模块/schedulesetting.md) |
| 129 | `schedulesettingdetail` | 5 | `id`(主键)、`scheduledbid`(计划任务id)、`attrname`(参数名称)、`attrvalue`(参数值) 等共 5 个字段 | [schedulesettingdetail.md](./tables/集成模块/schedulesettingdetail.md) |
| 130 | `shareoutter` | 9 | `id`(ID)、`sysid`(标识)、`type`(共享类型)、`content`(共享内容) 等共 9 个字段 | [shareoutter.md](./tables/集成模块/shareoutter.md) |
| 131 | `weaver_sso` | 6 | `isuse`(是否开启)、`sso_login_url`(登录地址)、`sso_loginout_url`(登出地址)、`rest_login_url`(rest登录地址) 等共 6 个字段 | [weaver_sso.md](./tables/集成模块/weaver_sso.md) |
| 132 | `weaver_sso_app` | 7 | `isuse`(是否使用)、`appid`(应用标识)、`appname`(应用名称)、`allow_ip`(允许ip) 等共 7 个字段 | [weaver_sso_app.md](./tables/集成模块/weaver_sso_app.md) |
| 133 | `wsformactionset` | 21 | `createdate`(创建日期)、`createtime`(创建时间)、`modifydate`(修改日期)、`modifytime`(修改时间) 等共 21 个字段 | [wsformactionset.md](./tables/集成模块/wsformactionset.md) |
| 134 | `wsregiste` | 4 | `id`(自增长主键)、`customcode`(自定义编码)、`customname`(自定义名称)、`webserviceurl`(webservice地址) | [wsregiste.md](./tables/集成模块/wsregiste.md) |
| 135 | `wsregistemethod` | 5 | `id`(自增长主键)、`mainid`(接口主键id)、`methodname`(方法名称)、`methoddesc`(方法描述) 等共 5 个字段 | [wsregistemethod.md](./tables/集成模块/wsregistemethod.md) |
| 136 | `wsregistemethodparam` | 5 | `id`(自增长主键)、`methodid`(方法主键id)、`paramname`(参数名称)、`paramtype`(参数类型) 等共 5 个字段 | [wsregistemethodparam.md](./tables/集成模块/wsregistemethodparam.md) |

### 财务管理

> 本模块共收录 `133` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `FnaCostCenter` | 7 | `id`(主键)、`supfccid`(上级id)、`type`(类型)、`name`(名称) 等共 7 个字段 | [FnaCostCenter.md](./tables/财务管理/FnaCostCenter.md) |
| 2 | `FnaCostCenterDtl` | 5 | `objvalue`(自定义浏览按钮id)、`id`(主键)、`fccid`(成本中心id)、`type`(关联对象类型) 等共 5 个字段 | [FnaCostCenterDtl.md](./tables/财务管理/FnaCostCenterDtl.md) |
| 3 | `airdtlinvoice` | 8 | `id`(主键)、`mainid`(发票台账id)、`from_city`(出发站)、`to_city`(到达站) 等共 8 个字段 | [airdtlinvoice.md](./tables/财务管理/airdtlinvoice.md) |
| 4 | `airinvoice` | 10 | `id`(主键)、`mainid`(发票台账id)、`user_name`(乘机人姓名)、`user_id`(身份证号) 等共 10 个字段 | [airinvoice.md](./tables/财务管理/airinvoice.md) |
| 5 | `bill_fnabudget` | 3 | `id`(主键)、`budgetdetail`(fanbudgetinfo.id)、`requestid`(reqid) | [bill_fnabudget.md](./tables/财务管理/bill_fnabudget.md) |
| 6 | `bill_fnabudgetchgapply` | 6 | `id`(主键)、`applicant`(申请人)、`deptid`(申请人部门)、`applydate`(费用日期) 等共 6 个字段 | [bill_fnabudgetchgapply.md](./tables/财务管理/bill_fnabudgetchgapply.md) |
| 7 | `bill_fnabudgetchgapplydetail` | 13 | `id`(bill_fnabudgetchgapply.id)、`organizationid`(承担主体)、`subject`(科目)、`budgetperiod`(费用日期) 等共 13 个字段 | [bill_fnabudgetchgapplydetail.md](./tables/财务管理/bill_fnabudgetchgapplydetail.md) |
| 8 | `bill_fnaloanapply` | 11 | `id`(主键)、`applicant`(借款人)、`deptid`(借款人部门)、`reason`(理由) 等共 11 个字段 | [bill_fnaloanapply.md](./tables/财务管理/bill_fnaloanapply.md) |
| 9 | `bill_fnaloanapplydetail` | 8 | `id`(主表主键)、`organizationid`(承担主体id)、`relatedprj`(相关项目)、`relatedcrm`(相关客户) 等共 8 个字段 | [bill_fnaloanapplydetail.md](./tables/财务管理/bill_fnaloanapplydetail.md) |
| 10 | `bill_fnapayapply` | 10 | `id`(主键)、`applicant`(申请人id)、`deptid`(申请人部门)、`reason`(说明) 等共 10 个字段 | [bill_fnapayapply.md](./tables/财务管理/bill_fnapayapply.md) |
| 11 | `bill_fnapayapplydetail` | 15 | `id`(主键)、`organizationid`(承担主体)、`subject`(科目)、`budgetperiod`(费用日期) 等共 15 个字段 | [bill_fnapayapplydetail.md](./tables/财务管理/bill_fnapayapplydetail.md) |
| 12 | `bill_fnawipeapply` | 11 | `id`(主键)、`applicant`(申请人)、`deptid`(申请人部门)、`wipetype`(作废) 等共 11 个字段 | [bill_fnawipeapply.md](./tables/财务管理/bill_fnawipeapply.md) |
| 13 | `bill_fnawipeapplydetail` | 17 | `relatedcrm`(相关客户)、`description`(说明)、`applyamount`(审批金额)、`amount`(申请季节) 等共 17 个字段 | [bill_fnawipeapplydetail.md](./tables/财务管理/bill_fnawipeapplydetail.md) |
| 14 | `carinvoice` | 6 | `id`(主键)、`mainid`(发票台账id)、`time`(时间)、`station_geton`(出发车站) 等共 6 个字段 | [carinvoice.md](./tables/财务管理/carinvoice.md) |
| 15 | `fnaadvanceinfo` | 12 | `id`(主键)、`requestid`(流程id)、`dtlnumber`(明细表序号)、`dtlid`(明细表记录id) 等共 12 个字段 | [fnaadvanceinfo.md](./tables/财务管理/fnaadvanceinfo.md) |
| 16 | `fnaadvanceinfoamountlog` | 16 | `id`(主键)、`requestid`(流程id)、`dtlnumber`(明细表序号)、`dtlid`(明细表记录id) 等共 16 个字段 | [fnaadvanceinfoamountlog.md](./tables/财务管理/fnaadvanceinfoamountlog.md) |
| 17 | `fnabatch4impfnabudget` | 3 | `guid1`(主键)、`id`(主键)、`budgetaccount`(金额) | [fnabatch4impfnabudget.md](./tables/财务管理/fnabatch4impfnabudget.md) |
| 18 | `fnabatch4subject` | 17 | `groupdispalyorder`(分组显示排序)、`budgetaccount`(预算金额)、`str4k`(字符串)、`str4k01`(字符串1) 等共 17 个字段 | [fnabatch4subject.md](./tables/财务管理/fnabatch4subject.md) |
| 19 | `fnaborrowinfo` | 15 | `createdate`(创建日期)、`createtime`(创建时间)、`recordtype`(记录类型)、`applicantid`(申请人id) 等共 15 个字段 | [fnaborrowinfo.md](./tables/财务管理/fnaborrowinfo.md) |
| 20 | `fnaborrowinfoamountlog` | 16 | `id`(主键)、`requestid`(流程requestid)、`dtlnumber`(明细表序号)、`dtlid`(明细表记录id) 等共 16 个字段 | [fnaborrowinfoamountlog.md](./tables/财务管理/fnaborrowinfoamountlog.md) |
| 21 | `fnabrowslastsearchresult` | 5 | `idfk`(科目id)、`charfk`(作废)、`browsertype`(浏览按钮类型)、`userid`(oa用户id) 等共 5 个字段 | [fnabrowslastsearchresult.md](./tables/财务管理/fnabrowslastsearchresult.md) |
| 22 | `fnabudgetassistant` | 6 | `eid`(元素id)、`ebaseid`(ebaseid)、`hpid`(主页id)、`grjk`(显示个人借款) 等共 6 个字段 | [fnabudgetassistant.md](./tables/财务管理/fnabudgetassistant.md) |
| 23 | `fnabudgetassistant1` | 7 | `eid`(元素id)、`ebaseid`(ebaseid)、`hpid`(主页id)、`hrm`(显示：个人信息) 等共 7 个字段 | [fnabudgetassistant1.md](./tables/财务管理/fnabudgetassistant1.md) |
| 24 | `fnabudgetfeetype` | 24 | `groupctrlguid`(当前科目所属统一费控预算科目的GUID标识)、`displayorder`(显示顺序)、`groupctrlid`(当前科目所属统一费控预算科目的id)、`iseditfeetypeguid`(当前科目所属可编制预算科目的GUID标识) 等共 24 个字段 | [fnabudgetfeetype.md](./tables/财务管理/fnabudgetfeetype.md) |
| 25 | `fnabudgetfeetypecge` | 2 | `mainsubjectid`(上级统一费控科目)、`subjectid`(例外科目) | [fnabudgetfeetypecge.md](./tables/财务管理/fnabudgetfeetypecge.md) |
| 26 | `fnabudgetfeetyperuleset` | 4 | `id`(主键)、`mainid`(科目id)、`type`(组织单位类型)、`orgid`(组织单位id) | [fnabudgetfeetyperuleset.md](./tables/财务管理/fnabudgetfeetyperuleset.md) |
| 27 | `fnabudgetfeetypeused` | 3 | `subjectid`(科目)、`userid`(oa用户)、`orderid`(排序) | [fnabudgetfeetypeused.md](./tables/财务管理/fnabudgetfeetypeused.md) |
| 28 | `fnabudgetinfo` | 15 | `description1`(备注信息)、`id`(主键)、`budgetstatus`(预算状态)、`createrid`(创建人id) 等共 15 个字段 | [fnabudgetinfo.md](./tables/财务管理/fnabudgetinfo.md) |
| 29 | `fnabudgetinfodetail` | 11 | `id`(主键)、`budgetinfoid`(部门预算信息id)、`budgetperiods`(年度期间id)、`budgettypeid`(科目id) 等共 11 个字段 | [fnabudgetinfodetail.md](./tables/财务管理/fnabudgetinfodetail.md) |
| 30 | `fnabudgetinfopagesize` | 3 | `id`(主键)、`userid`(oa用户)、`pagesize`(每页显示记录数量) | [fnabudgetinfopagesize.md](./tables/财务管理/fnabudgetinfopagesize.md) |
| 31 | `fnacommoninfo` | 2 | `valtype`(通用信息类型)、`valstr`(通用信息字符串内容) | [fnacommoninfo.md](./tables/财务管理/fnacommoninfo.md) |
| 32 | `fnacontrolscheme` | 6 | `id`(主键)、`name`(方案名称)、`code`(方案编码)、`fnayearid`(预算年度开始) 等共 6 个字段 | [fnacontrolscheme.md](./tables/财务管理/fnacontrolscheme.md) |
| 33 | `fnacontrolscheme_feewfinfo` | 2 | `fnacontrolschemeid`(预算方案id)、`fnafeewfinfoid`(费控流程id) | [fnacontrolscheme_feewfinfo.md](./tables/财务管理/fnacontrolscheme_feewfinfo.md) |
| 34 | `fnacontrolschemedtl` | 11 | `id`(主键)、`mainid`(预算方案id)、`kmidscondition`(预算科目)、`kmids`(科目id) 等共 11 个字段 | [fnacontrolschemedtl.md](./tables/财务管理/fnacontrolschemedtl.md) |
| 35 | `fnacoststandard` | 10 | `fielddbtype`(表现形式-小类型-自定义按钮类型值)、`guid1`(主键)、`name`(名称)、`paramtype`(表现形式-大类型) 等共 10 个字段 | [fnacoststandard.md](./tables/财务管理/fnacoststandard.md) |
| 36 | `fnacoststandarddefi` | 4 | `guid1`(主键)、`fcsdname`(费用标准额度名称)、`csamount`(费用标准额度)、`ordernumber`(顺序) | [fnacoststandarddefi.md](./tables/财务管理/fnacoststandarddefi.md) |
| 37 | `fnacoststandarddefidtl` | 4 | `guid1`(主键)、`fcsguid1`(fcsGuid1)、`fcsdguid1`(fcsdguid1)、`valchar`(维度调制值) | [fnacoststandarddefidtl.md](./tables/财务管理/fnacoststandarddefidtl.md) |
| 38 | `fnacreatexmlsqllog` | 3 | `id`(主键)、`guid1`(uuid)、`exesql`(执行的sql) | [fnacreatexmlsqllog.md](./tables/财务管理/fnacreatexmlsqllog.md) |
| 39 | `fnacurrency` | 5 | `id`(ID)、`currencyname`(币种名称)、`currencydesc`(币种描述)、`activable`(币种活跃性) 等共 5 个字段 | [fnacurrency.md](./tables/财务管理/fnacurrency.md) |
| 40 | `fnacurrencyexchange` | 8 | `id`(ID)、`defcurrencyid`(基准币种)、`thecurrencyid`(换算币种)、`fnayear`(会计年度) 等共 8 个字段 | [fnacurrencyexchange.md](./tables/财务管理/fnacurrencyexchange.md) |
| 41 | `fnadataset` | 7 | `id`(主键)、`dsetname`(数据集名称)、`datasourcename`(数据源名称)、`dsmemo`(备注) 等共 7 个字段 | [fnadataset.md](./tables/财务管理/fnadataset.md) |
| 42 | `fnaexpenseinfo` | 26 | `isbudgetautomovebyminusamt`(超额结转标识)、`sfbxwc`(是否报销完成标识)、`writeoffflag`(预申请费用是否冲销完成)、`id`(主键) 等共 26 个字段 | [fnaexpenseinfo.md](./tables/财务管理/fnaexpenseinfo.md) |
| 43 | `fnafeetypewfbrowdef` | 6 | `id`(主键)、`workflowid`(wfid)、`fieldid`(字段id)、`viewtype`(显示类型) 等共 6 个字段 | [fnafeetypewfbrowdef.md](./tables/财务管理/fnafeetypewfbrowdef.md) |
| 44 | `fnafeetypewfbrowdef_dt1` | 3 | `id`(主键)、`mainid`(浏览按钮报销费用类型应用过滤定义表.id)、`refid`(报销费用类型id（科目id）) | [fnafeetypewfbrowdef_dt1.md](./tables/财务管理/fnafeetypewfbrowdef_dt1.md) |
| 45 | `fnafeewfinfo` | 15 | `fnawftypereverseadvance`(启用预申请业务逻辑)、`budgetcanbenegative`(报销金额可为负数)、`id`(主键)、`workflowid`(流程workflowid) 等共 15 个字段 | [fnafeewfinfo.md](./tables/财务管理/fnafeewfinfo.md) |
| 46 | `fnafeewfinfocoststandard` | 6 | `id`(主键)、`workflowid`(wfid)、`enable`(是否启用)、`fnawftype`(财务流程类型) 等共 6 个字段 | [fnafeewfinfocoststandard.md](./tables/财务管理/fnafeewfinfocoststandard.md) |
| 47 | `fnafeewfinfofield` | 14 | `iswffieldlinkage`(（作废）)、`controlflowsubmission`(预申请流程是否：控制流程提交)、`automatictake`(报销流程中 是否在对应字段 【承担主体】 中带出带出 当前登录人员的)、`controlborrowingwf`(还款（报销）流程中 是否通过申请人来进行 可选借款流程过滤) 等共 14 个字段 | [fnafeewfinfofield.md](./tables/财务管理/fnafeewfinfofield.md) |
| 48 | `fnafeewfinfofieldcoststandard` | 15 | `id`(主键)、`mainid`(fnafeewfinfocoststandard.id)、`workflowid`(wfid)、`formid`(表单id) 等共 15 个字段 | [fnafeewfinfofieldcoststandard.md](./tables/财务管理/fnafeewfinfofieldcoststandard.md) |
| 49 | `fnafeewfinfologic` | 13 | `id`(主键)、`mainid`(主表主键)、`kmidscondition`(预算科目)、`kmids`(科目id) 等共 13 个字段 | [fnafeewfinfologic.md](./tables/财务管理/fnafeewfinfologic.md) |
| 50 | `fnafeewfinfologicadvancer` | 27 | `id`(主键)、`mainid`(fnafeewfinfoadvancer.id)、`rule1`(规则1)、`rule1intensity`(规则1强度) 等共 27 个字段 | [fnafeewfinfologicadvancer.md](./tables/财务管理/fnafeewfinfologicadvancer.md) |
| 51 | `fnafeewfinfologicreverse` | 27 | `id`(主键)、`mainid`(主表主键)、`rule1`(规则1)、`rule1intensity`(规则强度1) 等共 27 个字段 | [fnafeewfinfologicreverse.md](./tables/财务管理/fnafeewfinfologicreverse.md) |
| 52 | `fnafeewfinfonodectrl` | 4 | `id`(主键)、`mainid`(fnaFeeWfInfo.id)、`nodeid`(流程节点id)、`checkway`(流程节点类型) | [fnafeewfinfonodectrl.md](./tables/财务管理/fnafeewfinfonodectrl.md) |
| 53 | `fnafinancesetting` | 11 | `guid1`(主键)、`fnavoucherxmlid`(fnavoucherxml.id)、`fieldname`(字段名称)、`fieldvaluetype1`(字段值类型1) 等共 11 个字段 | [fnafinancesetting.md](./tables/财务管理/fnafinancesetting.md) |
| 54 | `fnagrowcode` | 3 | `id`(主键)、`invoicetype`(OCR票据识别类型)、`code`(OCR票据识别类型编号) | [fnagrowcode.md](./tables/财务管理/fnagrowcode.md) |
| 55 | `fnainitdatatb` | 2 | `typename`(预算初始化数据名称)、`result1`(是否执行) | [fnainitdatatb.md](./tables/财务管理/fnainitdatatb.md) |
| 56 | `fnainitsetoplog` | 11 | `userid`(oa用户id)、`ip`(ip地址)、`fnabktbname`(备份数据表名后缀)、`subject`(本次操作是否初始化：科目) 等共 11 个字段 | [fnainitsetoplog.md](./tables/财务管理/fnainitsetoplog.md) |
| 57 | `fnainvoicecheckfaillog` | 11 | `id`(主键)、`checktime`(错误出现时间)、`checkdate`(错误出现日期)、`requestid`(流程requestid) 等共 11 个字段 | [fnainvoicecheckfaillog.md](./tables/财务管理/fnainvoicecheckfaillog.md) |
| 58 | `fnainvoicefeewfinfologic` | 3 | `id`(主键)、`mainid`(fnainvoicewfinfo.id)、`promptsc`(自定义发票流程超额提醒信息) | [fnainvoicefeewfinfologic.md](./tables/财务管理/fnainvoicefeewfinfologic.md) |
| 59 | `fnainvoiceinterface` | 16 | `tokenurl`(获取token的接口地址)、`openidurl`(获取openid的接口地址)、`client_id`(企业client_id)、`client_secret`(client_id密钥) 等共 16 个字段 | [fnainvoiceinterface.md](./tables/财务管理/fnainvoiceinterface.md) |
| 60 | `fnainvoiceledger` | 27 | `imageid`(OCR图片id)、`purchasertaxno`(买方税号)、`salestaxno`(买房税号)、`userid_new`(发票归属人) 等共 27 个字段 | [fnainvoiceledger.md](./tables/财务管理/fnainvoiceledger.md) |
| 61 | `fnainvoiceledgerdetail` | 8 | `unitnumber`(数量)、`unitprice`(单价)、`id`(主键)、`mainid`(主表id（发票台账表id）) 等共 8 个字段 | [fnainvoiceledgerdetail.md](./tables/财务管理/fnainvoiceledgerdetail.md) |
| 62 | `fnainvoicelog` | 7 | `msg`(错误信息)、`ocrtype`(接口类型)、`id`(主键)、`interfacetype`(调用接口类型) 等共 7 个字段 | [fnainvoicelog.md](./tables/财务管理/fnainvoicelog.md) |
| 63 | `fnainvoicesubject` | 5 | `id`(主键)、`invoiceserviceyype`(货物或应税服务类型)、`subjectid`(科目id)、`lastmodifytime`(最后修改时间) 等共 5 个字段 | [fnainvoicesubject.md](./tables/财务管理/fnainvoicesubject.md) |
| 64 | `fnainvoicewfinfo` | 4 | `id`(主键)、`workflowid`(wfid)、`enable`(是否启用)、`lastmodifieddate`(最后修改日期) | [fnainvoicewfinfo.md](./tables/财务管理/fnainvoicewfinfo.md) |
| 65 | `fnainvoicewfinfofield` | 9 | `fieldid`(字段id)、`fieldname`(字段数据库名)、`tabindex`(页签顺序)、`dtlnumber`(明细表id) 等共 9 个字段 | [fnainvoicewfinfofield.md](./tables/财务管理/fnainvoicewfinfofield.md) |
| 66 | `fnaloaninfo` | 12 | `id`(主键)、`loantype`(来源)、`organizationid`(组织id)、`organizationtype`(组织类型) 等共 12 个字段 | [fnaloaninfo.md](./tables/财务管理/fnaloaninfo.md) |
| 67 | `fnaloanlog` | 14 | `id`(ID)、`loantypeid`(还款方式)、`resourceid`(还款人)、`departmentid`(部门id) 等共 14 个字段 | [fnaloanlog.md](./tables/财务管理/fnaloanlog.md) |
| 68 | `fnalog` | 10 | `log_user`(操作人)、`log_date`(操作日期)、`log_time`(操作时间)、`log_seqid`(排序列) 等共 10 个字段 | [fnalog.md](./tables/财务管理/fnalog.md) |
| 69 | `fnalogdtl` | 9 | `log_uuid_td1`(主键)、`main_uuid`(日志主表id)、`log_column`(修改数据的列名称)、`log_before_revision`(修改前内容) 等共 9 个字段 | [fnalogdtl.md](./tables/财务管理/fnalogdtl.md) |
| 70 | `fnalogoccurredexpensebatch` | 18 | `id`(主键)、`batchguid`(导入批次guid)、`tablename`(表名)、`organizationid`(承担主体id) 等共 18 个字段 | [fnalogoccurredexpensebatch.md](./tables/财务管理/fnalogoccurredexpensebatch.md) |
| 71 | `fnalogoccurredloanbatch` | 15 | `id`(主键)、`batchguid`(批次uuid)、`tablename`(表名)、`requestid`(流程id) 等共 15 个字段 | [fnalogoccurredloanbatch.md](./tables/财务管理/fnalogoccurredloanbatch.md) |
| 72 | `fnamobileerrormsg` | 4 | `id`(主键)、`userid`(oa人员id)、`requestid`(流程id)、`msg`(错误信息) | [fnamobileerrormsg.md](./tables/财务管理/fnamobileerrormsg.md) |
| 73 | `fnarptruleset` | 8 | `allowrptnames`(允许报表标识名)、`id`(主键)、`roleid`(角色id)、`allowzb`(是否有总部权限) 等共 8 个字段 | [fnarptruleset.md](./tables/财务管理/fnarptruleset.md) |
| 74 | `fnarptrulesetdtl` | 4 | `id`(主键)、`mainid`(FnaRptRuleSet表pk)、`showid`(权限id类型)、`showidtype`(权限id) | [fnarptrulesetdtl.md](./tables/财务管理/fnarptrulesetdtl.md) |
| 75 | `fnaruleset` | 7 | `allowfb`(是否允许分部)、`allowbm`(是否允许部门)、`allowfcc`(是否允许成本中心)、`id`(主键) 等共 7 个字段 | [fnaruleset.md](./tables/财务管理/fnaruleset.md) |
| 76 | `fnarulesetdtl` | 4 | `id`(主键)、`mainid`(主表主键)、`showid`(部门id)、`showidtype`(类型) | [fnarulesetdtl.md](./tables/财务管理/fnarulesetdtl.md) |
| 77 | `fnasynchronized` | 6 | `lockstr`(锁定字符串)、`lockguid`(锁定uuid)、`userid`(oa用户id)、`memo`(备注) 等共 6 个字段 | [fnasynchronized.md](./tables/财务管理/fnasynchronized.md) |
| 78 | `fnasystemset` | 42 | `optionalsubject`(科目浏览按钮可选科目规则)、`wfdtlimprole4subject`(科目字段流程明细导入规则)、`wfdtlimprole4fcc`(成本中心字段流程明细导入规则)、`costcontrolcycle`(费用控制周期) 等共 42 个字段 | [fnasystemset.md](./tables/财务管理/fnasystemset.md) |
| 79 | `fnatmptblog` | 11 | `id`(主键)、`rpttypename`(报表类型标识)、`guid1`(记录唯一标识)、`istemp`(是否临时查询结果) 等共 11 个字段 | [fnatmptblog.md](./tables/财务管理/fnatmptblog.md) |
| 80 | `fnatmptblogcolinfo` | 6 | `id`(主键)、`guid1`(主表唯一标识)、`coldbname`(数据库列名)、`coltype`(列名称值类型名称) 等共 6 个字段 | [fnatmptblogcolinfo.md](./tables/财务管理/fnatmptblogcolinfo.md) |
| 81 | `fnatmptblogshare` | 8 | `id`(主键)、`fnatmptblogid`(财务报表历史查询结果记录表id)、`groupguid1`(共享记录分组标识)、`sharetype`(共享对象类型) 等共 8 个字段 | [fnatmptblogshare.md](./tables/财务管理/fnatmptblogshare.md) |
| 82 | `fnavoucherobjinfo` | 18 | `id`(主键)、`fnavoucherinittypestr`(凭证初始化类型字符串)、`displayorder`(显示顺序)、`fieldname`(字段名) 等共 18 个字段 | [fnavoucherobjinfo.md](./tables/财务管理/fnavoucherobjinfo.md) |
| 83 | `fnavoucherxml` | 11 | `id`(主键)、`xmlname`(名称)、`xmlmemo`(备注)、`xmlversion`(版本号) 等共 11 个字段 | [fnavoucherxml.md](./tables/财务管理/fnavoucherxml.md) |
| 84 | `fnavoucherxmlcontent` | 13 | `id`(主键)、`fnavoucherxmlid`(fnavoucherxml.id)、`contenttype`(节点类型)、`contentparentid`(节点父id) 等共 13 个字段 | [fnavoucherxmlcontent.md](./tables/财务管理/fnavoucherxmlcontent.md) |
| 85 | `fnavoucherxmlcontentdset` | 9 | `id`(主键)、`fnavoucherxmlid`(fnavoucherxml.id)、`fnavoucherxmlcontentid`(fnavoucherxmlcontent.id)、`dsetalias`(数据集别名) 等共 9 个字段 | [fnavoucherxmlcontentdset.md](./tables/财务管理/fnavoucherxmlcontentdset.md) |
| 86 | `fnawfrequestidlog` | 4 | `requestid`(reqid)、`wffnatype`(预算action类型)、`lockdate`(触发日期)、`locktime`(触发时间) | [fnawfrequestidlog.md](./tables/财务管理/fnawfrequestidlog.md) |
| 87 | `fnayearsperiods` | 6 | `id`(主键)、`fnayear`(年度)、`startdate`(开始日期)、`enddate`(结束日期) 等共 6 个字段 | [fnayearsperiods.md](./tables/财务管理/fnayearsperiods.md) |
| 88 | `fnayearsperiodslist` | 10 | `status`(账期状态)、`id`(主键)、`fnayearid`(主表主键)、`periodsid`(期间id) 等共 10 个字段 | [fnayearsperiodslist.md](./tables/财务管理/fnayearsperiodslist.md) |
| 89 | `machineinvoice` | 6 | `id`(主键)、`mainid`(发票台账id)、`time`(时间)、`category`(种类) 等共 6 个字段 | [machineinvoice.md](./tables/财务管理/machineinvoice.md) |
| 90 | `motor_vehicleinvoice` | 13 | `id`(主键)、`mainid`(发票台账id)、`machine_code`(机打代码)、`machine_number`(机打号码) 等共 13 个字段 | [motor_vehicleinvoice.md](./tables/财务管理/motor_vehicleinvoice.md) |
| 91 | `second_carinvoice` | 10 | `id`(主键)、`mainid`(发票台账id)、`seller_id`(卖方单位代码/个人身份证号)、`buyer_id`(买方单位代码/个人身份证号) 等共 10 个字段 | [second_carinvoice.md](./tables/财务管理/second_carinvoice.md) |
| 92 | `smallinvoice` | 9 | `discount`(折扣)、`id`(主键)、`mainid`(发票台账id)、`storename`(店名) 等共 9 个字段 | [smallinvoice.md](./tables/财务管理/smallinvoice.md) |
| 93 | `taxiinvoice` | 5 | `id`(主键)、`mainid`(发票台账id)、`time_geton`(上车时间)、`time_getoff`(下车时间) 等共 5 个字段 | [taxiinvoice.md](./tables/财务管理/taxiinvoice.md) |
| 94 | `tollinvoice` | 5 | `id`(主键)、`mainid`(发票台账id)、`time`(时间)、`entrance`(入口) 等共 5 个字段 | [tollinvoice.md](./tables/财务管理/tollinvoice.md) |
| 95 | `traininvoice` | 8 | `station_getoff`(下车车站)、`train_number`(车次)、`seat`(座位类型)、`id`(主键) 等共 8 个字段 | [traininvoice.md](./tables/财务管理/traininvoice.md) |
| 96 | `wf_fna_fbft_imp` | 17 | `impguid1`(FnaBudgetfeeType表对应字段)、`id`(FnaBudgetfeeType表对应字段)、`name`(FnaBudgetfeeType表对应字段)、`description`(FnaBudgetfeeType表对应字段) 等共 17 个字段 | [wf_fna_fbft_imp.md](./tables/财务管理/wf_fna_fbft_imp.md) |
| 97 | `wf_fna_fcc_imp` | 8 | `id`(FnaCostCenter表对应字段)、`supfccid`(FnaCostCenter表对应字段)、`type`(FnaCostCenter表对应字段)、`name`(FnaCostCenter表对应字段) 等共 8 个字段 | [wf_fna_fcc_imp.md](./tables/财务管理/wf_fna_fcc_imp.md) |
| 98 | `wf_fna_ffi_imp` | 15 | `id`(fnafeewfinfo表对应字段)、`workflowid`(fnafeewfinfo表对应字段)、`enable`(fnafeewfinfo表对应字段)、`lastmodifieddate`(fnafeewfinfo表对应字段) 等共 15 个字段 | [wf_fna_ffi_imp.md](./tables/财务管理/wf_fna_ffi_imp.md) |
| 99 | `wf_fna_ffic_imp` | 5 | `id`(fnafeewfinfonodectrl表对应字段)、`mainid`(fnafeewfinfonodectrl表对应字段)、`nodeid`(fnafeewfinfonodectrl表对应字段)、`checkway`(fnafeewfinfonodectrl表对应字段) 等共 5 个字段 | [wf_fna_ffic_imp.md](./tables/财务管理/wf_fna_ffic_imp.md) |
| 100 | `wf_fna_ffif_imp` | 16 | `impguid1`(fnafeewfinfofield表对应字段)、`id`(fnafeewfinfofield表对应字段)、`mainid`(fnafeewfinfofield表对应字段)、`workflowid`(fnafeewfinfofield表对应字段) 等共 16 个字段 | [wf_fna_ffif_imp.md](./tables/财务管理/wf_fna_ffif_imp.md) |
| 101 | `wf_fna_ffilar_imp` | 28 | `id`(fnaFeeWfInfoLogicAdvanceR表对应字段)、`mainid`(fnaFeeWfInfoLogicAdvanceR表对应字段)、`rule1`(fnaFeeWfInfoLogicAdvanceR表对应字段)、`rule1intensity`(fnaFeeWfInfoLogicAdvanceR表对应字段) 等共 28 个字段 | [wf_fna_ffilar_imp.md](./tables/财务管理/wf_fna_ffilar_imp.md) |
| 102 | `wf_fna_ffilr_imp` | 28 | `impguid1`(fnafeewfinfologicreverse表对应字段)、`id`(fnafeewfinfologicreverse表对应字段)、`mainid`(fnafeewfinfologicreverse表对应字段)、`rule1`(fnafeewfinfologicreverse表对应字段) 等共 28 个字段 | [wf_fna_ffilr_imp.md](./tables/财务管理/wf_fna_ffilr_imp.md) |
| 103 | `wf_fna_implog` | 1 | `isinited`(是否完成全部初始化导入) | [wf_fna_implog.md](./tables/财务管理/wf_fna_implog.md) |
| 104 | `wf_fna_initwfinfo` | 4 | `workflowid`(wfid)、`formid`(表单id)、`fnawftype1`(财务流程类型1)、`fnawftype2`(财务流程类型2) | [wf_fna_initwfinfo.md](./tables/财务管理/wf_fna_initwfinfo.md) |
| 105 | `wf_fna_labelidx_imp` | 3 | `id`(HtmlLabelIndex表对应字段)、`indexdesc`(HtmlLabelIndex表对应字段)、`impguid1`(HtmlLabelIndex表对应字段) | [wf_fna_labelidx_imp.md](./tables/财务管理/wf_fna_labelidx_imp.md) |
| 106 | `wf_fna_labelinfo_imp` | 4 | `indexid`(HtmlLabelInfo表对应字段)、`labelname`(HtmlLabelInfo表对应字段)、`languageid`(HtmlLabelInfo表对应字段)、`impguid1`(HtmlLabelInfo表对应字段) | [wf_fna_labelinfo_imp.md](./tables/财务管理/wf_fna_labelinfo_imp.md) |
| 107 | `wf_fna_nfa_imp` | 11 | `id`(workflow_nodefieldattr表对应字段)、`fieldid`(workflow_nodefieldattr表对应字段)、`formid`(workflow_nodefieldattr表对应字段)、`isbill`(workflow_nodefieldattr表对应字段) 等共 11 个字段 | [wf_fna_nfa_imp.md](./tables/财务管理/wf_fna_nfa_imp.md) |
| 108 | `wf_fna_nfg_imp` | 13 | `impguid1`(workflow_NodeFormGroup表对应字段)、`nodeid`(workflow_NodeFormGroup表对应字段)、`groupid`(workflow_NodeFormGroup表对应字段)、`isadd`(workflow_NodeFormGroup表对应字段) 等共 13 个字段 | [wf_fna_nfg_imp.md](./tables/财务管理/wf_fna_nfg_imp.md) |
| 109 | `wf_fna_rb_imp` | 10 | `impguid1`(rule_base表对应字段)、`condit_temp`(rule_base表对应字段)、`id`(rule_base表对应字段)、`rulesrc`(rule_base表对应字段) 等共 10 个字段 | [wf_fna_rb_imp.md](./tables/财务管理/wf_fna_rb_imp.md) |
| 110 | `wf_fna_re_imp` | 6 | `impguid1`(rule_expressions表对应字段)、`id`(rule_expressions表对应字段)、`ruleid`(rule_expressions表对应字段)、`relation`(rule_expressions表对应字段) 等共 6 个字段 | [wf_fna_re_imp.md](./tables/财务管理/wf_fna_re_imp.md) |
| 111 | `wf_fna_reb_imp` | 21 | `impguid1`(rule_expressionbase表对应字段)、`id`(rule_expressionbase表对应字段)、`ruleid`(rule_expressionbase表对应字段)、`datafield`(rule_expressionbase表对应字段) 等共 21 个字段 | [wf_fna_reb_imp.md](./tables/财务管理/wf_fna_reb_imp.md) |
| 112 | `wf_fna_rmi_imp` | 10 | `impguid1`(rule_mapitem表对应字段)、`id`(rule_mapitem表对应字段)、`ruleid`(rule_mapitem表对应字段)、`rulesrc`(rule_mapitem表对应字段) 等共 10 个字段 | [wf_fna_rmi_imp.md](./tables/财务管理/wf_fna_rmi_imp.md) |
| 113 | `wf_fna_rml_imp` | 10 | `impguid1`(rule_maplist表对应字段)、`isused`(rule_maplist表对应字段)、`rulesrc`(rule_maplist表对应字段)、`nm`(rule_maplist表对应字段) 等共 10 个字段 | [wf_fna_rml_imp.md](./tables/财务管理/wf_fna_rml_imp.md) |
| 114 | `wf_fna_waction_imp` | 12 | `impguid1`(workflowactionset表对应字段)、`id`(workflowactionset表对应字段)、`actionname`(workflowactionset表对应字段)、`workflowid`(workflowactionset表对应字段) 等共 12 个字段 | [wf_fna_waction_imp.md](./tables/财务管理/wf_fna_waction_imp.md) |
| 115 | `wf_fna_waddi_imp` | 17 | `impguid1`(workflow_addinoperate表对应字段)、`id`(workflow_addinoperate表对应字段)、`objid`(workflow_addinoperate表对应字段)、`isnode`(workflow_addinoperate表对应字段) 等共 17 个字段 | [wf_fna_waddi_imp.md](./tables/财务管理/wf_fna_waddi_imp.md) |
| 116 | `wf_fna_wb_imp` | 17 | `id`(workflow_bill表对应字段)、`namelabel`(workflow_bill表对应字段)、`tablename`(workflow_bill表对应字段)、`createpage`(workflow_bill表对应字段) 等共 17 个字段 | [wf_fna_wb_imp.md](./tables/财务管理/wf_fna_wb_imp.md) |
| 117 | `wf_fna_wbf_imp` | 26 | `id`(workflow_billfield表对应字段)、`billid`(workflow_billfield表对应字段)、`fieldname`(workflow_billfield表对应字段)、`fieldlabel`(workflow_billfield表对应字段) 等共 26 个字段 | [wf_fna_wbf_imp.md](./tables/财务管理/wf_fna_wbf_imp.md) |
| 118 | `wf_fna_wde_imp` | 7 | `impguid1`(Workflow_DataInput_entry表对应字段)、`id`(Workflow_DataInput_entry表对应字段)、`workflowid`(Workflow_DataInput_entry表对应字段)、`triggerfieldname`(Workflow_DataInput_entry表对应字段) 等共 7 个字段 | [wf_fna_wde_imp.md](./tables/财务管理/wf_fna_wde_imp.md) |
| 119 | `wf_fna_wdf_imp` | 8 | `id`(Workflow_DataInput_field表对应字段)、`datainputid`(Workflow_DataInput_field表对应字段)、`tableid`(Workflow_DataInput_field表对应字段)、`type`(Workflow_DataInput_field表对应字段) 等共 8 个字段 | [wf_fna_wdf_imp.md](./tables/财务管理/wf_fna_wdf_imp.md) |
| 120 | `wf_fna_wdm_imp` | 7 | `datasourcename`(Workflow_DataInput_main表对应字段)、`impguid1`(Workflow_DataInput_main表对应字段)、`id`(Workflow_DataInput_main表对应字段)、`entryid`(Workflow_DataInput_main表对应字段) 等共 7 个字段 | [wf_fna_wdm_imp.md](./tables/财务管理/wf_fna_wdm_imp.md) |
| 121 | `wf_fna_wdt_imp` | 6 | `id`(Workflow_DataInput_table表对应字段)、`datainputid`(Workflow_DataInput_table表对应字段)、`tablename`(Workflow_DataInput_table表对应字段)、`alias`(Workflow_DataInput_table表对应字段) 等共 6 个字段 | [wf_fna_wdt_imp.md](./tables/财务管理/wf_fna_wdt_imp.md) |
| 122 | `wf_fna_wf_imp` | 104 | `impguid1`(workflow_nodebase表对应字段)、`isbeforwardalready`(workflow_nodebase表对应字段)、`isshowbeforwardalready`(workflow_nodebase表对应字段)、`isalreadyforward`(workflow_nodebase表对应字段) 等共 104 个字段 | [wf_fna_wf_imp.md](./tables/财务管理/wf_fna_wf_imp.md) |
| 123 | `wf_fna_wfbase_imp` | 105 | `impguid1`(workflow_base表对应字段)、`candelacc`(workflow_base表对应字段)、`isforwardrights`(workflow_base表对应字段)、`isimportwf`(workflow_base表对应字段) 等共 105 个字段 | [wf_fna_wfbase_imp.md](./tables/财务管理/wf_fna_wfbase_imp.md) |
| 124 | `wf_fna_wfbt_imp` | 5 | `id`(fnafeewfinfofield表对应字段)、`typename`(fnafeewfinfofield表对应字段)、`typedesc`(fnafeewfinfofield表对应字段)、`dsporder`(fnafeewfinfofield表对应字段) 等共 5 个字段 | [wf_fna_wfbt_imp.md](./tables/财务管理/wf_fna_wfbt_imp.md) |
| 125 | `wf_fna_wfdi_imp` | 5 | `formid`(workflow_formdetailinfo表对应字段)、`rowcalstr`(workflow_formdetailinfo表对应字段)、`colcalstr`(workflow_formdetailinfo表对应字段)、`maincalstr`(workflow_formdetailinfo表对应字段) 等共 5 个字段 | [wf_fna_wfdi_imp.md](./tables/财务管理/wf_fna_wfdi_imp.md) |
| 126 | `wf_fna_wn_imp` | 20 | `impguid1`(workflow_nodebase表对应字段)、`operators_1`(workflow_nodebase表对应字段)、`requestid`(workflow_nodebase表对应字段)、`startnodeid`(workflow_nodebase表对应字段) 等共 20 个字段 | [wf_fna_wn_imp.md](./tables/财务管理/wf_fna_wn_imp.md) |
| 127 | `wf_fna_wnf_imp` | 7 | `impguid1`(workflow_nodeform表对应字段)、`nodeid`(workflow_nodeform表对应字段)、`fieldid`(workflow_nodeform表对应字段)、`isview`(workflow_nodeform表对应字段) 等共 7 个字段 | [wf_fna_wnf_imp.md](./tables/财务管理/wf_fna_wnf_imp.md) |
| 128 | `wf_fna_wnhl_imp` | 18 | `impguid1`(workflow_nodehtmllayout表对应字段)、`id`(workflow_nodehtmllayout表对应字段)、`workflowid`(workflow_nodehtmllayout表对应字段)、`formid`(workflow_nodehtmllayout表对应字段) 等共 18 个字段 | [wf_fna_wnhl_imp.md](./tables/财务管理/wf_fna_wnhl_imp.md) |
| 129 | `wf_fna_wnlink_imp` | 72 | `impguid1`(workflow_nodelink表对应字段)、`id`(workflow_nodelink表对应字段)、`workflowid`(workflow_nodelink表对应字段)、`nodeid`(workflow_nodelink表对应字段) 等共 72 个字段 | [wf_fna_wnlink_imp.md](./tables/财务管理/wf_fna_wnlink_imp.md) |
| 130 | `wf_fna_wrbf_imp` | 62 | `requestnameshoworder`(workflow_rquestBrowseFunction表对应字段)、`workflowtypeshoworder`(workflow_rquestBrowseFunction表对应字段)、`processnumbershoworder`(workflow_rquestBrowseFunction表对应字段)、`createtypeidshoworder`(workflow_rquestBrowseFunction表对应字段) 等共 62 个字段 | [wf_fna_wrbf_imp.md](./tables/财务管理/wf_fna_wrbf_imp.md) |
| 131 | `wf_fna_wsi_imp` | 14 | `fieldid`(workflow_SelectItem表对应字段)、`isbill`(workflow_SelectItem表对应字段)、`selectvalue`(workflow_SelectItem表对应字段)、`selectname`(workflow_SelectItem表对应字段) 等共 14 个字段 | [wf_fna_wsi_imp.md](./tables/财务管理/wf_fna_wsi_imp.md) |
| 132 | `wf_fna_wval_imp` | 7 | `impguid1`(workflow_viewattrlinkage表对应字段)、`workflowid`(workflow_viewattrlinkage表对应字段)、`nodeid`(workflow_viewattrlinkage表对应字段)、`selectfieldid`(workflow_viewattrlinkage表对应字段) 等共 7 个字段 | [wf_fna_wval_imp.md](./tables/财务管理/wf_fna_wval_imp.md) |
| 133 | `workflowtofinanceurl` | 12 | `id`(主键)、`guid1`(uuid)、`sendurl`(推送url)、`requestid`(流程reqid) 等共 12 个字段 | [workflowtofinanceurl.md](./tables/财务管理/workflowtofinanceurl.md) |

### 表单建模

> 本模块共收录 `120` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `Mode_boarditemorder_xxx` | 5 | `id`(id)、`boardid`(看板id)、`dataid`(数据id)、`groupid`(分组id) 等共 5 个字段 | [Mode_boarditemorder_xxx.md](./tables/表单建模/Mode_boarditemorder_xxx.md) |
| 2 | `Modedatashare_XXX_set` | 23 | `browsersharetype`(浏览框权限类型)、`id`(id)、`sourceid`(数据id)、`righttype`(权限级别) 等共 23 个字段 | [Modedatashare_XXX_set.md](./tables/表单建模/Modedatashare_XXX_set.md) |
| 3 | `Modedatashare_xxx` | 21 | `browsersharetype`(浏览框权限类型)、`id`(id)、`sourceid`(数据id)、`type`(权限类型) 等共 21 个字段 | [Modedatashare_xxx.md](./tables/表单建模/Modedatashare_xxx.md) |
| 4 | `Modetabs_xxx` | 6 | `id`(id)、`tabname`(表名称)、`color`(颜色)、`type`(类型) 等共 6 个字段 | [Modetabs_xxx.md](./tables/表单建模/Modetabs_xxx.md) |
| 5 | `Modetabslog_xxx` | 9 | `id`(id)、`tabid`(标签id)、`operate`(操作)、`modeid`(模块id) 等共 9 个字段 | [Modetabslog_xxx.md](./tables/表单建模/Modetabslog_xxx.md) |
| 6 | `Modeviewlog_XXX` | 9 | `id`(id)、`relatedid`(使用id)、`relatedname`(使用过程)、`operatetype`(操作类型) 等共 9 个字段 | [Modeviewlog_XXX.md](./tables/表单建模/Modeviewlog_XXX.md) |
| 7 | `appdatacount` | 4 | `id`(主键id)、`appid`(应用id)、`month`(月份)、`sumval`(应用数) | [appdatacount.md](./tables/表单建模/appdatacount.md) |
| 8 | `appforminfo` | 2 | `appid`(应用id)、`formid`(表单id) | [appforminfo.md](./tables/表单建模/appforminfo.md) |
| 9 | `customfieldshowchange` | 15 | `rowbackvalue`(行背景色)、`rowfontvalue`(行字体颜色)、`displaystyles`(显示样式)、`thumbnail`(是否缩略图) 等共 15 个字段 | [customfieldshowchange.md](./tables/表单建模/customfieldshowchange.md) |
| 10 | `defaultvalue` | 5 | `id`(ID)、`modeid`(模块id)、`fieldid`(字段id)、`customervalue`(默认值) 等共 5 个字段 | [defaultvalue.md](./tables/表单建模/defaultvalue.md) |
| 11 | `expandbaserightexpressionbase` | 3 | `id`(ID)、`fieldid`(字段id)、`fieldname`(数据库字段名) | [expandbaserightexpressionbase.md](./tables/表单建模/expandbaserightexpressionbase.md) |
| 12 | `expandbaserightexpressions` | 3 | `id`(ID)、`rightid`(权限设置id)、`relation`(关系) | [expandbaserightexpressions.md](./tables/表单建模/expandbaserightexpressions.md) |
| 13 | `expandbaserightinfo` | 4 | `id`(ID)、`modeid`(模块id)、`expandid`(页面扩展id)、`righttype`(权限类型) | [expandbaserightinfo.md](./tables/表单建模/expandbaserightinfo.md) |
| 14 | `formengineset` | 18 | `waterimg`(水印图片)、`wateralpha`(水印透明度)、`id`(主键id)、`appid`(应用id) 等共 18 个字段 | [formengineset.md](./tables/表单建模/formengineset.md) |
| 15 | `formmodeelement` | 10 | `isautoomit`(超出宽度自动省略)、`morehref`(多连接)、`id`(ID)、`eid`(门户页面id) 等共 10 个字段 | [formmodeelement.md](./tables/表单建模/formmodeelement.md) |
| 16 | `formmodeelementtemplate` | 9 | `id`(id)、`eid`(eid)、`reportid`(查询id)、`isshowunread`(是否显示已读) 等共 9 个字段 | [formmodeelementtemplate.md](./tables/表单建模/formmodeelementtemplate.md) |
| 17 | `formmodelog` | 3 | `id`(操作时间，显示形式2         8)、`objid`(操作对象)、`logmodule`(操作模块) | [formmodelog.md](./tables/表单建模/formmodelog.md) |
| 18 | `mode_barcode` | 11 | `id`(ID)、`modeid`(模块id)、`isused`(是否启用)、`resolution`(分辨率) 等共 11 个字段 | [mode_barcode.md](./tables/表单建模/mode_barcode.md) |
| 19 | `mode_batchimp_log` | 12 | `id`(id)、`modeid`(模块id)、`operatetype`(操作类型)、`ipaddress`(IP) 等共 12 个字段 | [mode_batchimp_log.md](./tables/表单建模/mode_batchimp_log.md) |
| 20 | `mode_batchmodify` | 5 | `id`(主键id)、`name`(字段名称)、`remark`(说明)、`modeid`(模块id) 等共 5 个字段 | [mode_batchmodify.md](./tables/表单建模/mode_batchmodify.md) |
| 21 | `mode_batchmodifydetail` | 5 | `id`(主键id)、`mainid`(主表id)、`changetype`(改变类型)、`feildid`(字段id) 等共 5 个字段 | [mode_batchmodifydetail.md](./tables/表单建模/mode_batchmodifydetail.md) |
| 22 | `mode_batchset` | 5 | `id`(ID)、`expandid`(页面扩展id)、`showorder`(显示顺序)、`customsearchid`(查询列表id) 等共 5 个字段 | [mode_batchset.md](./tables/表单建模/mode_batchset.md) |
| 23 | `mode_board` | 15 | `grouptype`(分组类型)、`id`(id)、`name`(看板名称)、`appid`(所属应用) 等共 15 个字段 | [mode_board.md](./tables/表单建模/mode_board.md) |
| 24 | `mode_board_group` | 8 | `resourceid`(数据id)、`id`(id)、`boardid`(看板id)、`formid`(表单id) 等共 8 个字段 | [mode_board_group.md](./tables/表单建模/mode_board_group.md) |
| 25 | `mode_board_grouptemp` | 5 | `id`(id)、`boardid`(看板id)、`isroot`(自定义是否根节点)、`type`(类型) 等共 5 个字段 | [mode_board_grouptemp.md](./tables/表单建模/mode_board_grouptemp.md) |
| 26 | `mode_boardshareinfo` | 10 | `id`(id)、`boardid`(看板id)、`sharetype`(权限类型)、`relatedid`(关系id) 等共 10 个字段 | [mode_boardshareinfo.md](./tables/表单建模/mode_boardshareinfo.md) |
| 27 | `mode_browser` | 33 | `createdate`(创建日期)、`createtime`(创建时间)、`modifydate`(更改日期)、`modifytime`(更改时间) 等共 33 个字段 | [mode_browser.md](./tables/表单建模/mode_browser.md) |
| 28 | `mode_custombrowser` | 8 | `javafileaddress`(固定java条件)、`isdisplaydraftdata`(是否显示草稿)、`id`(ID)、`modeid`(模块id) 等共 8 个字段 | [mode_custombrowser.md](./tables/表单建模/mode_custombrowser.md) |
| 29 | `mode_custombrowserdspfield` | 4 | `id`(ID)、`customid`(浏览框id)、`fieldid`(字段id)、`isquery`(是否查询条件) | [mode_custombrowserdspfield.md](./tables/表单建模/mode_custombrowserdspfield.md) |
| 30 | `mode_customcountset` | 10 | `orderid`(排序id)、`id`(id)、`customid`(查询id)、`name`(名称) 等共 10 个字段 | [mode_customcountset.md](./tables/表单建模/mode_customcountset.md) |
| 31 | `mode_customdspfield` | 7 | `shownamelabel`(显示转换)、`alignment`(对齐方式)、`ismaplocation`(开启地图)、`id`(ID) 等共 7 个字段 | [mode_customdspfield.md](./tables/表单建模/mode_customdspfield.md) |
| 32 | `mode_custompage` | 11 | `guid`(uuid)、`props`(已废弃)、`component`(已废弃)、`showorder`(显示顺序) 等共 11 个字段 | [mode_custompage.md](./tables/表单建模/mode_custompage.md) |
| 33 | `mode_custompagedetail` | 7 | `id`(ID)、`mainid`(自定义页面主id)、`hrefname`(名称)、`hreftitle`(提示信息) 等共 7 个字段 | [mode_custompagedetail.md](./tables/表单建模/mode_custompagedetail.md) |
| 34 | `mode_customresource` | 15 | `id`(ID)、`appid`(所属应用)、`resourcename`(名称)、`customsearchid`(查询列表) 等共 15 个字段 | [mode_customresource.md](./tables/表单建模/mode_customresource.md) |
| 35 | `mode_customsearch` | 10 | `iswatermark`(水印信息)、`sliderpercentage`(滑块显示占比)、`isshowquerycondition`(是否展开查询条件)、`javafileaddress`(java查询条件) 等共 10 个字段 | [mode_customsearch.md](./tables/表单建模/mode_customsearch.md) |
| 36 | `mode_customsearchbutton` | 5 | `pageexpandid`(页面扩展id)、`id`(ID)、`objid`(查询列表id)、`buttonname`(名称) 等共 5 个字段 | [mode_customsearchbutton.md](./tables/表单建模/mode_customsearchbutton.md) |
| 37 | `mode_customtree` | 11 | `id`(ID)、`treename`(树形名称)、`treedesc`(描述)、`modeid`(模块id) 等共 11 个字段 | [mode_customtree.md](./tables/表单建模/mode_customtree.md) |
| 38 | `mode_customtreedetail` | 5 | `id`(ID)、`mainid`(树形id)、`nodename`(名称)、`nodedesc`(描述) 等共 5 个字段 | [mode_customtreedetail.md](./tables/表单建模/mode_customtreedetail.md) |
| 39 | `mode_dataapprovalinfo` | 11 | `billid`(数据id)、`modeid`(模块id)、`formid`(表单id)、`requestid`(流程requestid) 等共 11 个字段 | [mode_dataapprovalinfo.md](./tables/表单建模/mode_dataapprovalinfo.md) |
| 40 | `mode_databatchimport` | 5 | `importorder`(导入顺序)、`id`(ID)、`modeid`(模块id)、`interfacepath`(接口路径) 等共 5 个字段 | [mode_databatchimport.md](./tables/表单建模/mode_databatchimport.md) |
| 41 | `mode_deletelog` | 8 | `id`(id)、`creator`(创建者)、`createdate`(创建日期)、`createtime`(创建时间) 等共 8 个字段 | [mode_deletelog.md](./tables/表单建模/mode_deletelog.md) |
| 42 | `mode_dmlactionfieldmap` | 3 | `id`(ID)、`actionsqlsetid`(dml接口动作详细信息id)、`maptype`(操作类型) | [mode_dmlactionfieldmap.md](./tables/表单建模/mode_dmlactionfieldmap.md) |
| 43 | `mode_dmlactionset` | 10 | `dmlsource`(数据源)、`dmlsourcetype`(数据类型)、`dmlsourceorder`(来源类型)、`id`(ID) 等共 10 个字段 | [mode_dmlactionset.md](./tables/表单建模/mode_dmlactionset.md) |
| 44 | `mode_dmlactionsqlset` | 17 | `id`(ID)、`actionid`(dml接口动作主id)、`actiontable`(数据源表)、`dmlformid`(外部主表) 等共 17 个字段 | [mode_dmlactionsqlset.md](./tables/表单建模/mode_dmlactionsqlset.md) |
| 45 | `mode_excelfield` | 4 | `id`(ID)、`modeid`(模块id)、`formid`(表单id)、`note`(说明) | [mode_excelfield.md](./tables/表单建模/mode_excelfield.md) |
| 46 | `mode_excelfielddetail` | 5 | `id`(ID)、`mainid`(条件设置表id)、`selectids`(选择框id)、`selectvalue`(选择框的值) 等共 5 个字段 | [mode_excelfielddetail.md](./tables/表单建模/mode_excelfielddetail.md) |
| 47 | `mode_expfieldtrans` | 3 | `id`(id)、`customid`(查询列表id)、`fieldid`(字段id) | [mode_expfieldtrans.md](./tables/表单建模/mode_expfieldtrans.md) |
| 48 | `mode_exportcustomstyle` | 17 | `customid`(查询列表id)、`headerbg`(表头背景色)、`headerfontcolor`(表头字体颜色)、`headerfont`(表头字体) 等共 17 个字段 | [mode_exportcustomstyle.md](./tables/表单建模/mode_exportcustomstyle.md) |
| 49 | `mode_exportexcelfield` | 7 | `customid`(查询列表id)、`fieldid`(字段id)、`isexport`(是否导出)、`exportorder`(导出顺序) 等共 7 个字段 | [mode_exportexcelfield.md](./tables/表单建模/mode_exportexcelfield.md) |
| 50 | `mode_exportexcelset` | 7 | `customid`(查询列表id)、`iscustomstyle`(是否自定义导出样式)、`isgroupexport`(是否分组导出)、`isexportfield`(是否自定义导出字段) 等共 7 个字段 | [mode_exportexcelset.md](./tables/表单建模/mode_exportexcelset.md) |
| 51 | `mode_expressionbase` | 4 | `searchtransmethodid`(查询id)、`id`(ID)、`fieldid`(字段id)、`fieldname`(数据库字段名) | [mode_expressionbase.md](./tables/表单建模/mode_expressionbase.md) |
| 52 | `mode_expressionbase_tid` | 2 | `id`(id)、`uuid`(uuid) | [mode_expressionbase_tid.md](./tables/表单建模/mode_expressionbase_tid.md) |
| 53 | `mode_expressions` | 4 | `searchtransmethodid`(查询id)、`id`(ID)、`rightid`(权限设置id)、`relation`(关系) | [mode_expressions.md](./tables/表单建模/mode_expressions.md) |
| 54 | `mode_fieldtype` | 7 | `id`(主键id)、`typename`(类型名称)、`namelabel`(字段显示名的标签id)、`classname`(流程字段html代码生成类) 等共 7 个字段 | [mode_fieldtype.md](./tables/表单建模/mode_fieldtype.md) |
| 55 | `mode_fileuploadset` | 12 | `modeid`(模块id)、`formid`(表单id)、`fieldid`(字段id)、`selectfieldid`(选择目录) 等共 12 个字段 | [mode_fileuploadset.md](./tables/表单建模/mode_fileuploadset.md) |
| 56 | `mode_ganttdspfield` | 8 | `id`(id)、`ganttid`(刚特图id)、`fieldid`(字段id)、`isshow`(是否显示) 等共 8 个字段 | [mode_ganttdspfield.md](./tables/表单建模/mode_ganttdspfield.md) |
| 57 | `mode_ganttset` | 25 | `id`(id)、`ganttname`(刚特图名称)、`appid`(所属应用)、`formid`(表单id) 等共 25 个字段 | [mode_ganttset.md](./tables/表单建模/mode_ganttset.md) |
| 58 | `mode_impexp_log` | 8 | `id`(id)、`creator`(创建者)、`createdate`(创建日期)、`createtime`(创建时间) 等共 8 个字段 | [mode_impexp_log.md](./tables/表单建模/mode_impexp_log.md) |
| 59 | `mode_impexp_logdetail` | 5 | `id`(id)、`logid`(日志id)、`tablename`(表名称)、`logtype`(日志类型) 等共 5 个字段 | [mode_impexp_logdetail.md](./tables/表单建模/mode_impexp_logdetail.md) |
| 60 | `mode_impexp_recorddetail` | 7 | `id`(id)、`tablename`(表名称)、`columnname`(字段名称)、`columnvalue`(字段值) 等共 7 个字段 | [mode_impexp_recorddetail.md](./tables/表单建模/mode_impexp_recorddetail.md) |
| 61 | `mode_impfailurelog` | 7 | `id`(ID)、`modeid`(模块id)、`errormsg`(错误信息)、`tablename`(表名称) 等共 7 个字段 | [mode_impfailurelog.md](./tables/表单建模/mode_impfailurelog.md) |
| 62 | `mode_import_fieldtrans` | 4 | `id`(主键)、`modeid`(模块id)、`formid`(表单id)、`fieldid`(字段id) | [mode_import_fieldtrans.md](./tables/表单建模/mode_import_fieldtrans.md) |
| 63 | `mode_jscodearea` | 6 | `id`(主键ID)、`customid`(查询列表ID)、`scriptstr`(js代码)、`ext1`(扩展字段1) 等共 6 个字段 | [mode_jscodearea.md](./tables/表单建模/mode_jscodearea.md) |
| 64 | `mode_layout_querysql` | 9 | `id`(主键id)、`modeid`(模块id)、`formid`(表单id)、`layoutid`(布局id) 等共 9 个字段 | [mode_layout_querysql.md](./tables/表单建模/mode_layout_querysql.md) |
| 65 | `mode_layout_sortfield` | 8 | `ordertype`(排序类型)、`ordernum`(字段顺序)、`id`(主键id)、`modeid`(模块id) 等共 8 个字段 | [mode_layout_sortfield.md](./tables/表单建模/mode_layout_sortfield.md) |
| 66 | `mode_mindset` | 17 | `id`(id)、`formid`(表单id)、`modeid`(模块id)、`rootname`(根节点名称) 等共 17 个字段 | [mode_mindset.md](./tables/表单建模/mode_mindset.md) |
| 67 | `mode_newserialnum` | 4 | `id`(主键id)、`codemainid`(编码id)、`condition`(匹配条件)、`num`(当前流水号) | [mode_newserialnum.md](./tables/表单建模/mode_newserialnum.md) |
| 68 | `mode_pageexpand` | 6 | `groupid`(tab页分组)、`isquickbutton`(快捷按钮)、`id`(ID)、`modeid`(模块id) 等共 6 个字段 | [mode_pageexpand.md](./tables/表单建模/mode_pageexpand.md) |
| 69 | `mode_pageexpanddetail` | 5 | `triggerworkflowsetid`(自定义流程id)、`javafileaddress`(java条件)、`id`(ID)、`mainid`(页面扩展主id) 等共 5 个字段 | [mode_pageexpanddetail.md](./tables/表单建模/mode_pageexpanddetail.md) |
| 70 | `mode_pageexpandtemplate` | 3 | `id`(ID)、`expendname`(名称)、`showtype`(显示样式) | [mode_pageexpandtemplate.md](./tables/表单建模/mode_pageexpandtemplate.md) |
| 71 | `mode_pagerelatefield` | 5 | `id`(ID)、`modeid`(模块id)、`hreftype`(链接目标来源)、`hrefid`(链接目标) 等共 5 个字段 | [mode_pagerelatefield.md](./tables/表单建模/mode_pagerelatefield.md) |
| 72 | `mode_pagerelatefielddetail` | 4 | `id`(ID)、`mainid`(页面扩展相关字段主id)、`modefieldname`(模块字段)、`hreffieldname`(链接目标字段) | [mode_pagerelatefielddetail.md](./tables/表单建模/mode_pagerelatefielddetail.md) |
| 73 | `mode_quicksearch_condition` | 6 | `id`(id)、`customid`(查询id)、`fieldid`(字段id)、`customname`(查询名称) 等共 6 个字段 | [mode_quicksearch_condition.md](./tables/表单建模/mode_quicksearch_condition.md) |
| 74 | `mode_quicksearch_detail` | 9 | `fieldid`(字段id)、`customid`(查询id)、`id`(id)、`cid`(cid) 等共 9 个字段 | [mode_quicksearch_detail.md](./tables/表单建模/mode_quicksearch_detail.md) |
| 75 | `mode_reminddata` | 13 | `subbillid`(明细表id)、`isremindsms`(短信提醒)、`isremindemail`(邮件提醒)、`isremindworkflow`(流程提醒) 等共 13 个字段 | [mode_reminddata.md](./tables/表单建模/mode_reminddata.md) |
| 76 | `mode_reminddata_all` | 12 | `isremindsms`(短信提醒)、`isremindemail`(邮件提醒)、`isremindworkflow`(流程提醒)、`isremindwechat`(微信云桥提醒) 等共 12 个字段 | [mode_reminddata_all.md](./tables/表单建模/mode_reminddata_all.md) |
| 77 | `mode_reminddata_error` | 12 | `id`(id)、`remindjobid`(提醒id)、`modeid`(模块id)、`billid`(数据id) 等共 12 个字段 | [mode_reminddata_error.md](./tables/表单建模/mode_reminddata_error.md) |
| 78 | `mode_reminddata_log` | 4 | `id`(ID)、`remindjobid`(提醒基本信息id)、`lastreminddate`(上次提醒日期)、`lastremindtime`(上次提醒时间) | [mode_reminddata_log.md](./tables/表单建模/mode_reminddata_log.md) |
| 79 | `mode_remindjob` | 1 | `formtype`(数据表单类型) | [mode_remindjob.md](./tables/表单建模/mode_remindjob.md) |
| 80 | `mode_sapactionset` | 6 | `id`(id)、`actionname`(接口名称)、`modeid`(模块id)、`expandid`(扩展id) 等共 6 个字段 | [mode_sapactionset.md](./tables/表单建模/mode_sapactionset.md) |
| 81 | `mode_sapactionsetdetail` | 6 | `id`(id)、`mainid`(mainid)、`type`(类型)、`paratype`(参数类型) 等共 6 个字段 | [mode_sapactionsetdetail.md](./tables/表单建模/mode_sapactionsetdetail.md) |
| 82 | `mode_searchpageshareinfo` | 3 | `id`(ID)、`pageid`(查询列表id)、`righttype`(权限级别) | [mode_searchpageshareinfo.md](./tables/表单建模/mode_searchpageshareinfo.md) |
| 83 | `mode_selectitempage` | 10 | `id`(主键id)、`selectitemname`(选择项名称)、`selectitemdesc`(选择项描述)、`creater`(创建人) 等共 10 个字段 | [mode_selectitempage.md](./tables/表单建模/mode_selectitempage.md) |
| 84 | `mode_selectitempagedetail` | 14 | `id`(主键id)、`mainid`(主表id)、`name`(名称)、`disorder`(排序) 等共 14 个字段 | [mode_selectitempagedetail.md](./tables/表单建模/mode_selectitempagedetail.md) |
| 85 | `mode_templatedspfield` | 10 | `id`(主键id)、`templateid`(模板主表id)、`fieldid`(字段id)、`isshow`(是否显示) 等共 10 个字段 | [mode_templatedspfield.md](./tables/表单建模/mode_templatedspfield.md) |
| 86 | `mode_templateinfo` | 9 | `id`(主键id)、`customid`(查询页id)、`templatename`(模板名称)、`templatetype`(模板类型) 等共 9 个字段 | [mode_templateinfo.md](./tables/表单建模/mode_templateinfo.md) |
| 87 | `mode_toolbar_search` | 10 | `id`(主键id)、`isusedsearch`(是否启用)、`searchname`(查询名称)、`searchfield`(查询字段) 等共 10 个字段 | [mode_toolbar_search.md](./tables/表单建模/mode_toolbar_search.md) |
| 88 | `mode_triggerworkflowset` | 10 | `triggername`(名称)、`triggeroperation`(操作类型)、`isenable`(是否开启)、`conditiontype`(条件类型) 等共 10 个字段 | [mode_triggerworkflowset.md](./tables/表单建模/mode_triggerworkflowset.md) |
| 89 | `mode_triggerworkflowsetdetail` | 5 | `defaultvalue`(失败信息)、`id`(ID)、`mainid`(数据审批主id)、`modefieldid`(模块字段名称) 等共 5 个字段 | [mode_triggerworkflowsetdetail.md](./tables/表单建模/mode_triggerworkflowsetdetail.md) |
| 90 | `mode_workflowtomodeset` | 8 | `conditionsql`(触发sql)、`conditiontext`(触发内容)、`uuid`(uuid)、`remark`(备注) 等共 8 个字段 | [mode_workflowtomodeset.md](./tables/表单建模/mode_workflowtomodeset.md) |
| 91 | `mode_workflowtomodesetdetail` | 5 | `id`(ID)、`mainid`(流程转数据主id)、`modefieldid`(模块字段名称)、`wffieldid`(流程字段名称) 等共 5 个字段 | [mode_workflowtomodesetdetail.md](./tables/表单建模/mode_workflowtomodesetdetail.md) |
| 92 | `mode_workflowtomodesetopt` | 4 | `id`(ID)、`mainid`(流程转数据主id)、`detailtablename`(明细表表名)、`opttype`(明细表操作类型) | [mode_workflowtomodesetopt.md](./tables/表单建模/mode_workflowtomodesetopt.md) |
| 93 | `mode_wsactionset` | 11 | `id`(id)、`actionname`(接口名称)、`modeid`(模块id)、`expandid`(扩展id) 等共 11 个字段 | [mode_wsactionset.md](./tables/表单建模/mode_wsactionset.md) |
| 94 | `modeattrlinkage` | 4 | `isenabled`(是否启用)、`id`(ID)、`modeid`(模块id)、`type`(布局类型) | [modeattrlinkage.md](./tables/表单建模/modeattrlinkage.md) |
| 95 | `modecode` | 3 | `uuid`(uuid)、`id`(ID)、`isuse`(是否启用) | [modecode.md](./tables/表单建模/modecode.md) |
| 96 | `modecode_daizi` | 4 | `fieldvalue`(字段值)、`shortvalue`(短值)、`id`(id)、`codedetailid`(详细编码值) | [modecode_daizi.md](./tables/表单建模/modecode_daizi.md) |
| 97 | `modecodedetail` | 5 | `uuid`(uuid)、`id`(ID)、`codemainid`(字段编码主id)、`showname`(显示名称) 等共 5 个字段 | [modecodedetail.md](./tables/表单建模/modecodedetail.md) |
| 98 | `modedatainputentry` | 6 | `isenabled`(是否启用)、`id`(ID)、`modeid`(模块id)、`triggername`(触发名称) 等共 6 个字段 | [modedatainputentry.md](./tables/表单建模/modedatainputentry.md) |
| 99 | `modedatainputfield` | 4 | `id`(ID)、`datainputid`(字段联动主id)、`tableid`(字段联动引用数据库表名id)、`type`(设置类型) | [modedatainputfield.md](./tables/表单建模/modedatainputfield.md) |
| 100 | `modedatainputmain` | 6 | `id`(ID)、`entryid`(基本信息id)、`whereclause`(表之间关联条件)、`iscycle`(4) 等共 6 个字段 | [modedatainputmain.md](./tables/表单建模/modedatainputmain.md) |
| 101 | `modedatainputtable` | 5 | `id`(ID)、`datainputid`(字段联动主id)、`tablename`(表名)、`alias`(别名) 等共 5 个字段 | [modedatainputtable.md](./tables/表单建模/modedatainputtable.md) |
| 102 | `modefieldattr` | 4 | `id`(ID)、`modeid`(模块id)、`formid`(表单id)、`type`(布局类型) | [modefieldattr.md](./tables/表单建模/modefieldattr.md) |
| 103 | `modefieldauthorize` | 5 | `id`(ID)、`modeid`(模块id)、`formid`(表单id)、`fieldid`(字段id) 等共 5 个字段 | [modefieldauthorize.md](./tables/表单建模/modefieldauthorize.md) |
| 104 | `modeformextend` | 3 | `formid`(表单id)、`appid`(所属应用)、`isvirtualform`(是否虚拟表单) | [modeformextend.md](./tables/表单建模/modeformextend.md) |
| 105 | `modeformfield` | 2 | `modeid`(模块id)、`type`(布局类型) | [modeformfield.md](./tables/表单建模/modeformfield.md) |
| 106 | `modeformfieldextend` | 9 | `formid`(表单id)、`fieldid`(字段id)、`needlog`(是否记录日志)、`isprompt`(是否提交数据提醒) 等共 9 个字段 | [modeformfieldextend.md](./tables/表单建模/modeformfieldextend.md) |
| 107 | `modeformgroup` | 3 | `modeid`(模块id)、`formid`(表单id)、`type`(布局类型) | [modeformgroup.md](./tables/表单建模/modeformgroup.md) |
| 108 | `modeformverify` | 7 | `id`(id)、`formid`(表单id)、`fieldids`(字段id)、`operate`(操作者) 等共 7 个字段 | [modeformverify.md](./tables/表单建模/modeformverify.md) |
| 109 | `modehtmllayout` | 4 | `id`(ID)、`modeid`(模块id)、`formid`(表单id)、`type`(布局类型) | [modehtmllayout.md](./tables/表单建模/modehtmllayout.md) |
| 110 | `modeinfo` | 13 | `empowmenttype`(自定义目录)、`id`(模块id)、`modename`(名称)、`modedesc`(描述) 等共 13 个字段 | [modeinfo.md](./tables/表单建模/modeinfo.md) |
| 111 | `modelogfielddetail` | 6 | `id`(主键id)、`viewlogid`(日志主表id)、`fieldid`(字段id)、`fieldvalue`(当前值) 等共 6 个字段 | [modelogfielddetail.md](./tables/表单建模/modelogfielddetail.md) |
| 112 | `modeqrcode` | 3 | `id`(应用id)、`modeid`(模块id)、`targettype`(目标类型) | [modeqrcode.md](./tables/表单建模/modeqrcode.md) |
| 113 | `modereplyat` | 5 | `id`(id)、`userid`(使用者id)、`replyid`(回复评论id)、`billid`(数据id) 等共 5 个字段 | [modereplyat.md](./tables/表单建模/modereplyat.md) |
| 114 | `moderightinfo` | 5 | `browsersharetype`(浏览框数据权限类型)、`javafileaddress`(java条件)、`id`(ID)、`modeid`(模块id) 等共 5 个字段 | [moderightinfo.md](./tables/表单建模/moderightinfo.md) |
| 115 | `moderightinfo_matrix` | 3 | `rightid`(权限id)、`matrix`(矩阵)、`value_field`(字段值) | [moderightinfo_matrix.md](./tables/表单建模/moderightinfo_matrix.md) |
| 116 | `moderightinfo_matrixcondition` | 3 | `rightid`(权限id)、`condition_field`(字段条件)、`fieldid`(字段id) | [moderightinfo_matrixcondition.md](./tables/表单建模/moderightinfo_matrixcondition.md) |
| 117 | `modetreefield` | 13 | `icon`(应用自定义图标)、`iconcolor`(图标字体颜色)、`iconbg`(图标背景颜色)、`id`(应用id) 等共 13 个字段 | [modetreefield.md](./tables/表单建模/modetreefield.md) |
| 118 | `remind_multi_ruleinfo` | 8 | `id`(主键)、`remindjobid`(提醒id对应mode_remindjob表的id)、`receivertype`(提醒接收人员类型)、`receiverdetail`(提醒人员id) 等共 8 个字段 | [remind_multi_ruleinfo.md](./tables/表单建模/remind_multi_ruleinfo.md) |
| 119 | `serialnum` | 9 | `id`(主键id)、`num`(当前流水号)、`codemainid`(编码id)、`field1`(编码字段1) 等共 9 个字段 | [serialnum.md](./tables/表单建模/serialnum.md) |
| 120 | `workflowtomodelog` | 24 | `modeuuid`(uuid)、`check_dt_sql_msg`(校验sql信息)、`successfullog`(成功sql信息)、`actionid`(接口id) 等共 24 个字段 | [workflowtomodelog.md](./tables/表单建模/workflowtomodelog.md) |

### 客户管理

> 本模块共收录 `103` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `LgcStockInOutDetail` | 11 | `id`(id)、`inoutid`(进出库id)、`assetid`(产品id)、`batchmark`(批量标记) 等共 11 个字段 | [LgcStockInOutDetail.md](./tables/客户管理/LgcStockInOutDetail.md) |
| 2 | `LgcStockMode` | 5 | `id`(id)、`modename`(名称)、`modetype`(类型)、`modestatus`(状态) 等共 5 个字段 | [LgcStockMode.md](./tables/客户管理/LgcStockMode.md) |
| 3 | `bill_approvecustomer` | 9 | `id`(ID)、`managerid`(客户经理id)、`requestid`(工作流请求的ID)、`approveid`(被审批客户的的id) 等共 9 个字段 | [bill_approvecustomer.md](./tables/客户管理/bill_approvecustomer.md) |
| 4 | `contract_shareinfo` | 14 | `id`(id)、`relateditemid`(相关项目id)、`sharetype`(共享类型)、`seclevel`(安全级别) 等共 14 个字段 | [contract_shareinfo.md](./tables/客户管理/contract_shareinfo.md) |
| 5 | `contractsharedetail` | 4 | `contractid`(联系共享的id)、`userid`(用户id)、`usertype`(用户类型)、`sharelevel`(共享等级) | [contractsharedetail.md](./tables/客户管理/contractsharedetail.md) |
| 6 | `crm_addresstype` | 5 | `id`(id)、`fullname`(地址全称)、`description`(地址描述)、`candelete`(是否可以被删除) 等共 5 个字段 | [crm_addresstype.md](./tables/客户管理/crm_addresstype.md) |
| 7 | `crm_attention` | 3 | `id`(id)、`resourceid`(人员id)、`customerid`(客户id) | [crm_attention.md](./tables/客户管理/crm_attention.md) |
| 8 | `crm_busniessinfoeache` | 6 | `id`(id)、`userid`(人员id)、`data`(数据)、`modifydate`(日期) 等共 6 个字段 | [crm_busniessinfoeache.md](./tables/客户管理/crm_busniessinfoeache.md) |
| 9 | `crm_busniessinfolog` | 6 | `id`(id)、`crmid`(客户id)、`requesttype`(请求类型)、`requestdate`(日期) 等共 6 个字段 | [crm_busniessinfolog.md](./tables/客户管理/crm_busniessinfolog.md) |
| 10 | `crm_busniessinfosettings` | 11 | `id`(id)、`isopen`(是否开启)、`appkey`(appkey)、`crmtype`(适用客户类型) 等共 11 个字段 | [crm_busniessinfosettings.md](./tables/客户管理/crm_busniessinfosettings.md) |
| 11 | `crm_cardregsettings` | 8 | `id`(id)、`isopen`(是否开启)、`url`(接口地址)、`loginid`(账号) 等共 8 个字段 | [crm_cardregsettings.md](./tables/客户管理/crm_cardregsettings.md) |
| 12 | `crm_common_attention` | 6 | `id`(id)、`operatetype`(关注类型)、`objid`(关注id)、`operator`(关注人员id) 等共 6 个字段 | [crm_common_attention.md](./tables/客户管理/crm_common_attention.md) |
| 13 | `crm_contacterlog_remind` | 6 | `id`(id)、`customerid`(客户id)、`daytype`(提醒日期类型)、`before`(提前多少天) 等共 6 个字段 | [crm_contacterlog_remind.md](./tables/客户管理/crm_contacterlog_remind.md) |
| 14 | `crm_contactertitle` | 7 | `id`(id)、`fullname`(名称)、`description`(描述)、`usetype`(使用方法) 等共 7 个字段 | [crm_contactertitle.md](./tables/客户管理/crm_contactertitle.md) |
| 15 | `crm_contactlog` | 23 | `id`(id)、`customerid`(客户id)、`contacterid`(联系人id)、`resourceid`(人员id) 等共 23 个字段 | [crm_contactlog.md](./tables/客户管理/crm_contactlog.md) |
| 16 | `crm_contactway` | 4 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) | [crm_contactway.md](./tables/客户管理/crm_contactway.md) |
| 17 | `crm_contract` | 21 | `id`(id)、`name`(合同名称)、`typeid`(合同性质)、`docid`(合同正本) 等共 21 个字段 | [crm_contract.md](./tables/客户管理/crm_contract.md) |
| 18 | `crm_contract_exchange` | 7 | `id`(id)、`contractid`(合同id)、`name`(标题)、`remark`(备注) 等共 7 个字段 | [crm_contract_exchange.md](./tables/客户管理/crm_contract_exchange.md) |
| 19 | `crm_contractpaymethod` | 13 | `id`(id)、`contractid`(合同id)、`prjname`(付款项目名称)、`typeid`(付款性质) 等共 13 个字段 | [crm_contractpaymethod.md](./tables/客户管理/crm_contractpaymethod.md) |
| 20 | `crm_contractproduct` | 14 | `id`(id)、`contractid`(合同id)、`productid`(产品id)、`unitid`(单位id) 等共 14 个字段 | [crm_contractproduct.md](./tables/客户管理/crm_contractproduct.md) |
| 21 | `crm_contractproinfo` | 6 | `id`(id)、`proid`(产品id)、`factnum`(实际交货数量)、`factdate`(实际交货日期) 等共 6 个字段 | [crm_contractproinfo.md](./tables/客户管理/crm_contractproinfo.md) |
| 22 | `crm_contracttype` | 5 | `id`(id)、`name`(名称)、`contractdesc`(描述)、`workflowid`(工作流ID) 等共 5 个字段 | [crm_contracttype.md](./tables/客户管理/crm_contracttype.md) |
| 23 | `crm_creditinfo` | 5 | `id`(id)、`fullname`(等级名称)、`creditamount`(信用金额额度)、`highamount`(最高信用额度) 等共 5 个字段 | [crm_creditinfo.md](./tables/客户管理/crm_creditinfo.md) |
| 24 | `crm_customer_label` | 4 | `id`(id)、`userid`(人员id)、`customerid`(客户id)、`labelid`(标签id) | [crm_customer_label.md](./tables/客户管理/crm_customer_label.md) |
| 25 | `crm_customeraddress` | 44 | `dhwb1`(未知)、`zdy1`(未知)、`zdy2`(未知)、`c1`(未知) 等共 44 个字段 | [crm_customeraddress.md](./tables/客户管理/crm_customeraddress.md) |
| 26 | `crm_customercontacter` | 63 | `datefield2`(日期字段)、`datefield3`(日期字段)、`datefield4`(日期字段)、`datefield5`(日期字段) 等共 63 个字段 | [crm_customercontacter.md](./tables/客户管理/crm_customercontacter.md) |
| 27 | `crm_customercontacter_mind` | 5 | `id`(id)、`customerid`(客户id)、`contacterid`(联系人id)、`parentid`(父节点id) 等共 5 个字段 | [crm_customercontacter_mind.md](./tables/客户管理/crm_customercontacter_mind.md) |
| 28 | `crm_customercontacter_mind_log` | 8 | `id`(id)、`customerid`(客户id)、`contacterid`(联系人)、`operate_usr`(操作者) 等共 8 个字段 | [crm_customercontacter_mind_log.md](./tables/客户管理/crm_customercontacter_mind_log.md) |
| 29 | `crm_customercredit` | 3 | `creditamount`(信用额度)、`credittime`(信用期间)、`currencytype`(币种) | [crm_customercredit.md](./tables/客户管理/crm_customercredit.md) |
| 30 | `crm_customerdefinfield` | 26 | `id`(id)、`fieldname`(字段名称)、`fieldlabel`(标签id)、`fielddbtype`(字段类型) 等共 26 个字段 | [crm_customerdefinfield.md](./tables/客户管理/crm_customerdefinfield.md) |
| 31 | `crm_customerdefinfieldgroup` | 6 | `id`(id)、`usetable`(用于表)、`grouplabel`(组名称标签)、`candel`(能否删除) 等共 6 个字段 | [crm_customerdefinfieldgroup.md](./tables/客户管理/crm_customerdefinfieldgroup.md) |
| 32 | `crm_customerdesc` | 4 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) | [crm_customerdesc.md](./tables/客户管理/crm_customerdesc.md) |
| 33 | `crm_customerinfo` | 97 | `seasflag`(公海标志)、`oldmanager`(1)、`kh`(1)、`approvedate`(1) 等共 97 个字段 | [crm_customerinfo.md](./tables/客户管理/crm_customerinfo.md) |
| 34 | `crm_customerrating` | 10 | `id`(id)、`fullname`(名称)、`description`(描述)、`workflow11`(工作流信息) 等共 10 个字段 | [crm_customerrating.md](./tables/客户管理/crm_customerrating.md) |
| 35 | `crm_customersettings` | 8 | `id`(id)、`modifyuser`(修改者id)、`crm_rmd_create`(新建客户提醒开始)、`crm_rmd_create2`(新建客户提醒类型) 等共 8 个字段 | [crm_customersettings.md](./tables/客户管理/crm_customersettings.md) |
| 36 | `crm_customersize` | 4 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) | [crm_customersize.md](./tables/客户管理/crm_customersize.md) |
| 37 | `crm_customerstatus` | 7 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) 等共 7 个字段 | [crm_customerstatus.md](./tables/客户管理/crm_customerstatus.md) |
| 38 | `crm_customertag` | 6 | `id`(id)、`customerid`(客户id)、`tag`(标签名称)、`creater`(创建人员) 等共 6 个字段 | [crm_customertag.md](./tables/客户管理/crm_customertag.md) |
| 39 | `crm_customertype` | 7 | `id`(id)、`fullname`(名称)、`description`(描述)、`candelete`(能否删除) 等共 7 个字段 | [crm_customertype.md](./tables/客户管理/crm_customertype.md) |
| 40 | `crm_customertypepersonal` | 3 | `userid`(人员id)、`maintype`(主分类)、`subtype`(子分类) | [crm_customertypepersonal.md](./tables/客户管理/crm_customertypepersonal.md) |
| 41 | `crm_customize` | 21 | `userid`(人员id)、`row1col1`(第1行第1列设置)、`row1col2`(第1行第2列设置)、`row1col3`(第1行第3列设置) 等共 21 个字段 | [crm_customize.md](./tables/客户管理/crm_customize.md) |
| 42 | `crm_customizeoption` | 5 | `id`(id)、`tabledesc`(信息表类型)、`fieldname`(相应表中的字段名)、`labelid`(字段显示名的Label的ID) 等共 5 个字段 | [crm_customizeoption.md](./tables/客户管理/crm_customizeoption.md) |
| 43 | `crm_deliverytype` | 6 | `id`(id)、`fullname`(类型名称)、`description`(类型描述)、`sendtype`(发货方法) 等共 6 个字段 | [crm_deliverytype.md](./tables/客户管理/crm_deliverytype.md) |
| 44 | `crm_detailpagetabconfig` | 10 | `id`(id)、`name`(栏目名称)、`linkurl`(内部链接)、`isopen`(是否启用) 等共 10 个字段 | [crm_detailpagetabconfig.md](./tables/客户管理/crm_detailpagetabconfig.md) |
| 45 | `crm_evaluation` | 4 | `id`(id)、`name`(名称)、`proportion`(打分)、`orderkey`(排序字段) | [crm_evaluation.md](./tables/客户管理/crm_evaluation.md) |
| 46 | `crm_evaluation_level` | 4 | `id`(id)、`name`(名称)、`levelvalue`(等级)、`orderkey`(排序字段) | [crm_evaluation_level.md](./tables/客户管理/crm_evaluation_level.md) |
| 47 | `crm_evaluation_leveldetail` | 4 | `id`(id)、`customerid`(客户名称ID)、`evaluationid`(客户价值评估项目名称ID)、`levelid`(打分ID) | [crm_evaluation_leveldetail.md](./tables/客户管理/crm_evaluation_leveldetail.md) |
| 48 | `crm_exchange_info` | 6 | `sortid`(客户id)、`type_n`(留言类型)、`readdate`(查看日期)、`readtime`(查看时间) 等共 6 个字段 | [crm_exchange_info.md](./tables/客户管理/crm_exchange_info.md) |
| 49 | `crm_failfactor` | 4 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) | [crm_failfactor.md](./tables/客户管理/crm_failfactor.md) |
| 50 | `crm_fieldswitch` | 6 | `fieldid`(字段ID)、`datatype`(数据类型)、`isopen`(是否开启)、`ismust`(是否必填) 等共 6 个字段 | [crm_fieldswitch.md](./tables/客户管理/crm_fieldswitch.md) |
| 51 | `crm_label` | 10 | `id`(id)、`userid`(人员id)、`name`(标签名称)、`labelcolor`(标签颜色) 等共 10 个字段 | [crm_label.md](./tables/客户管理/crm_label.md) |
| 52 | `crm_ledgerinfo` | 5 | `customerid`(客户id)、`customercode`(客户财务代码)、`tradetype`(交易类型)、`ledger1`(科目1 id) 等共 5 个字段 | [crm_ledgerinfo.md](./tables/客户管理/crm_ledgerinfo.md) |
| 53 | `crm_log` | 20 | `id`(id)、`customerid`(客户id)、`logtype`(日志类型)、`documentid`(文档id) 等共 20 个字段 | [crm_log.md](./tables/客户管理/crm_log.md) |
| 54 | `crm_loginlog` | 4 | `id`(id)、`logindate`(登陆日期)、`logintime`(登陆时间)、`ipaddress`(IP地址) | [crm_loginlog.md](./tables/客户管理/crm_loginlog.md) |
| 55 | `crm_mapreport` | 19 | `id`(id)、`name`(报表名称)、`unit`(单位)、`datasource`(默认数据源) 等共 19 个字段 | [crm_mapreport.md](./tables/客户管理/crm_mapreport.md) |
| 56 | `crm_modify` | 12 | `customerid`(客户id)、`tabledesc`(对应表)、`type`(类型)、`addresstype`(地址类型) 等共 12 个字段 | [crm_modify.md](./tables/客户管理/crm_modify.md) |
| 57 | `crm_payinfo` | 6 | `id`(id)、`payid`(单据id)、`factprice`(实际付款金额)、`factdate`(实际付款日期) 等共 6 个字段 | [crm_payinfo.md](./tables/客户管理/crm_payinfo.md) |
| 58 | `crm_paymentterm` | 3 | `id`(id)、`fullname`(名称)、`description`(描述) | [crm_paymentterm.md](./tables/客户管理/crm_paymentterm.md) |
| 59 | `crm_producttable` | 7 | `sellchanceid`(销售机会id)、`productid`(产品id)、`assetunitid`(计量单位)、`currencyid`(货币id) 等共 7 个字段 | [crm_producttable.md](./tables/客户管理/crm_producttable.md) |
| 60 | `crm_seasapprovelog` | 7 | `description`(描述)、`id`(id)、`seasid`(公海id)、`custoemrid`(客户id) 等共 7 个字段 | [crm_seasapprovelog.md](./tables/客户管理/crm_seasapprovelog.md) |
| 61 | `crm_seascustomer` | 3 | `id`(id)、`customerid`(客户id)、`seasid`(公海id) | [crm_seascustomer.md](./tables/客户管理/crm_seascustomer.md) |
| 62 | `crm_seascustomerapprove` | 4 | `id`(id)、`seascustomerid`(公海客户id)、`approveuser`(分配人)、`approvedate`(分配时间) | [crm_seascustomerapprove.md](./tables/客户管理/crm_seascustomerapprove.md) |
| 63 | `crm_seasinfo` | 15 | `subcompanyids`(分部ID)、`departmentids`(部门ID)、`id`(id)、`name`(名称) 等共 15 个字段 | [crm_seasinfo.md](./tables/客户管理/crm_seasinfo.md) |
| 64 | `crm_seasright` | 10 | `id`(id)、`seasid`(公海id)、`sharetype`(共享类型)、`sharelevel`(共享级别) 等共 10 个字段 | [crm_seasright.md](./tables/客户管理/crm_seasright.md) |
| 65 | `crm_sectorinfo` | 7 | `id`(id)、`fullname`(名称)、`description`(描述)、`parentid`(上一级行业) 等共 7 个字段 | [crm_sectorinfo.md](./tables/客户管理/crm_sectorinfo.md) |
| 66 | `crm_selectitem` | 5 | `fieldid`(字段ID)、`selectvalue`(选项值)、`selectname`(选项名称)、`fieldorder`(选项排序) 等共 5 个字段 | [crm_selectitem.md](./tables/客户管理/crm_selectitem.md) |
| 67 | `crm_sellchance` | 24 | `id`(id)、`creater`(创建者)、`subject`(标题)、`customerid`(相关客户) 等共 24 个字段 | [crm_sellchance.md](./tables/客户管理/crm_sellchance.md) |
| 68 | `crm_sellchance_label` | 4 | `id`(id)、`userid`(人员id)、`sellchanceid`(商机id)、`labelid`(标签id) | [crm_sellchance_label.md](./tables/客户管理/crm_sellchance_label.md) |
| 69 | `crm_sellchanceatt` | 3 | `id`(id)、`resourceid`(人员id)、`sellchanceid`(销售机会id) | [crm_sellchanceatt.md](./tables/客户管理/crm_sellchanceatt.md) |
| 70 | `crm_sellchancelabel` | 10 | `id`(id)、`userid`(人员id)、`name`(标签名称)、`labelcolor`(标签颜色) 等共 10 个字段 | [crm_sellchancelabel.md](./tables/客户管理/crm_sellchancelabel.md) |
| 71 | `crm_sellstatus` | 3 | `id`(id)、`fullname`(名称)、`description`(描述) | [crm_sellstatus.md](./tables/客户管理/crm_sellstatus.md) |
| 72 | `crm_selltimespan` | 3 | `id`(id)、`timespan`(销售期间)、`spannum`(销售期间数) | [crm_selltimespan.md](./tables/客户管理/crm_selltimespan.md) |
| 73 | `crm_selltypes` | 3 | `id`(id)、`fullname`(名称)、`description`(描述) | [crm_selltypes.md](./tables/客户管理/crm_selltypes.md) |
| 74 | `crm_shareinfo` | 20 | `id`(id)、`relateditemid`(相关客户id)、`sharetype`(共享类型)、`seclevel`(最低安全级别) 等共 20 个字段 | [crm_shareinfo.md](./tables/客户管理/crm_shareinfo.md) |
| 75 | `crm_successfactor` | 4 | `id`(id)、`fullname`(名称)、`description`(描述)、`orderkey`(排序字段) | [crm_successfactor.md](./tables/客户管理/crm_successfactor.md) |
| 76 | `crm_t_shareinfo` | 16 | `id`(id)、`relateditemid`(相关联对象ID)、`sharetype`(共享类型)、`seclevel`(安全级别) 等共 16 个字段 | [crm_t_shareinfo.md](./tables/客户管理/crm_t_shareinfo.md) |
| 77 | `crm_todblog` | 8 | `logtype`(日志类型)、`submitdate`(日期)、`submittime`(时间)、`submiter`(操作者) 等共 8 个字段 | [crm_todblog.md](./tables/客户管理/crm_todblog.md) |
| 78 | `crm_todblogdetail` | 4 | `id`(id)、`customerid`(客户id)、`logid`(导入日志id)、`operationtype`(操作类型) | [crm_todblogdetail.md](./tables/客户管理/crm_todblogdetail.md) |
| 79 | `crm_tradeinfo表` | 5 | `id`(id)、`fullname`(名称)、`rangelower`(下限金额)、`rangeupper`(上限金额) 等共 5 个字段 | [crm_tradeinfo表.md](./tables/客户管理/crm_tradeinfo表.md) |
| 80 | `crm_viewlog` | 6 | `customerid`(客户id)、`type`(查看客户信息)、`modifydate`(修改日期)、`modifytime`(修改时间) 等共 6 个字段 | [crm_viewlog.md](./tables/客户管理/crm_viewlog.md) |
| 81 | `crm_viewlog1` | 6 | `id`(id)、`viewer`(浏览者)、`viewdate`(浏览日期)、`viewtime`(浏览时间) 等共 6 个字段 | [crm_viewlog1.md](./tables/客户管理/crm_viewlog1.md) |
| 82 | `crm_viewlog2` | 5 | `customerid`(客户id)、`oldmanager`(旧的客户经理)、`newmanager`(新的客户经理)、`movedate`(转移日期) 等共 5 个字段 | [crm_viewlog2.md](./tables/客户管理/crm_viewlog2.md) |
| 83 | `crmsharedetail` | 4 | `crmid`(客户id)、`userid`(人员id)、`usertype`(用户类型)、`sharelevel`(用户级别) | [crmsharedetail.md](./tables/客户管理/crmsharedetail.md) |
| 84 | `crmshareinittable` | 1 | `isinitialized`(是否初始化过) | [crmshareinittable.md](./tables/客户管理/crmshareinittable.md) |
| 85 | `exchange_info` | 21 | `id`(编号)、`sortid`(待定)、`name`(待定)、`remarkold`(待定) 等共 21 个字段 | [exchange_info.md](./tables/客户管理/exchange_info.md) |
| 86 | `lgcasset` | 14 | `id`(id)、`assetmark`(产品编号)、`barcode`(代码)、`seclevel`(安全级别) 等共 14 个字段 | [lgcasset.md](./tables/客户管理/lgcasset.md) |
| 87 | `lgcassetassortment` | 51 | `id`(id)、`assortmentmark`(产品种类编号)、`assortmentname`(产品种类名称)、`seclevel`(安全级别) 等共 51 个字段 | [lgcassetassortment.md](./tables/客户管理/lgcassetassortment.md) |
| 88 | `lgcassetcountry` | 37 | `textfield3`(文本字符串类型)、`textfield4`(文本字符串类型)、`textfield5`(文本字符串类型)、`tinyintfield1`(整数类型) 等共 37 个字段 | [lgcassetcountry.md](./tables/客户管理/lgcassetcountry.md) |
| 89 | `lgcassetcrm` | 14 | `id`(id)、`assetid`(产品id)、`crmid`(供应商id)、`countryid`(国家id) 等共 14 个字段 | [lgcassetcrm.md](./tables/客户管理/lgcassetcrm.md) |
| 90 | `lgcassetprice` | 9 | `id`(id)、`assetid`(产品编号)、`assetcountyid`(产品国家id)、`pricedesc`(价格描述) 等共 9 个字段 | [lgcassetprice.md](./tables/客户管理/lgcassetprice.md) |
| 91 | `lgcassetrelationtype` | 6 | `id`(id)、`typename`(产品配置类型名称)、`typedesc`(产品类型说明)、`typekind`(类型) 等共 6 个字段 | [lgcassetrelationtype.md](./tables/客户管理/lgcassetrelationtype.md) |
| 92 | `lgcassetstock` | 5 | `id`(id)、`warehouseid`(仓库id)、`assetid`(产品id)、`stocknum`(期初数) 等共 5 个字段 | [lgcassetstock.md](./tables/客户管理/lgcassetstock.md) |
| 93 | `lgcassettype` | 4 | `id`(id)、`typemark`(编号)、`typename`(名称)、`typedesc`(说明) | [lgcassettype.md](./tables/客户管理/lgcassettype.md) |
| 94 | `lgcassetunit` | 4 | `id`(id)、`unitmark`(单位编码)、`unitname`(单位名称)、`unitdesc`(描述) | [lgcassetunit.md](./tables/客户管理/lgcassetunit.md) |
| 95 | `lgccatalogs` | 50 | `id`(id)、`catalogname`(名称)、`catalogdesc`(说明)、`catalogorder`(排序) 等共 50 个字段 | [lgccatalogs.md](./tables/客户管理/lgccatalogs.md) |
| 96 | `lgcconfiguration` | 4 | `supassetid`(资产id)、`subassetid`(关联资产id)、`relationtypeid`(类型id)、`id`(id) | [lgcconfiguration.md](./tables/客户管理/lgcconfiguration.md) |
| 97 | `lgccounttype` | 10 | `id`(id)、`typename`(类型名称)、`typedesc`(类型描述)、`salesinid`(销售收入科目) 等共 10 个字段 | [lgccounttype.md](./tables/客户管理/lgccounttype.md) |
| 98 | `lgcpaymenttype` | 4 | `id`(id)、`typename`(类型名称)、`typedesc`(类型说明)、`paymentid`(支付方式) | [lgcpaymenttype.md](./tables/客户管理/lgcpaymenttype.md) |
| 99 | `lgcwarehouse` | 4 | `id`(id)、`warehousename`(仓库名称)、`warehousedesc`(仓库描述)、`roleid`(角色id) | [lgcwarehouse.md](./tables/客户管理/lgcwarehouse.md) |
| 100 | `lgcwebshop` | 18 | `id`(id)、`usertype`(收货人类型)、`userid`(收货人id)、`username`(收货人名称) 等共 18 个字段 | [lgcwebshop.md](./tables/客户管理/lgcwebshop.md) |
| 101 | `lgcwebshopdetail` | 8 | `id`(id)、`webshopid`(订单id)、`assetid`(商品id)、`countryid`(国家id) 等共 8 个字段 | [lgcwebshopdetail.md](./tables/客户管理/lgcwebshopdetail.md) |
| 102 | `lgcwebshopreceivetype` | 4 | `id`(id)、`typename`(名称)、`typeesc`(说明)、`typecountry`(国家) | [lgcwebshopreceivetype.md](./tables/客户管理/lgcwebshopreceivetype.md) |
| 103 | `shareinittable` | 1 | `isinitialized`(是否初始化过) | [shareinittable.md](./tables/客户管理/shareinittable.md) |

### 知识管理

> 本模块共收录 `92` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `codedetail` | 5 | `id`(ID)、`codemainid`(对应主表id)、`showname`(显示名称)、`showtype`(显示类型) 等共 5 个字段 | [codedetail.md](./tables/知识管理/codedetail.md) |
| 2 | `codemain` | 11 | `id`(ID)、`titleimg`(编码图像)、`titlename`(编码主题)、`isuse`(是否有效) 等共 11 个字段 | [codemain.md](./tables/知识管理/codemain.md) |
| 3 | `cus_formdict` | 8 | `qfws`(？)、`id`(ID)、`fielddbtype`(字段数据库类型)、`fieldhtmltype`(字段页面类型) 等共 8 个字段 | [cus_formdict.md](./tables/知识管理/cus_formdict.md) |
| 4 | `cus_formfield` | 13 | `scope`(范围)、`scopeid`(范围id)、`fieldlable`(字段显示名)、`fieldid`(字段id) 等共 13 个字段 | [cus_formfield.md](./tables/知识管理/cus_formfield.md) |
| 5 | `cus_formsetting` | 10 | `id`(ID)、`module`(模块)、`page`(调用的页面)、`status`(状态) 等共 10 个字段 | [cus_formsetting.md](./tables/知识管理/cus_formsetting.md) |
| 6 | `cus_selectitem` | 8 | `hrm_isdefault`(默认)、`fieldid`(字段id)、`selectvalue`(下拉框选项值)、`selectname`(下拉框选项显示名称) 等共 8 个字段 | [cus_selectitem.md](./tables/知识管理/cus_selectitem.md) |
| 7 | `cus_treeform` | 6 | `scope`(范围)、`formlabel`(显示名称)、`id`(显示标识)、`parentid`(父节点id) 等共 6 个字段 | [cus_treeform.md](./tables/知识管理/cus_treeform.md) |
| 8 | `diraccesscontroldetail` | 3 | `id`(ID)、`sourceid`(目录id)、`type`(授权类型) | [diraccesscontroldetail.md](./tables/知识管理/diraccesscontroldetail.md) |
| 9 | `diraccesscontrollist` | 7 | `joblevel`(岗位级别)、`jobdepartment`(指定部门)、`jobsubcompany`(指定分部)、`jobids`(岗位) 等共 7 个字段 | [diraccesscontrollist.md](./tables/知识管理/diraccesscontrollist.md) |
| 10 | `diraccesspermission1` | 9 | `dirid`(目录id)、`dirtype`(目录类型)、`userid`(用户id)、`usertype`(用户类型) 等共 9 个字段 | [diraccesspermission1.md](./tables/知识管理/diraccesspermission1.md) |
| 11 | `doc_prop` | 4 | `id`(id)、`propkey`(属性功能)、`propvalue`(属性值)、`propdesc`(属性说明) | [doc_prop.md](./tables/知识管理/doc_prop.md) |
| 12 | `doc_reply` | 11 | `id`(回复id)、`docid`(文档id)、`userid`(回复对象)、`reply_parentid`(主回复（根节点回复）) 等共 11 个字段 | [doc_reply.md](./tables/知识管理/doc_reply.md) |
| 13 | `docapproveremark` | 7 | `id`(ID)、`docid`(文档id)、`approveremark`(审批意见)、`approverid`(审批人) 等共 7 个字段 | [docapproveremark.md](./tables/知识管理/docapproveremark.md) |
| 14 | `docapprovewf` | 5 | `id`(ID)、`docid`(文档id)、`approvetype`(审批类型)、`requestid`(请求id) 等共 5 个字段 | [docapprovewf.md](./tables/知识管理/docapprovewf.md) |
| 15 | `doccategoryusecount` | 3 | `secid`(子目录id)、`userid`(创建者id)、`count`(创建次数) | [doccategoryusecount.md](./tables/知识管理/doccategoryusecount.md) |
| 16 | `docchangesetting` | 19 | `autosend`(是否自动发送)、`autosendtime`(自动发送间隔分钟)、`autoreceive`(是否自动发送)、`autoreceivetime`(自动接收间隔分钟) 等共 19 个字段 | [docchangesetting.md](./tables/知识管理/docchangesetting.md) |
| 17 | `docconditiondetail` | 3 | `mouldid`(模板id)、`name`(名称)、`value`(值) | [docconditiondetail.md](./tables/知识管理/docconditiondetail.md) |
| 18 | `docconditionmould` | 6 | `id`(id)、`name`(用户名)、`userid`(用户id)、`usertype`(用户类型) 等共 6 个字段 | [docconditionmould.md](./tables/知识管理/docconditionmould.md) |
| 19 | `docdetail` | 53 | `sumdownload`(下载量)、`accessorycount`(附件个数)、`replaydoccount`(回复文档的数量)、`usertype`(用户类型) 等共 53 个字段 | [docdetail.md](./tables/知识管理/docdetail.md) |
| 20 | `docdetailcontent` | 2 | `docid`(文档id)、`doccontent`(文档内容) | [docdetailcontent.md](./tables/知识管理/docdetailcontent.md) |
| 21 | `docdetaillog` | 5 | `id`(ID)、`docid`(文档id)、`docsubject`(文档主题)、`doccreater`(文档创建者) 等共 5 个字段 | [docdetaillog.md](./tables/知识管理/docdetaillog.md) |
| 22 | `docdocumentsignature` | 7 | `id`(ID)、`versionid`(签章的文档具体的版本)、`markname`(签章名称)、`username`(用户名称) 等共 7 个字段 | [docdocumentsignature.md](./tables/知识管理/docdocumentsignature.md) |
| 23 | `docdummydetail` | 8 | `id`(ID)、`catelogid`(虚拟目录id)、`docid`(文档id)、`importdate`(导入日期) 等共 8 个字段 | [docdummydetail.md](./tables/知识管理/docdummydetail.md) |
| 24 | `docfrontpage` | 6 | `id`(ID)、`frontpagename`(新闻页名称)、`frontpagedesc`(新闻页描述)、`isactive`(是否活跃) 等共 6 个字段 | [docfrontpage.md](./tables/知识管理/docfrontpage.md) |
| 25 | `docftpconfig` | 10 | `id`(ID)、`ftpconfigname`(ftp服务器名称)、`ftpconfigdesc`(ftp服务器描述)、`serverip`(ftp服务器地址) 等共 10 个字段 | [docftpconfig.md](./tables/知识管理/docftpconfig.md) |
| 26 | `dochandwrittencolor` | 4 | `id`(ID)、`namecn`(中文名称)、`nameen`(英文名称)、`hexrgb`(十六进制rgb) | [dochandwrittencolor.md](./tables/知识管理/dochandwrittencolor.md) |
| 27 | `dochandwrittendetail` | 5 | `id`(ID)、`docid`(文档id)、`doceditionid`(文档版本id)、`username`(用户名) 等共 5 个字段 | [dochandwrittendetail.md](./tables/知识管理/dochandwrittendetail.md) |
| 28 | `docimagefile` | 10 | `signaturecount`(签章)、`id`(id)、`docid`(对应文档id)、`imagefileid`(图片文件id) 等共 10 个字段 | [docimagefile.md](./tables/知识管理/docimagefile.md) |
| 29 | `docmaincategory` | 7 | `id`(由用户定义的主目录id)、`categoryname`(主目录描述)、`categoryiconid`(主目录图片的id)、`categoryorder`(主目录的显示顺序) 等共 7 个字段 | [docmaincategory.md](./tables/知识管理/docmaincategory.md) |
| 30 | `docmaincatftpconfig` | 5 | `id`(ID)、`maincategoryid`(主目录id)、`refreshsubandsec`(是否更新分目录和子目录设置)、`isuseftp`(是否启用) 等共 5 个字段 | [docmaincatftpconfig.md](./tables/知识管理/docmaincatftpconfig.md) |
| 31 | `docmark` | 7 | `id`(ID)、`docid`(文档id)、`markhrmtype`(打分人用户类型)、`markhrmid`(打分人用户id) 等共 7 个字段 | [docmark.md](./tables/知识管理/docmark.md) |
| 32 | `docmould` | 10 | `id`(文档模板id)、`mouldname`(文档模板描述)、`mouldtext`(文档模板html)、`issysdefault`(是否系统默认) 等共 10 个字段 | [docmould.md](./tables/知识管理/docmould.md) |
| 33 | `docmouldbookmark` | 5 | `id`(ID)、`docid`(文档id)、`mouldid`(模板id)、`bookmarkid`(书签id) 等共 5 个字段 | [docmouldbookmark.md](./tables/知识管理/docmouldbookmark.md) |
| 34 | `docmouldfile` | 4 | `id`(文档模板id)、`mouldname`(文档模板描述)、`mouldtext`(文档模板html)、`mouldtype`(模板文档类型) | [docmouldfile.md](./tables/知识管理/docmouldfile.md) |
| 35 | `docpicupload` | 3 | `id`(上传图片id)、`picname`(上传图片描述)、`pictype`(上传图片种类) | [docpicupload.md](./tables/知识管理/docpicupload.md) |
| 36 | `docpopupinfo` | 8 | `docid`(文档id)、`pop_startdate`(开始时间)、`pop_enddate`(结束时间)、`pop_num`(文档弹出次数) 等共 8 个字段 | [docpopupinfo.md](./tables/知识管理/docpopupinfo.md) |
| 37 | `docpopupuser` | 5 | `id`(ID)、`userid`(用户id)、`docid`(文档id)、`haspopnum`(已经弹出次数) 等共 5 个字段 | [docpopupuser.md](./tables/知识管理/docpopupuser.md) |
| 38 | `docpreview` | 17 | `id`(ID)、`imagefileid`(附件id)、`filepath`(临时文件路径)、`pdffileid`(pdf附件id) 等共 17 个字段 | [docpreview.md](./tables/知识管理/docpreview.md) |
| 39 | `docpreviewhistory` | 17 | `id`(ID)、`imagefileid`(附件id)、`filepath`(临时文件路径)、`pdffileid`(pdf附件id) 等共 17 个字段 | [docpreviewhistory.md](./tables/知识管理/docpreviewhistory.md) |
| 40 | `docpreviewhtml` | 12 | `id`(ID)、`imagefileid`(附件id)、`htmlfileid`(html附件id)、`previewcount`(预览次数) 等共 12 个字段 | [docpreviewhtml.md](./tables/知识管理/docpreviewhtml.md) |
| 41 | `docpreviewhtmlhistory` | 12 | `id`(ID)、`imagefileid`(附件id)、`htmlfileid`(html附件id)、`previewcount`(预览次数) 等共 12 个字段 | [docpreviewhtmlhistory.md](./tables/知识管理/docpreviewhtmlhistory.md) |
| 42 | `docpreviewhtmlimage` | 4 | `id`(ID)、`imagefileid`(附件id)、`picfileid`(pic附件id)、`docid`(文档id) | [docpreviewhtmlimage.md](./tables/知识管理/docpreviewhtmlimage.md) |
| 43 | `docprintlog` | 7 | `id`(ID)、`printuserid`(打印人员id)、`printdocid`(打印文档id)、`printdate`(打印日期) 等共 7 个字段 | [docprintlog.md](./tables/知识管理/docprintlog.md) |
| 44 | `docprivateseccategory` | 6 | `id`(目录id)、`categoryname`(目录名称)、`ecology_pinyin_search`(缩写)、`parentid`(父目录) 等共 6 个字段 | [docprivateseccategory.md](./tables/知识管理/docprivateseccategory.md) |
| 45 | `docreadtag` | 5 | `id`(ID)、`usertype`(用户类型)、`docid`(文档id)、`userid`(用户id) 等共 5 个字段 | [docreadtag.md](./tables/知识管理/docreadtag.md) |
| 46 | `docreceiveunit` | 14 | `unitcode`(编码)、`id`(收文单位id)、`receiveunitname`(收文单位名称)、`superiorunitid`(上级单位id) 等共 14 个字段 | [docreceiveunit.md](./tables/知识管理/docreceiveunit.md) |
| 47 | `docsearchdefine` | 22 | `userid`(用户id)、`subjectdef`(主题字段是否为基本字段)、`contentdef`(内容字段是否为基本字段)、`replydef`(回复字段是否为基本字段) 等共 22 个字段 | [docsearchdefine.md](./tables/知识管理/docsearchdefine.md) |
| 48 | `docsearchmould` | 43 | `id`(查询模板id)、`mouldname`(查询模板描述)、`userid`(用户id)、`docsubject`(文档主题) 等共 43 个字段 | [docsearchmould.md](./tables/知识管理/docsearchmould.md) |
| 49 | `docseccategory` | 13 | `seccategorytype`(目录类型)、`uploadext`(附件上传限制格式)、`pushoperation`(推送操作)、`pushways`(推送方式) 等共 13 个字段 | [docseccategory.md](./tables/知识管理/docseccategory.md) |
| 50 | `docseccategoryapprovewfdetail` | 7 | `id`(ID)、`seccategoryid`(文挡子目录id)、`approvetype`(审批类型)、`workflowid`(审批流程) 等共 7 个字段 | [docseccategoryapprovewfdetail.md](./tables/知识管理/docseccategoryapprovewfdetail.md) |
| 51 | `docseccategorycoderseq` | 7 | `id`(ID)、`sequence`(流水号)、`yearseq`(如果日期单独流水且为年的情况下将使用这里的信息)、`monthseq`(如果日期单独流水且为月的情况下将使用这里的信息) 等共 7 个字段 | [docseccategorycoderseq.md](./tables/知识管理/docseccategorycoderseq.md) |
| 52 | `docseccategorycussearch` | 8 | `id`(ID)、`viewindex`(显示顺序)、`visible`(是否启用)、`seccategoryid`(文档目录id) 等共 8 个字段 | [docseccategorycussearch.md](./tables/知识管理/docseccategorycussearch.md) |
| 53 | `docseccategorydocproperty` | 16 | `id`(ID)、`seccategoryid`(子目录id)、`viewindex`(显示顺序)、`type`(类型) 等共 16 个字段 | [docseccategorydocproperty.md](./tables/知识管理/docseccategorydocproperty.md) |
| 54 | `docseccategoryimportfaildetail` | 6 | `id`(目录id)、`historyid`(历史目录id)、`failrow`(失败的行)、`failcol`(失败的列) 等共 6 个字段 | [docseccategoryimportfaildetail.md](./tables/知识管理/docseccategoryimportfaildetail.md) |
| 55 | `docseccategoryimporthistory` | 8 | `id`(目录id)、`filepath`(文件路径)、`operateuserid`(操作者)、`successnum`(成功数量) 等共 8 个字段 | [docseccategoryimporthistory.md](./tables/知识管理/docseccategoryimporthistory.md) |
| 56 | `docseccategorymould` | 3 | `id`(ID)、`seccategoryid`(子目录id)、`mouldtype`(模版类型) | [docseccategorymould.md](./tables/知识管理/docseccategorymould.md) |
| 57 | `docseccategorymouldbookmark` | 3 | `docseccategorymouldid`(主表id)、`bookmarkid`(书签id)、`docseccategorydocpropertyid`(文档属性页id) | [docseccategorymouldbookmark.md](./tables/知识管理/docseccategorymouldbookmark.md) |
| 58 | `docseccategoryshare` | 25 | `joblevel`(岗位级别)、`jobdepartment`(岗位指定部门)、`jobsubcompany`(岗位指定分部)、`jobids`(岗位) 等共 25 个字段 | [docseccategoryshare.md](./tables/知识管理/docseccategoryshare.md) |
| 59 | `docseccategorytemplate` | 12 | `uploadext`(附件上传控制格式)、`pushoperation`(推送设置)、`pushways`(推送方式)、`id`(子目录id) 等共 12 个字段 | [docseccategorytemplate.md](./tables/知识管理/docseccategorytemplate.md) |
| 60 | `docseccategorytype` | 2 | `seccategoryid`(子目录id)、`typeid`(文档种类id) | [docseccategorytype.md](./tables/知识管理/docseccategorytype.md) |
| 61 | `docsenddocdefaultvalue` | 2 | `categoryid`(目录id)、`createrid`(创建人id) | [docsenddocdefaultvalue.md](./tables/知识管理/docsenddocdefaultvalue.md) |
| 62 | `docsenddocdetail` | 23 | `id`(id)、`subject`(主题)、`docids`(文档id)、`dockind`(无) 等共 23 个字段 | [docsenddocdetail.md](./tables/知识管理/docsenddocdetail.md) |
| 63 | `docsharedetail` | 3 | `docid`(文档id)、`userid`(用户id)、`usertype`(用户类型) | [docsharedetail.md](./tables/知识管理/docsharedetail.md) |
| 64 | `docsubcategory` | 8 | `id`(ID)、`maincategoryid`(主目录id)、`categoryname`(分目录描述)、`subcategoryid`(分目录id) 等共 8 个字段 | [docsubcategory.md](./tables/知识管理/docsubcategory.md) |
| 65 | `docsubscribe` | 13 | `id`(ID)、`docid`(文档id)、`hrmid`(订阅申请者id)、`ownerid`(文档所有者id) 等共 13 个字段 | [docsubscribe.md](./tables/知识管理/docsubscribe.md) |
| 66 | `docsummation` | 3 | `docid`(文档id)、`countnum`(数量)、`type`(类型) | [docsummation.md](./tables/知识管理/docsummation.md) |
| 67 | `docsysdefault` | 2 | `fgpicwidth`(新闻页图片宽度)、`fgpicfixtype`(新闻页图片调整方式) | [docsysdefault.md](./tables/知识管理/docsysdefault.md) |
| 68 | `doctopservice` | 3 | `id`(id)、`docid`(文档id)、`operatetime`(操作时间) | [doctopservice.md](./tables/知识管理/doctopservice.md) |
| 69 | `doctreedocfield` | 10 | `id`(ID)、`treedocfieldname`(虚拟目录名称)、`superiorfieldid`(上级目录id)、`allsuperiorfieldid`(所有上级字段id) 等共 10 个字段 | [doctreedocfield.md](./tables/知识管理/doctreedocfield.md) |
| 70 | `doctype` | 24 | `hrmresclause`(选择人力资源的where子句)、`hrmreslabel`(选择人力资源项的标题)、`hascrm`(是否使用crm)、`crmclause`(选择crm的where子句) 等共 24 个字段 | [doctype.md](./tables/知识管理/doctype.md) |
| 71 | `docusercategory` | 5 | `secid`(子目录id)、`mainid`(主目录id)、`subid`(分目录id)、`userid`(用户id) 等共 5 个字段 | [docusercategory.md](./tables/知识管理/docusercategory.md) |
| 72 | `docuserdefault` | 14 | `id`(自定义条目id)、`userid`(用户id)、`hascreater`(文档列表是否显示创建者)、`hascreatedate`(文档列表是否显示创建日期) 等共 14 个字段 | [docuserdefault.md](./tables/知识管理/docuserdefault.md) |
| 73 | `docuserselfcategory` | 7 | `id`(ID)、`userid`(用户id)、`name`(目录名称)、`parentid`(上级目录id) 等共 7 个字段 | [docuserselfcategory.md](./tables/知识管理/docuserselfcategory.md) |
| 74 | `docuserselfdocs` | 5 | `docid`(文档id)、`usercatalogid`(目录id)、`userid`(用户id)、`doctype`(文档类型) 等共 5 个字段 | [docuserselfdocs.md](./tables/知识管理/docuserselfdocs.md) |
| 75 | `docuserview` | 2 | `docid`(文档id)、`userid`(用户id) | [docuserview.md](./tables/知识管理/docuserview.md) |
| 76 | `docwebcomment` | 7 | `id`(id)、`docid`(文档id)、`name`(名称)、`mail_1`(邮件) 等共 7 个字段 | [docwebcomment.md](./tables/知识管理/docwebcomment.md) |
| 77 | `downloadlog` | 8 | `userid`(用户id)、`username`(用户名称)、`downloadtime`(下载时间)、`imageid`(图片/附件id) 等共 8 个字段 | [downloadlog.md](./tables/知识管理/downloadlog.md) |
| 78 | `imagefile` | 22 | `delfilerealpath`(啥)、`iszip`(是否压缩)、`isencrypt`(是否加密)、`filesize`(文件大小) 等共 22 个字段 | [imagefile.md](./tables/知识管理/imagefile.md) |
| 79 | `imagefilebackup` | 2 | `id`(ID)、`imagefileid`(文件id) | [imagefilebackup.md](./tables/知识管理/imagefilebackup.md) |
| 80 | `imagefilesource` | 5 | `id`(ID)、`imagefileid`(文件id)、`comefrom`(来源)、`objid`(来源对象) 等共 5 个字段 | [imagefilesource.md](./tables/知识管理/imagefilesource.md) |
| 81 | `imagefiletemp` | 5 | `imagefileid`(文件id)、`docid`(文档id)、`createid`(创建人id)、`createdate`(创建日期) 等共 5 个字段 | [imagefiletemp.md](./tables/知识管理/imagefiletemp.md) |
| 82 | `imagefiletemppic` | 7 | `id`(ID)、`imagefileid`(文件id)、`docid`(文档id)、`createid`(创建人id) 等共 7 个字段 | [imagefiletemppic.md](./tables/知识管理/imagefiletemppic.md) |
| 83 | `mouldbookmark` | 5 | `id`(ID)、`mouldid`(模板id)、`name`(书签名)、`descript`(说明) 等共 5 个字段 | [mouldbookmark.md](./tables/知识管理/mouldbookmark.md) |
| 84 | `recycle_docdetail` | 107 | `id`(文档id)、`maincategory`(主目录)、`subcategory`(分目录)、`seccategory`(子目录) 等共 107 个字段 | [recycle_docdetail.md](./tables/知识管理/recycle_docdetail.md) |
| 85 | `recycle_docdetailcontent` | 2 | `docid`(文档id)、`doccontent`(文档内容) | [recycle_docdetailcontent.md](./tables/知识管理/recycle_docdetailcontent.md) |
| 86 | `recycle_docimagefile` | 14 | `id`(id)、`docid`(文档id)、`imagefileid`(附件id)、`imagefilename`(附件名称) 等共 14 个字段 | [recycle_docimagefile.md](./tables/知识管理/recycle_docimagefile.md) |
| 87 | `recycle_docshare` | 24 | `sharelevel`(安全级别)、`userid`(用户id)、`subcompanyid`(分部id)、`departmentid`(部门id) 等共 24 个字段 | [recycle_docshare.md](./tables/知识管理/recycle_docshare.md) |
| 88 | `recycle_imagefile` | 22 | `imagefileid`(附件id)、`imagefilename`(附件名称)、`imagefiletype`(附件类型)、`imagefile`(附件) 等共 22 个字段 | [recycle_imagefile.md](./tables/知识管理/recycle_imagefile.md) |
| 89 | `recycle_shareinnerdoc` | 14 | `id`(id)、`sourceid`(文档id)、`type`(共享类型)、`content`(共享内容) 等共 14 个字段 | [recycle_shareinnerdoc.md](./tables/知识管理/recycle_shareinnerdoc.md) |
| 90 | `seccreaterdocpope` | 21 | `id`(ID)、`secid`(目录id)、`pcreater`(文档创建人权限)、`pcreatermanager`(文档创建人直接上级权限) 等共 21 个字段 | [seccreaterdocpope.md](./tables/知识管理/seccreaterdocpope.md) |
| 91 | `shareinnerdoc` | 14 | `id`(ID)、`sourceid`(表示的是不同文档的id)、`type`(共享记录的类型)、`content`(如果当共享的类型为角色的时候. 其值表于为角色id角色级别id) 等共 14 个字段 | [shareinnerdoc.md](./tables/知识管理/shareinnerdoc.md) |
| 92 | `shareouterdoc` | 14 | `joblevel`(岗位级别)、`jobdepartment`(指定部门)、`jobsubcompany`(指定分部)、`id`(ID) 等共 14 个字段 | [shareouterdoc.md](./tables/知识管理/shareouterdoc.md) |

### 门户管理

> 本模块共收录 `53` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `favourite` | 7 | `id`(id)、`resourceid`(人员id)、`adddate`(加入时间)、`favouritename`(名称) 等共 7 个字段 | [favourite.md](./tables/门户管理/favourite.md) |
| 2 | `hp_element_picturesize` | 6 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`pictureheight`(图片高度) 等共 6 个字段 | [hp_element_picturesize.md](./tables/门户管理/hp_element_picturesize.md) |
| 3 | `hp_element_picturesize_t` | 6 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`pictureheight`(图片高度) 等共 6 个字段 | [hp_element_picturesize_t.md](./tables/门户管理/hp_element_picturesize_t.md) |
| 4 | `hp_element_showfield_use` | 5 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`showfield`(显示字段编号) 等共 5 个字段 | [hp_element_showfield_use.md](./tables/门户管理/hp_element_showfield_use.md) |
| 5 | `hp_element_showfield_use_t` | 5 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`showfield`(显示字段编号) 等共 5 个字段 | [hp_element_showfield_use_t.md](./tables/门户管理/hp_element_showfield_use_t.md) |
| 6 | `hp_mobile_baseelement` | 13 | `id`(元素id)、`elementtype`(元素类型)、`title`(默认标题)、`logo`(默认图标路径) 等共 13 个字段 | [hp_mobile_baseelement.md](./tables/门户管理/hp_mobile_baseelement.md) |
| 7 | `hp_mobile_element` | 23 | `id`(主键)、`title`(标题)、`logo`(元素图标ID)、`islocked`(是否锁定) 等共 23 个字段 | [hp_mobile_element.md](./tables/门户管理/hp_mobile_element.md) |
| 8 | `hp_mobile_hpinfo` | 17 | `publishid`(发布id)、`id`(主键（主页id）)、`infoname`(主页名称)、`infodesc`(描述) 等共 17 个字段 | [hp_mobile_hpinfo.md](./tables/门户管理/hp_mobile_hpinfo.md) |
| 9 | `hp_mobile_hplayout` | 5 | `id`(主键)、`hpid`(主页id)、`areaelement`(区域元素)、`userid`(用户id) 等共 5 个字段 | [hp_mobile_hplayout.md](./tables/门户管理/hp_mobile_hplayout.md) |
| 10 | `hp_mobile_ptaccesscontrollist` | 17 | `mainid`(主键)、`dirid`(目录id)、`dirtype`(目录类型)、`seclevel`(安全级别下限) 等共 17 个字段 | [hp_mobile_ptaccesscontrollist.md](./tables/门户管理/hp_mobile_ptaccesscontrollist.md) |
| 11 | `hp_mobile_shareinnerhp` | 11 | `id`(主键)、`hpid`(主页id)、`type`(共享类型)、`content`(内容) 等共 11 个字段 | [hp_mobile_shareinnerhp.md](./tables/门户管理/hp_mobile_shareinnerhp.md) |
| 12 | `hp_nonstandard_func_server` | 4 | `id`(主键)、`funcid`(非标编号)、`serverid`(服务器节点id)、`status`(启用状态) | [hp_nonstandard_func_server.md](./tables/门户管理/hp_nonstandard_func_server.md) |
| 13 | `hp_server_info` | 3 | `id`(主键（节点id）)、`serverip`(节点ip地址)、`servertype`(节点类型) | [hp_server_info.md](./tables/门户管理/hp_server_info.md) |
| 14 | `hpbaseelementapi` | 2 | `elementid`(元素的ebaseid)、`api`(元素的api路径) | [hpbaseelementapi.md](./tables/门户管理/hpbaseelementapi.md) |
| 15 | `hpbaseelementcustom` | 9 | `perpage`(每页显示条数)、`linkmode`(链接方式)、`savemethod`(保存方法)、`moreurl`(更多页面url) 等共 9 个字段 | [hpbaseelementcustom.md](./tables/门户管理/hpbaseelementcustom.md) |
| 16 | `hpcommonmenu` | 7 | `linktype`(链接类型)、`id`(主键)、`userid`(用户ID)、`menutype`(菜单类型) 等共 7 个字段 | [hpcommonmenu.md](./tables/门户管理/hpcommonmenu.md) |
| 17 | `hpcurrenttabtemplate` | 5 | `id`(主键)、`eid`(元素id)、`currenttab`(当前tab页id)、`userid`(用户id) 等共 5 个字段 | [hpcurrenttabtemplate.md](./tables/门户管理/hpcurrenttabtemplate.md) |
| 18 | `hpcustompagetabinfo` | 3 | `eid`(元素id)、`tabid`(tab页id)、`sqlwhere`(信息组合) | [hpcustompagetabinfo.md](./tables/门户管理/hpcustompagetabinfo.md) |
| 19 | `hpdefualtsetting` | 2 | `subcompanyid`(分部id)、`hpid`(门户首页id) | [hpdefualtsetting.md](./tables/门户管理/hpdefualtsetting.md) |
| 20 | `hpechartstemplate` | 3 | `id`(主键)、`title`(标题)、`echartoption`(配置信息) | [hpechartstemplate.md](./tables/门户管理/hpechartstemplate.md) |
| 21 | `hpelement_notice` | 12 | `id`(主键id)、`title`(标题)、`content`(内容)、`imgsrc`(图片路径) 等共 12 个字段 | [hpelement_notice.md](./tables/门户管理/hpelement_notice.md) |
| 22 | `hpelement_slidesetting` | 6 | `id`(主键)、`eleid`(元素id)、`displaydesc`(显示方式)、`imgsrc`(图片地址) 等共 6 个字段 | [hpelement_slidesetting.md](./tables/门户管理/hpelement_slidesetting.md) |
| 23 | `hpelement_slidesettingtemplate` | 5 | `id`(主键)、`eid`(元素id)、`displaydesc`(显示方式)、`imgsrc`(图片路径) 等共 5 个字段 | [hpelement_slidesettingtemplate.md](./tables/门户管理/hpelement_slidesettingtemplate.md) |
| 24 | `hpelementimgtemplate` | 6 | `imagefileid`(图片文件ID)、`eid`(元素ID)、`filerealpath`(图片文件存放路径)、`miniimgpath`(缩略图存放路径) 等共 6 个字段 | [hpelementimgtemplate.md](./tables/门户管理/hpelementimgtemplate.md) |
| 25 | `hpelements_order_col_default` | 4 | `id`(主键)、`fieldname`(字段显示名)、`fieldcolumn`(字段显示列名)、`ebaseid`(原始元素id) | [hpelements_order_col_default.md](./tables/门户管理/hpelements_order_col_default.md) |
| 26 | `hpelements_order_col_use` | 6 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`colid`(排序字段编号) 等共 6 个字段 | [hpelements_order_col_use.md](./tables/门户管理/hpelements_order_col_use.md) |
| 27 | `hpelements_order_col_use_t` | 6 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`colid`(排序字段id) 等共 6 个字段 | [hpelements_order_col_use_t.md](./tables/门户管理/hpelements_order_col_use_t.md) |
| 28 | `hpelementsettingdetailtemplate` | 11 | `id`(主键id)、`userid`(用户ID或分部ID)、`usertype`(用户类型)、`eid`(元素ID) 等共 11 个字段 | [hpelementsettingdetailtemplate.md](./tables/门户管理/hpelementsettingdetailtemplate.md) |
| 29 | `hpelementsettingtemplate` | 4 | `id`(主键)、`eid`(元素id)、`name`(设置属性名)、`value`(设置属性值) | [hpelementsettingtemplate.md](./tables/门户管理/hpelementsettingtemplate.md) |
| 30 | `hpelementtemplate` | 25 | `id`(主键)、`eid`(元素id)、`title`(元素标题)、`ebaseid`(原始的元素表ID) 等共 25 个字段 | [hpelementtemplate.md](./tables/门户管理/hpelementtemplate.md) |
| 31 | `hpfieldlengthtemplate` | 10 | `id`(主键)、`eid`(元素id)、`userid`(用户id)、`usertype`(用户类型) 等共 10 个字段 | [hpfieldlengthtemplate.md](./tables/门户管理/hpfieldlengthtemplate.md) |
| 32 | `hpinfo_workflow` | 12 | `id`(主键ID)、`infoname`(名称)、`styleid`(样式ID)、`layoutid`(布局id) 等共 12 个字段 | [hpinfo_workflow.md](./tables/门户管理/hpinfo_workflow.md) |
| 33 | `hpmobilenavsetting` | 1 | `navstyleid`(原始样式id) | [hpmobilenavsetting.md](./tables/门户管理/hpmobilenavsetting.md) |
| 34 | `hpmobilestyle` | 8 | `styleid`(样式id)、`menustylename`(菜单样式名称)、`menustyletype`(菜单样式类型)、`menustylecreater`(菜单样式创建人) 等共 8 个字段 | [hpmobilestyle.md](./tables/门户管理/hpmobilestyle.md) |
| 35 | `hpnewstabinfotemplate` | 5 | `eid`(元素id)、`tabid`(tab页id)、`tabtitle`(tab页标题)、`sqlwhere`(参数组合) 等共 5 个字段 | [hpnewstabinfotemplate.md](./tables/门户管理/hpnewstabinfotemplate.md) |
| 36 | `hpnewstopinfo` | 14 | `id`(主键)、`stylename`(样式名称)、`type`(类型)、`lasteditdate`(最后更新日期) 等共 14 个字段 | [hpnewstopinfo.md](./tables/门户管理/hpnewstopinfo.md) |
| 37 | `hpoutdatasettingaddr` | 6 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`sourceid`(数据来源id) 等共 6 个字段 | [hpoutdatasettingaddr.md](./tables/门户管理/hpoutdatasettingaddr.md) |
| 38 | `hpoutdatasettingaddrtemplate` | 6 | `eid`(元素id)、`tabid`(tab页id)、`sourceid`(数据来源id)、`address`(集成登录设置) 等共 6 个字段 | [hpoutdatasettingaddrtemplate.md](./tables/门户管理/hpoutdatasettingaddrtemplate.md) |
| 39 | `hpoutdatasettingdef` | 12 | `id`(主键)、`pattern`(数据来源类型)、`source`(数据来源)、`area`(内容) 等共 12 个字段 | [hpoutdatasettingdef.md](./tables/门户管理/hpoutdatasettingdef.md) |
| 40 | `hpoutdatasettingdeftemplate` | 12 | `id`(主键)、`pattern`(数据来源类型)、`source`(数据来源)、`area`(内容) 等共 12 个字段 | [hpoutdatasettingdeftemplate.md](./tables/门户管理/hpoutdatasettingdeftemplate.md) |
| 41 | `hpoutdatasettingfield` | 8 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`showfield`(显示字段id) 等共 8 个字段 | [hpoutdatasettingfield.md](./tables/门户管理/hpoutdatasettingfield.md) |
| 42 | `hpoutdatasettingfieldtemplate` | 8 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`showfield`(显示字段id) 等共 8 个字段 | [hpoutdatasettingfieldtemplate.md](./tables/门户管理/hpoutdatasettingfieldtemplate.md) |
| 43 | `hpoutdatatabsetting` | 5 | `id`(主键)、`eid`(元素id)、`tabid`(tab页id)、`title`(标题名称) 等共 5 个字段 | [hpoutdatatabsetting.md](./tables/门户管理/hpoutdatatabsetting.md) |
| 44 | `hpoutdatatabsettingtemplate` | 5 | `eid`(元素id)、`tabid`(tab页id)、`title`(标题名称)、`type`(数据类型) 等共 5 个字段 | [hpoutdatatabsettingtemplate.md](./tables/门户管理/hpoutdatatabsettingtemplate.md) |
| 45 | `hppluginsetting` | 6 | `pid`(插件id)、`plugindesc`(插件描述)、`filepath`(插件文件链接地址)、`isuse`(是否使用) 等共 6 个字段 | [hppluginsetting.md](./tables/门户管理/hppluginsetting.md) |
| 46 | `hpreportformtemplate` | 4 | `id`(主键)、`title`(标题)、`creator`(创建人)、`reportformsql`(报表sql) | [hpreportformtemplate.md](./tables/门户管理/hpreportformtemplate.md) |
| 47 | `hpsetting_wfcentertemplate` | 15 | `id`(主键)、`eid`(元素id)、`viewtype`(流程查看类型)、`typeids`(流程类型id) 等共 15 个字段 | [hpsetting_wfcentertemplate.md](./tables/门户管理/hpsetting_wfcentertemplate.md) |
| 48 | `hpsysremind` | 3 | `id`(主键)、`eid`(元素id)、`orderid`(顺序id) | [hpsysremind.md](./tables/门户管理/hpsysremind.md) |
| 49 | `hpsysremindtemplate` | 3 | `id`(主键)、`eid`(元素id)、`orderid`(顺序id) | [hpsysremindtemplate.md](./tables/门户管理/hpsysremindtemplate.md) |
| 50 | `hpwf_order_col_default` | 3 | `id`(主键ID)、`fieldname`(显示字段标签)、`fieldcolumn`(显示字段列名) | [hpwf_order_col_default.md](./tables/门户管理/hpwf_order_col_default.md) |
| 51 | `hpwf_order_col_use` | 6 | `id`(主键id)、`eid`(元素id)、`tabid`(tab页id)、`colid`(显示字段id) 等共 6 个字段 | [hpwf_order_col_use.md](./tables/门户管理/hpwf_order_col_use.md) |
| 52 | `menucontrollist` | 3 | `type`(菜单类型)、`menuid`(菜单id)、`isopen`(是否开启) | [menucontrollist.md](./tables/门户管理/menucontrollist.md) |
| 53 | `workflowsettingdetailtemplate` | 6 | `id`(自增列ID)、`eid`(元素id)、`tabid`(tab页id)、`type`(流程来源类型) 等共 6 个字段 | [workflowsettingdetailtemplate.md](./tables/门户管理/workflowsettingdetailtemplate.md) |

### 公文管理

> 本模块共收录 `49` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `bill_docprintapply` | 8 | `id`(编号)、`resourceid`(资源编号)、`deptid`(单位编号)、`relateddocid`(相关文档编号) 等共 8 个字段 | [bill_docprintapply.md](./tables/公文管理/bill_docprintapply.md) |
| 2 | `bill_innersenddoc` | 28 | `id`(编号)、`requestid`(请求编号)、`resourceid`(资源编号)、`departmentid`(部门编号) 等共 28 个字段 | [bill_innersenddoc.md](./tables/公文管理/bill_innersenddoc.md) |
| 3 | `bill_senddoc` | 28 | `generalmanagercheck`(管理员核查)、`resourceid_1`(资源编号1)、`resourceid_2`(资源编号2)、`resourceid_3`(资源编号3) 等共 28 个字段 | [bill_senddoc.md](./tables/公文管理/bill_senddoc.md) |
| 4 | `commreceivegroup` | 10 | `id`(编号)、`unitgroupid`(组编号)、`type`(类型)、`content`(类型对应的ID) 等共 10 个字段 | [commreceivegroup.md](./tables/公文管理/commreceivegroup.md) |
| 5 | `docchangefieldconfig` | 9 | `chageflag`(交换标志)、`companyid`(单位编号)、`version`(版本)、`workflowid`(流程编号) 等共 9 个字段 | [docchangefieldconfig.md](./tables/公文管理/docchangefieldconfig.md) |
| 6 | `docchangereceive` | 20 | `id`(编号)、`type`(类型)、`imagefileid`(文档编号)、`sn`(文号) 等共 20 个字段 | [docchangereceive.md](./tables/公文管理/docchangereceive.md) |
| 7 | `docchangereceivefield` | 7 | `chageflag`(是否交换)、`companyid`(单位编号)、`sn`(序号)、`version`(版本) 等共 7 个字段 | [docchangereceivefield.md](./tables/公文管理/docchangereceivefield.md) |
| 8 | `docchangereceivewf` | 6 | `id`(编号)、`receiveid`(接收编号)、`requestid`(请求编号)、`createdate`(创建日期) 等共 6 个字段 | [docchangereceivewf.md](./tables/公文管理/docchangereceivewf.md) |
| 9 | `docchangesend` | 5 | `id`(编号)、`senddate`(发文日期)、`sendtime`(发文时间)、`requestid`(请求编号) 等共 5 个字段 | [docchangesend.md](./tables/公文管理/docchangesend.md) |
| 10 | `docchangesenddetail` | 8 | `id`(编号)、`type`(类型)、`receiver`(接收者)、`receivedate`(接收日期) 等共 8 个字段 | [docchangesenddetail.md](./tables/公文管理/docchangesenddetail.md) |
| 11 | `docchangewffield` | 9 | `workflowid`(工作流程编号)、`version`(版本)、`fieldid`(字段编号)、`ischange`(是否交换) 等共 9 个字段 | [docchangewffield.md](./tables/公文管理/docchangewffield.md) |
| 12 | `docchangeworkflow` | 10 | `id`(编号)、`createdate`(创建日期)、`createtime`(创建时间)、`workflowid`(工作流编号) 等共 10 个字段 | [docchangeworkflow.md](./tables/公文管理/docchangeworkflow.md) |
| 13 | `docinstancylevel` | 4 | `id`(ID)、`name`(名称)、`desc_n`(描述)、`showorder`(展示顺序) | [docinstancylevel.md](./tables/公文管理/docinstancylevel.md) |
| 14 | `docseccatftpconfig` | 5 | `id`(ID)、`seccategoryid`(子目录id)、`isuseftp`(是否启用)、`ftpconfigid`(ftp服务器配置id) 等共 5 个字段 | [docseccatftpconfig.md](./tables/公文管理/docseccatftpconfig.md) |
| 15 | `docsecretlevel` | 4 | `id`(ID)、`name`(秘密等级名称)、`desc_n`(秘密等级描述)、`showorder`(显示顺序) | [docsecretlevel.md](./tables/公文管理/docsecretlevel.md) |
| 16 | `docsenddockind` | 4 | `id`(ID)、`name`(公文种类名称)、`desc_n`(公文种类描述)、`showorder`(显示顺序) | [docsenddockind.md](./tables/公文管理/docsenddockind.md) |
| 17 | `docsenddocnumber` | 4 | `id`(ID)、`name`(发文字号名称)、`desc_n`(发文字号描述)、`showorder`(显示顺序) | [docsenddocnumber.md](./tables/公文管理/docsenddocnumber.md) |
| 18 | `docsubcatftpconfig` | 5 | `id`(ID)、`subcategoryid`(分目录id)、`refreshsec`(更新子目录设置)、`isuseftp`(是否启用) 等共 5 个字段 | [docsubcatftpconfig.md](./tables/公文管理/docsubcatftpconfig.md) |
| 19 | `exchange_receive_doc_info_oa` | 15 | `receive_date`(接收日期)、`receive_time`(接收时间)、`id`(编号)、`document_identifier`(公文标识) 等共 15 个字段 | [exchange_receive_doc_info_oa.md](./tables/公文管理/exchange_receive_doc_info_oa.md) |
| 20 | `exchange_receivemsgstatus_oa` | 10 | `receive_doc_info_oa_id`(收文信息编号)、`id`(编号)、`operator`(操作人编号)、`operate_date`(操作日期) 等共 10 个字段 | [exchange_receivemsgstatus_oa.md](./tables/公文管理/exchange_receivemsgstatus_oa.md) |
| 21 | `exchange_receiveunitlist_oa` | 9 | `oper_date`(操作日期)、`oper_time`(操作时间)、`type`(类型)、`id`(编号) 等共 9 个字段 | [exchange_receiveunitlist_oa.md](./tables/公文管理/exchange_receiveunitlist_oa.md) |
| 22 | `exchange_senddocinfo_oa` | 11 | `id`(编号)、`document_identifier`(公文标识)、`document_title`(公文标题)、`send_company_id`(发文单位编号) 等共 11 个字段 | [exchange_senddocinfo_oa.md](./tables/公文管理/exchange_senddocinfo_oa.md) |
| 23 | `it` | 12 | `inner1`(停用)、`lx1`(停用)、`lx2`(停用)、`mc`(停用) 等共 12 个字段 | [it.md](./tables/公文管理/it.md) |
| 24 | `odoc_exchange_com_admin` | 3 | `id`(编号)、`exchange_companyid`(交换单位编号)、`admin_userid`(交换单位管理员编号) | [odoc_exchange_com_admin.md](./tables/公文管理/odoc_exchange_com_admin.md) |
| 25 | `odoc_exchange_com_fieldattr` | 4 | `id`(编号)、`exchange_companyid`(交换单位编号)、`exchange_fieldidid`(交换字段编号)、`exchange_com_fieldname`(交换单位字段名称) | [odoc_exchange_com_fieldattr.md](./tables/公文管理/odoc_exchange_com_fieldattr.md) |
| 26 | `odoc_exchange_com_user` | 4 | `id`(编号)、`exchange_companyid`(交换单位编号)、`userid`(用户编号)、`description`(描述) | [odoc_exchange_com_user.md](./tables/公文管理/odoc_exchange_com_user.md) |
| 27 | `odoc_exchange_company` | 4 | `id`(编号)、`company_name`(交换单位名称)、`company_oa_addr`(交换单位地址)、`company_code`(交换单位编号) | [odoc_exchange_company.md](./tables/公文管理/odoc_exchange_company.md) |
| 28 | `odoc_exchange_docbase` | 12 | `id`(编号)、`document_identifier`(公文标识)、`document_title`(公文标题)、`issued_number_of_document`(发文号) 等共 12 个字段 | [odoc_exchange_docbase.md](./tables/公文管理/odoc_exchange_docbase.md) |
| 29 | `odoc_exchange_field` | 7 | `id`(编号)、`showname`(展示名称)、`xml_name`(xml名称)、`descript`(描述) 等共 7 个字段 | [odoc_exchange_field.md](./tables/公文管理/odoc_exchange_field.md) |
| 30 | `odoc_exchange_recieveinfo` | 6 | `is_received`(是否已经接收)、`id`(编号)、`document_identifier`(公文标识)、`receive_companyid`(接收单位编号) 等共 6 个字段 | [odoc_exchange_recieveinfo.md](./tables/公文管理/odoc_exchange_recieveinfo.md) |
| 31 | `odoc_exchange_status` | 9 | `note`(备注)、`id`(编号)、`receiveid`(收文单位编号)、`operator`(操作人编号) 等共 9 个字段 | [odoc_exchange_status.md](./tables/公文管理/odoc_exchange_status.md) |
| 32 | `odoc_formsignatueconfig` | 15 | `id`(编号)、`workflowid`(工作流编号)、`nodeid`(节点编号)、`synchallnodes`(是否同步所有节点) 等共 15 个字段 | [odoc_formsignatueconfig.md](./tables/公文管理/odoc_formsignatueconfig.md) |
| 33 | `odoc_hotterm` | 2 | `termword`(热门词)、`searchtimes`(搜索次数) | [odoc_hotterm.md](./tables/公文管理/odoc_hotterm.md) |
| 34 | `odoc_odoctype` | 4 | `id`(编号)、`type_name`(类型名称)、`type_describe`(类型描述)、`showorder`(显示顺序) | [odoc_odoctype.md](./tables/公文管理/odoc_odoctype.md) |
| 35 | `odoc_requestdoc` | 13 | `id`(编号)、`requestid`(请求编号)、`docid`(文档编号)、`officaltype`(公文过程) 等共 13 个字段 | [odoc_requestdoc.md](./tables/公文管理/odoc_requestdoc.md) |
| 36 | `odoc_requestdoc_hasinit` | 1 | `hasinit`(是否初始化) | [odoc_requestdoc_hasinit.md](./tables/公文管理/odoc_requestdoc_hasinit.md) |
| 37 | `odoc_topictype` | 4 | `showorder`(显示顺序)、`id`(编号)、`topic_name`(主题词名称)、`topic_describe`(主题词描述) | [odoc_topictype.md](./tables/公文管理/odoc_topictype.md) |
| 38 | `odocgroupmembers` | 3 | `id`(主键)、`groupid`(组编号)、`memberid`(单位编号) | [odocgroupmembers.md](./tables/公文管理/odocgroupmembers.md) |
| 39 | `odocofdset` | 4 | `id`(编号)、`convertissuerurl`(转换地址)、`unzipfilepath`(解压缩文件路径)、`convertmode`(转换方式) | [odocofdset.md](./tables/公文管理/odocofdset.md) |
| 40 | `odocofdwfset` | 12 | `id`(编号)、`workflowid`(工作流编号)、`convertnodes`(转换节点)、`signaturenodes`(签章结点) 等共 12 个字段 | [odocofdwfset.md](./tables/公文管理/odocofdwfset.md) |
| 41 | `receiveunit_group` | 5 | `id`(编号)、`receiveunitname`(接收单位名称)、`receiveunittype`(接收单位类型)、`operationid`(操作人编号) 等共 5 个字段 | [receiveunit_group.md](./tables/公文管理/receiveunit_group.md) |
| 42 | `workflow_createdoc` | 38 | `opentextinformnode`(打开正文节点)、`istextinform`(是否展示在表单)、`odoctype`(文档类型)、`id`(ID) 等共 38 个字段 | [workflow_createdoc.md](./tables/公文管理/workflow_createdoc.md) |
| 43 | `workflow_docshow` | 8 | `flowid`(流程id)、`selectitemid`(选择框选择项id)、`seccategoryid`(二级目录id)、`modulid`(显示模版标签id) 等共 8 个字段 | [workflow_docshow.md](./tables/公文管理/workflow_docshow.md) |
| 44 | `workflow_docshowedit` | 9 | `id`(ID)、`flowid`(流程id)、`selectitemid`(选择框类型字段id)、`seccategoryid`(子目录id) 等共 9 个字段 | [workflow_docshowedit.md](./tables/公文管理/workflow_docshowedit.md) |
| 45 | `workflow_mould` | 8 | `selectvalue`(选择框值)、`isdefault`(是否默认)、`id`(ID)、`workflowid`(流程id) 等共 8 个字段 | [workflow_mould.md](./tables/公文管理/workflow_mould.md) |
| 46 | `workflow_processdefine` | 9 | `showname`(显示名)、`id`(ID)、`sysid`(系统id)、`label`(标签) 等共 9 个字段 | [workflow_processdefine.md](./tables/公文管理/workflow_processdefine.md) |
| 47 | `workflow_texttoofd` | 8 | `id`(编号)、`requestid`(请求编号)、`docid`(正文ID)、`ofddocid`(OFD文档编号（对应docimagefile表中的docid）) 等共 8 个字段 | [workflow_texttoofd.md](./tables/公文管理/workflow_texttoofd.md) |
| 48 | `workflow_texttopdf` | 9 | `id`(ID)、`requestid`(请求id)、`docid`(被转换的文档id)、`pdfdocid`(转成pdf后的文档id) 等共 9 个字段 | [workflow_texttopdf.md](./tables/公文管理/workflow_texttopdf.md) |
| 49 | `workflow_texttopdfconfig` | 19 | `id`(ID)、`workflowid`(流程id)、`topdfnodeid`(转换节点id)、`pdfsavesecid`(转成pdf存放固定目录id) 等共 19 个字段 | [workflow_texttopdfconfig.md](./tables/公文管理/workflow_texttopdfconfig.md) |

### 会议管理

> 本模块共收录 `48` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `bill_meeting_dt1_topic` | 7 | `id`(ID)、`mainid`(对应流程主表id)、`subject`(议程主题)、`projid`(相关项目) 等共 7 个字段 | [bill_meeting_dt1_topic.md](./tables/会议管理/bill_meeting_dt1_topic.md) |
| 2 | `bill_meeting_dt2_service` | 5 | `id`(主键)、`mainid`(会议id)、`items`(服务项目)、`otheritem`(其他服务) 等共 5 个字段 | [bill_meeting_dt2_service.md](./tables/会议管理/bill_meeting_dt2_service.md) |
| 3 | `meeting` | 77 | `qrticket`(会议二维码)、`address`(会议地点)、`ck_address`(冲突检测用会议地点)、`ck_services`(冲突检测用会议服务) 等共 77 个字段 | [meeting.md](./tables/会议管理/meeting.md) |
| 4 | `meetingRoomScreenField` | 6 | `id`(ID)、`columns`(对应数据库名称)、`otherColumns`(其他名称)、`fieldLabel`(名称) 等共 6 个字段 | [meetingRoomScreenField.md](./tables/会议管理/meetingRoomScreenField.md) |
| 5 | `meetingRoomScreen_Set` | 15 | `id`(ID)、`name`(样式名称)、`showRoomName`(是否显示会议室名称)、`roomNameFontColor`(会议室名称字体颜色) 等共 15 个字段 | [meetingRoomScreen_Set.md](./tables/会议管理/meetingRoomScreen_Set.md) |
| 6 | `meeting_address` | 4 | `id`(主键)、`meetingtype`(会议类型)、`addressid`(地点id)、`desc_n`(描述) | [meeting_address.md](./tables/会议管理/meeting_address.md) |
| 7 | `meeting_bill` | 3 | `billid`(会议表单id)、`defined`(meeting_defind表中的scopeid)、`tablename`(会议流程表单对应的数据库表名) | [meeting_bill.md](./tables/会议管理/meeting_bill.md) |
| 8 | `meeting_decision` | 11 | `id`(主键)、`meetingid`(会议id)、`requestid`(会议决议通知流程请求id)、`coding`(决议编号) 等共 11 个字段 | [meeting_decision.md](./tables/会议管理/meeting_decision.md) |
| 9 | `meeting_defined` | 1 | `scopeid`(定义类型) | [meeting_defined.md](./tables/会议管理/meeting_defined.md) |
| 10 | `meeting_docshare` | 4 | `meetingid`(会议id)、`docid`(文档id或者附件id)、`type`(不同类型的文档)、`discussid`(type=3时,具体哪一条相关交流的id) | [meeting_docshare.md](./tables/会议管理/meeting_docshare.md) |
| 11 | `meeting_fieldgroup` | 5 | `id`(ID)、`grouplabel`(分组标签id,支持国际化)、`grouporder`(组排序)、`grouptype`(分组类型) 等共 5 个字段 | [meeting_fieldgroup.md](./tables/会议管理/meeting_fieldgroup.md) |
| 12 | `meeting_formfield` | 6 | `fieldid`(主键)、`fielddbtype`(对应数据库的类型)、`fieldname`(数据库字段名称)、`sysfieldlabel`(字段系统标签) 等共 6 个字段 | [meeting_formfield.md](./tables/会议管理/meeting_formfield.md) |
| 13 | `meeting_member` | 14 | `rolelevel`(角色等级)、`seclevel`(安全级别)、`seclevelmax`(最高安全级别)、`departmentid`(部门id) 等共 14 个字段 | [meeting_member.md](./tables/会议管理/meeting_member.md) |
| 14 | `meeting_member2` | 16 | `id`(主键)、`meetingid`(会议id)、`membertype`(人员类型)、`memberid`(参会人员id) 等共 16 个字段 | [meeting_member2.md](./tables/会议管理/meeting_member2.md) |
| 15 | `meeting_membercrm` | 9 | `id`(主键)、`meetingid`(会议id)、`memberrecid`(参会人员记录id)、`name`(姓名) 等共 9 个字段 | [meeting_membercrm.md](./tables/会议管理/meeting_membercrm.md) |
| 16 | `meeting_remind` | 4 | `id`(ID)、`meeting`(会议id)、`remindtime`(提醒时间)、`modetype`(提醒模式) | [meeting_remind.md](./tables/会议管理/meeting_remind.md) |
| 17 | `meeting_remind_mode` | 1 | `type`(会议不同提醒模式) | [meeting_remind_mode.md](./tables/会议管理/meeting_remind_mode.md) |
| 18 | `meeting_remind_template` | 6 | `id`(ID)、`type`(提醒方式)、`desc_n`(模板描述)、`title`(发送标题) 等共 6 个字段 | [meeting_remind_template.md](./tables/会议管理/meeting_remind_template.md) |
| 19 | `meeting_remind_type` | 8 | `isuse`(是否启用)、`settingurl`(设置url)、`sysrights`(设置权限)、`id`(ID) 等共 8 个字段 | [meeting_remind_type.md](./tables/会议管理/meeting_remind_type.md) |
| 20 | `meeting_repeat` | 4 | `id`(主键)、`meetingid`(会议id)、`begindate`(重复会议开始时间)、`doneflag`(结束标志) | [meeting_repeat.md](./tables/会议管理/meeting_repeat.md) |
| 21 | `meeting_selectitem` | 8 | `id`(ID)、`fieldid`(对应meeting_formfield的id)、`selectvalue`(选项值)、`selectname`(选项名称) 等共 8 个字段 | [meeting_selectitem.md](./tables/会议管理/meeting_selectitem.md) |
| 22 | `meeting_service` | 5 | `id`(ID)、`meetingtype`(服务类型)、`hrmid`(负责人员id)、`name`(负责人员名称) 等共 5 个字段 | [meeting_service.md](./tables/会议管理/meeting_service.md) |
| 23 | `meeting_service2` | 5 | `id`(会议服务id)、`meetingid`(会议标识)、`hrmid`(会议负责人id)、`name`(服务类型) 等共 5 个字段 | [meeting_service2.md](./tables/会议管理/meeting_service2.md) |
| 24 | `meeting_service_item` | 4 | `hrmids`(负责人)、`id`(ID)、`type`(服务类型id)、`itemname`(服务项目名称) | [meeting_service_item.md](./tables/会议管理/meeting_service_item.md) |
| 25 | `meeting_service_new` | 5 | `id`(主键)、`meetingid`(对应会议id)、`items`(选择的服务项目)、`hrmids`(负责人) 等共 5 个字段 | [meeting_service_new.md](./tables/会议管理/meeting_service_new.md) |
| 26 | `meeting_service_type` | 4 | `usecheck`(是否检查冲突)、`id`(ID)、`name`(服务类型名称)、`desc_n`(服务类型描述) | [meeting_service_type.md](./tables/会议管理/meeting_service_type.md) |
| 27 | `meeting_sharedetail` | 15 | `objid`(共享对象id)、`userid`(共享人员id)、`id`(主键)、`meetingid`(会议id) 等共 15 个字段 | [meeting_sharedetail.md](./tables/会议管理/meeting_sharedetail.md) |
| 28 | `meeting_sign` | 11 | `site`(签到地点)、`id`(主键)、`meetingid`(会议ID)、`userid`(参会人员ID) 等共 11 个字段 | [meeting_sign.md](./tables/会议管理/meeting_sign.md) |
| 29 | `meeting_topic` | 9 | `id`(ID)、`meetingid`(会议标识)、`subject`(议程主题)、`hrmid`(&nbsp;) 等共 9 个字段 | [meeting_topic.md](./tables/会议管理/meeting_topic.md) |
| 30 | `meeting_topicdate` | 7 | `id`(主键)、`meetingid`(会议id)、`topicid`(议程id)、`begindate`(开始日期) 等共 7 个字段 | [meeting_topicdate.md](./tables/会议管理/meeting_topicdate.md) |
| 31 | `meeting_topicdoc` | 5 | `id`(主键)、`meetingid`(会议id)、`topicid`(议程id)、`docid`(文档id) 等共 5 个字段 | [meeting_topicdoc.md](./tables/会议管理/meeting_topicdoc.md) |
| 32 | `meeting_type` | 9 | `id`(ID)、`name`(名称)、`approver`(审批工作流)、`desc_n`(说明) 等共 9 个字段 | [meeting_type.md](./tables/会议管理/meeting_type.md) |
| 33 | `meeting_view_status` | 5 | `id`(ID)、`meetingid`(会议id)、`userid`(人员id)、`usertype`(人员类型) 等共 5 个字段 | [meeting_view_status.md](./tables/会议管理/meeting_view_status.md) |
| 34 | `meeting_week_type` | 3 | `id`(星期id)、`name`(星期中文名)、`label`(星期标签id) | [meeting_week_type.md](./tables/会议管理/meeting_week_type.md) |
| 35 | `meeting_wf_relation` | 5 | `defined`(meeting_defind表中的scopeid)、`fieldid`(会议卡片字段id)、`fieldname`(会议卡片字段名称)、`billid`(会议表单id, formid) 等共 5 个字段 | [meeting_wf_relation.md](./tables/会议管理/meeting_wf_relation.md) |
| 36 | `meetingcaller` | 14 | `id`(主键)、`meetingtype`(会议类型)、`callertype`(召集人类型)、`seclevel`(安全级别) 等共 14 个字段 | [meetingcaller.md](./tables/会议管理/meetingcaller.md) |
| 37 | `meetinglog` | 13 | `id`(主键)、`relatedid`(会议记录id)、`relatedname`(会议名称)、`operatetype`(操作类型) 等共 13 个字段 | [meetinglog.md](./tables/会议管理/meetinglog.md) |
| 38 | `meetingmonitor` | 14 | `id`(主键id)、`jktype`(监控类型)、`jkvalue`(监控对应值)、`subcompanyid`(所属分部) 等共 14 个字段 | [meetingmonitor.md](./tables/会议管理/meetingmonitor.md) |
| 39 | `meetingmonitordt` | 2 | `mmid`(监控id)、`meetingtypeid`(会议类型id) | [meetingmonitordt.md](./tables/会议管理/meetingmonitordt.md) |
| 40 | `meetingroom` | 11 | `id`(ID)、`name`(会议室名称)、`roomdesc`(会议室描述)、`hrmid`(负责人) 等共 11 个字段 | [meetingroom.md](./tables/会议管理/meetingroom.md) |
| 41 | `meetingroom_share` | 3 | `id`(id)、`mid`(会议室id)、`permissiontype`(权限类型) | [meetingroom_share.md](./tables/会议管理/meetingroom_share.md) |
| 42 | `meetingroom_type` | 3 | `id`(主键id)、`name`(会议室分类名称)、`dsporder`(排序) | [meetingroom_type.md](./tables/会议管理/meetingroom_type.md) |
| 43 | `meetingset` | 52 | `canchange`(允许变更)、`serviceconflictchk`(服务冲突检验)、`serviceconflict`(服务冲突)、`zqhyzdkd`(周期最大跨度) 等共 52 个字段 | [meetingset.md](./tables/会议管理/meetingset.md) |
| 44 | `meetingshare` | 25 | `id`(主键)、`meetingid`(会议id)、`userid`(人力资源)、`usertype`(共享人员类型) 等共 25 个字段 | [meetingshare.md](./tables/会议管理/meetingshare.md) |
| 45 | `meetingshareset` | 22 | `id`(ID)、`meetingtype`(会议类型id)、`sharetype`(共享类型)、`seclevel`(所有人安全级别) 等共 22 个字段 | [meetingshareset.md](./tables/会议管理/meetingshareset.md) |
| 46 | `meetingsharetype` | 2 | `mmid`(会议共享设置ID)、`meetingtype`(会议类型) | [meetingsharetype.md](./tables/会议管理/meetingsharetype.md) |
| 47 | `meetingsign_set` | 10 | `fontsize`(字体大小)、`id`(主键id)、`meetingid`(会议id)、`bgcolor`(背景颜色) 等共 10 个字段 | [meetingsign_set.md](./tables/会议管理/meetingsign_set.md) |
| 48 | `meetingtype_share` | 3 | `id`(id)、`mtid`(会议类型id)、`permissiontype`(权限类型) | [meetingtype_share.md](./tables/会议管理/meetingtype_share.md) |

### 政务应用

> 本模块共收录 `47` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `govern_actionconfig` | 8 | `id`(id)、`categoryid`(类型id)、`actiontype`(动作类型)、`actionsetid`(action id) 等共 8 个字段 | [govern_actionconfig.md](./tables/政务应用/govern_actionconfig.md) |
| 2 | `govern_actionsetting` | 6 | `id`(id)、`categoryid`(类型id)、`actiontype`(动作类型)、`triggertype`(触发方式) 等共 6 个字段 | [govern_actionsetting.md](./tables/政务应用/govern_actionsetting.md) |
| 3 | `govern_attention` | 5 | `id`(数据id)、`userid`(用户id)、`taskid`(任务id)、`attdate`(关注日期) 等共 5 个字段 | [govern_attention.md](./tables/政务应用/govern_attention.md) |
| 4 | `govern_category` | 13 | `id`(id)、`name`(名称)、`isused`(是否启用)、`isauto`(是否自动下发) 等共 13 个字段 | [govern_category.md](./tables/政务应用/govern_category.md) |
| 5 | `govern_code` | 6 | `id`(数据id)、`isUse`(是否启用)、`categoryId`(督办类型id)、`codeFieldId`(编码字段) 等共 6 个字段 | [govern_code.md](./tables/政务应用/govern_code.md) |
| 6 | `govern_codeDetail` | 8 | `id`(数据id)、`codeMainId`(主编码id)、`showType`(编码类型)、`codeOrder`(排序) 等共 8 个字段 | [govern_codeDetail.md](./tables/政务应用/govern_codeDetail.md) |
| 7 | `govern_column` | 8 | `id`(id)、`name`(栏目名称)、`categoryid`(类型id)、`isuse`(是否启用) 等共 8 个字段 | [govern_column.md](./tables/政务应用/govern_column.md) |
| 8 | `govern_cutoff` | 8 | `id`(数据id)、`taskid`(办结任务id)、`categoryid`(督办类型id)、`requestid`(流程requestid) 等共 8 个字段 | [govern_cutoff.md](./tables/政务应用/govern_cutoff.md) |
| 9 | `govern_doc` | 7 | `id`(id)、`doctype`(类型)、`createdate`(创建日期)、`createtime`(创建时间) 等共 7 个字段 | [govern_doc.md](./tables/政务应用/govern_doc.md) |
| 10 | `govern_extension` | 13 | `id`(数据id)、`taskid`(延期任务id)、`categoryid`(督办类型id)、`requestid`(流程requestid) 等共 13 个字段 | [govern_extension.md](./tables/政务应用/govern_extension.md) |
| 11 | `govern_field` | 26 | `defaultvalue`(默认值)、`isinherit`(子任务是否继承)、`name`(字段显示名)、`issystem`(是否系统字段) 等共 26 个字段 | [govern_field.md](./tables/政务应用/govern_field.md) |
| 12 | `govern_instruct` | 10 | `content`(批示内容)、`id`(id)、`taskid`(数据id)、`userid`(用户id) 等共 10 个字段 | [govern_instruct.md](./tables/政务应用/govern_instruct.md) |
| 13 | `govern_log` | 6 | `id`(id)、`dealtype`(日志类型)、`userid`(用户id)、`dataid`(任务id) 等共 6 个字段 | [govern_log.md](./tables/政务应用/govern_log.md) |
| 14 | `govern_officialsetting` | 10 | `id`(id)、`categoryid`(类型id)、`type`(动作类型)、`triggertype`(触发方式) 等共 10 个字段 | [govern_officialsetting.md](./tables/政务应用/govern_officialsetting.md) |
| 15 | `govern_operator` | 20 | `id`(id)、`taskid`(任务id)、`projid`(事项id)、`categoryid`(类型id) 等共 20 个字段 | [govern_operator.md](./tables/政务应用/govern_operator.md) |
| 16 | `govern_prjsharedetail` | 15 | `id`(id)、`sourceid`(数据id)、`categoryid`(类型id)、`datatype`(废弃字段) 等共 15 个字段 | [govern_prjsharedetail.md](./tables/政务应用/govern_prjsharedetail.md) |
| 17 | `govern_project` | 9 | `remark`(描述)、`id`(id)、`categoryid`(类型id)、`creater`(创建人) 等共 9 个字段 | [govern_project.md](./tables/政务应用/govern_project.md) |
| 18 | `govern_prompt` | 9 | `promptcontent`(催办内容)、`flag`(是否显示催办标识)、`id`(数据id)、`topic`(催办主题) 等共 9 个字段 | [govern_prompt.md](./tables/政务应用/govern_prompt.md) |
| 19 | `govern_remind` | 17 | `id`(数据id)、`name`(提醒名称)、`isUsed`(是否启用)、`remindSms`(短信提醒) 等共 17 个字段 | [govern_remind.md](./tables/政务应用/govern_remind.md) |
| 20 | `govern_report` | 9 | `reportcontent`(汇报内容)、`id`(id)、`topic`(汇报主题)、`reportdate`(汇报日期) 等共 9 个字段 | [govern_report.md](./tables/政务应用/govern_report.md) |
| 21 | `govern_rightinfo` | 17 | `fieldid`(字段id)、`id`(id)、`categoryid`(类型id)、`opttype`(权限级别) 等共 17 个字段 | [govern_rightinfo.md](./tables/政务应用/govern_rightinfo.md) |
| 22 | `govern_selectitem` | 11 | `id`(id)、`fieldid`(字段id)、`selectvalue`(选择项值)、`selectname`(选择项显示名称) 等共 11 个字段 | [govern_selectitem.md](./tables/政务应用/govern_selectitem.md) |
| 23 | `govern_sharerule` | 19 | `id`(id)、`sourceid`(数据id)、`categoryid`(类型id)、`datatype`(类型) 等共 19 个字段 | [govern_sharerule.md](./tables/政务应用/govern_sharerule.md) |
| 24 | `govern_task` | 46 | `remark`(任务描述)、`id`(数据id)、`categoryid`(类型id)、`projid`(督办事项id) 等共 46 个字段 | [govern_task.md](./tables/政务应用/govern_task.md) |
| 25 | `govern_tasksharedetail` | 19 | `id`(id)、`sourceid`(数据id)、`categoryid`(类型id)、`datatype`(类型) 等共 19 个字段 | [govern_tasksharedetail.md](./tables/政务应用/govern_tasksharedetail.md) |
| 26 | `govern_triggersetting` | 4 | `id`(数据id)、`governfieldid`(督办字段id)、`flowfieldid`(流程字段id)、`triggerid`(触发id) | [govern_triggersetting.md](./tables/政务应用/govern_triggersetting.md) |
| 27 | `info_actionSetting` | 25 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`type`(类型) 等共 25 个字段 | [info_actionSetting.md](./tables/政务应用/info_actionSetting.md) |
| 28 | `info_adjustment` | 11 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`unitid`(单位id) 等共 11 个字段 | [info_adjustment.md](./tables/政务应用/info_adjustment.md) |
| 29 | `info_customunit` | 12 | `id`(数据id)、`uuid`(32位随机id)、`name`(单位名称)、`unitcode`(编码) 等共 12 个字段 | [info_customunit.md](./tables/政务应用/info_customunit.md) |
| 30 | `info_editrole` | 12 | `id`(数据id)、`uuid`(随机id)、`pathid`(路径id)、`sharetype`(权限类型) 等共 12 个字段 | [info_editrole.md](./tables/政务应用/info_editrole.md) |
| 31 | `info_editroleDetail` | 6 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`sharetype`(权限类型) 等共 6 个字段 | [info_editroleDetail.md](./tables/政务应用/info_editroleDetail.md) |
| 32 | `info_feedback` | 9 | `id`(数据id)、`uuid`(32位随机id)、`title`(标题)、`content`(反馈内容) 等共 9 个字段 | [info_feedback.md](./tables/政务应用/info_feedback.md) |
| 33 | `info_journal` | 24 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(所属路径)、`type`(期刊类型) 等共 24 个字段 | [info_journal.md](./tables/政务应用/info_journal.md) |
| 34 | `info_journal_detail` | 6 | `id`(数据id)、`uuid`(32位随机id)、`mainid`(期刊id)、`siftid`(待编信息id) 等共 6 个字段 | [info_journal_detail.md](./tables/政务应用/info_journal_detail.md) |
| 35 | `info_journalcolumn` | 5 | `id`(数据id)、`uuid`(32位随机id)、`mainid`(刊型id)、`name`(名称) 等共 5 个字段 | [info_journalcolumn.md](./tables/政务应用/info_journalcolumn.md) |
| 36 | `info_journaltype` | 16 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`name`(刊型名称) 等共 16 个字段 | [info_journaltype.md](./tables/政务应用/info_journaltype.md) |
| 37 | `info_log` | 10 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`infoid`(上报信息id) 等共 10 个字段 | [info_log.md](./tables/政务应用/info_log.md) |
| 38 | `info_path` | 19 | `id`(数据id)、`uuid`(32位随机id)、`name`(路径名称)、`isrepeat`(上报信息标题重复验证) 等共 19 个字段 | [info_path.md](./tables/政务应用/info_path.md) |
| 39 | `info_report` | 14 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`title`(标题) 等共 14 个字段 | [info_report.md](./tables/政务应用/info_report.md) |
| 40 | `info_reportunit` | 4 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`unitid`(单位id) | [info_reportunit.md](./tables/政务应用/info_reportunit.md) |
| 41 | `info_reward` | 22 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`name`(加分项名称) 等共 22 个字段 | [info_reward.md](./tables/政务应用/info_reward.md) |
| 42 | `info_reward_detail` | 7 | `id`(数据id)、`uuid`(32位随机id)、`mainid`(加分项id)、`type`(类型) 等共 7 个字段 | [info_reward_detail.md](./tables/政务应用/info_reward_detail.md) |
| 43 | `info_score` | 13 | `id`(数据id)、`uuid`(32位随机id)、`siftid`(待编信息id)、`infoid`(上报信息id) 等共 13 个字段 | [info_score.md](./tables/政务应用/info_score.md) |
| 44 | `info_sifting` | 27 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`infoid`(上报信息id) 等共 27 个字段 | [info_sifting.md](./tables/政务应用/info_sifting.md) |
| 45 | `info_unitdetail` | 5 | `id`(数据id)、`uuid`(32位随机id)、`mainid`(上报单位id)、`type`(数据类型) 等共 5 个字段 | [info_unitdetail.md](./tables/政务应用/info_unitdetail.md) |
| 46 | `info_unitgroup` | 6 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`name`(分组名称) 等共 6 个字段 | [info_unitgroup.md](./tables/政务应用/info_unitgroup.md) |
| 47 | `info_workflowConfig` | 5 | `id`(数据id)、`uuid`(32位随机id)、`pathid`(路径id)、`requestid`(流程请求id) 等共 5 个字段 | [info_workflowConfig.md](./tables/政务应用/info_workflowConfig.md) |

### 项目管理

> 本模块共收录 `47` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `prj_code` | 10 | `id`(标识id)、`isuse`(编码方式)、`subcompanyflow`(分部流水)、`departmentflow`(部门流水) 等共 10 个字段 | [prj_code.md](./tables/项目管理/prj_code.md) |
| 2 | `prj_codeseq` | 13 | `id`(标识id)、`sequenceid`(流水号)、`subcompanyid`(分部)、`departmentid`(部门) 等共 13 个字段 | [prj_codeseq.md](./tables/项目管理/prj_codeseq.md) |
| 3 | `prj_cpt` | 7 | `id`(标识id)、`prjid`(项目id)、`taskid`(任务id)、`isactived`(是否为活动任务) 等共 7 个字段 | [prj_cpt.md](./tables/项目管理/prj_cpt.md) |
| 4 | `prj_customer` | 6 | `id`(标识id)、`prjid`(项目id)、`taskid`(任务id)、`customerid`(客户id) 等共 6 个字段 | [prj_customer.md](./tables/项目管理/prj_customer.md) |
| 5 | `prj_doc` | 8 | `id`(标识id)、`prjid`(项目id)、`taskid`(任务id)、`isactived`(是否为活动任务) 等共 8 个字段 | [prj_doc.md](./tables/项目管理/prj_doc.md) |
| 6 | `prj_log` | 9 | `projectid`(项目id)、`logtype`(日志类型)、`documentid`(文档id)、`logcontent`(日志内容) 等共 9 个字段 | [prj_log.md](./tables/项目管理/prj_log.md) |
| 7 | `prj_members` | 3 | `id`(标识id)、`relateditemid`(项目id)、`userid`(成员id) | [prj_members.md](./tables/项目管理/prj_members.md) |
| 8 | `prj_modify` | 10 | `projectid`(项目id)、`type`(日志类型)、`fieldname`(字段名)、`modifydate`(修改日期) 等共 10 个字段 | [prj_modify.md](./tables/项目管理/prj_modify.md) |
| 9 | `prj_prjcardgroup` | 9 | `id`(标识id)、`prjtype`(项目类型)、`groupname`(分组名称)、`grouplabel`(分组标签) 等共 9 个字段 | [prj_prjcardgroup.md](./tables/项目管理/prj_prjcardgroup.md) |
| 10 | `prj_prjcardtab` | 9 | `id`(标识id)、`groupname`(标签页名称)、`grouplabel`(标签页标签)、`dsporder`(标签页顺序) 等共 9 个字段 | [prj_prjcardtab.md](./tables/项目管理/prj_prjcardtab.md) |
| 11 | `prj_prjwfactset` | 7 | `id`(标识id)、`mainid`(流程配置主表id)、`fieldid`(字段id)、`customervalue`(动作类型) 等共 7 个字段 | [prj_prjwfactset.md](./tables/项目管理/prj_prjwfactset.md) |
| 12 | `prj_prjwfconf` | 25 | `id`(标识id)、`wftype`(流程类型)、`wfid`(流程id)、`formid`(表单id) 等共 25 个字段 | [prj_prjwfconf.md](./tables/项目管理/prj_prjwfconf.md) |
| 13 | `prj_prjwffieldmap` | 5 | `id`(标识id)、`mainid`(流程配置主表id)、`fieldtype`(字段类型)、`fieldid`(字段id) 等共 5 个字段 | [prj_prjwffieldmap.md](./tables/项目管理/prj_prjwffieldmap.md) |
| 14 | `prj_projectinfo` | 76 | `tinyintfield3`(自定义选择字段3)、`tinyintfield4`(自定义选择字段4)、`tinyintfield5`(自定义选择字段5)、`subcompanyid1`(分部) 等共 76 个字段 | [prj_projectinfo.md](./tables/项目管理/prj_projectinfo.md) |
| 15 | `prj_projectstatus` | 7 | `id`(标识id)、`fullname`(状态标签)、`description`(名称)、`summary`(描述) 等共 7 个字段 | [prj_projectstatus.md](./tables/项目管理/prj_projectstatus.md) |
| 16 | `prj_projecttype` | 9 | `isprint`(甘特图是否打印)、`id`(标识id)、`fullname`(名称)、`description`(描述) 等共 9 个字段 | [prj_projecttype.md](./tables/项目管理/prj_projecttype.md) |
| 17 | `prj_request` | 8 | `id`(标识id)、`prjid`(项目id)、`taskid`(任务id)、`isactived`(是否活动任务) 等共 8 个字段 | [prj_request.md](./tables/项目管理/prj_request.md) |
| 18 | `prj_searchmould` | 24 | `id`(标识id)、`mouldname`(模板名称)、`userid`(用户id)、`prjid`(项目id) 等共 24 个字段 | [prj_searchmould.md](./tables/项目管理/prj_searchmould.md) |
| 19 | `prj_selectitem` | 12 | `fieldid`(字段id)、`isbill`(备用字段)、`selectvalue`(选项值)、`selectname`(选项显示名称) 等共 12 个字段 | [prj_selectitem.md](./tables/项目管理/prj_selectitem.md) |
| 20 | `prj_settings` | 26 | `id`(标识id)、`subcompanyid`(分部id)、`departmentid`(部门id)、`userid`(用户id) 等共 26 个字段 | [prj_settings.md](./tables/项目管理/prj_settings.md) |
| 21 | `prj_shareinfo` | 17 | `id`(标识id)、`relateditemid`(项目id)、`sharetype`(共享类型)、`seclevel`(安全级别(下限)) 等共 17 个字段 | [prj_shareinfo.md](./tables/项目管理/prj_shareinfo.md) |
| 22 | `prj_specialfield` | 7 | `id`(标识id)、`fieldid`(字段id)、`displayname`(显示名称)、`linkaddress`(链接地址) 等共 7 个字段 | [prj_specialfield.md](./tables/项目管理/prj_specialfield.md) |
| 23 | `prj_t_shareinfo` | 16 | `id`(标识id)、`relateditemid`(项目id)、`sharetype`(对象类型)、`seclevel`(安全级别(下限)) 等共 16 个字段 | [prj_t_shareinfo.md](./tables/项目管理/prj_t_shareinfo.md) |
| 24 | `prj_task_needdoc` | 8 | `id`(标识id)、`taskid`(任务id)、`templettaskid`(模板任务id)、`docmaincategory`(文档主目录) 等共 8 个字段 | [prj_task_needdoc.md](./tables/项目管理/prj_task_needdoc.md) |
| 25 | `prj_task_needwf` | 6 | `id`(标识id)、`taskid`(任务id)、`templettaskid`(模板任务id)、`workflowid`(流程id) 等共 6 个字段 | [prj_task_needwf.md](./tables/项目管理/prj_task_needwf.md) |
| 26 | `prj_task_referdoc` | 5 | `id`(标识id)、`taskid`(任务id)、`templettaskid`(模板任务id)、`docid`(文档id) 等共 5 个字段 | [prj_task_referdoc.md](./tables/项目管理/prj_task_referdoc.md) |
| 27 | `prj_taskinfo` | 35 | `stageid`(阶段id)、`prefinish`(前置任务)、`id`(标识id)、`prjid`(项目id) 等共 35 个字段 | [prj_taskinfo.md](./tables/项目管理/prj_taskinfo.md) |
| 28 | `prj_taskmodifylog` | 20 | `id`(标识id)、`projid`(项目id)、`taskid`(任务id)、`subject`(标题) 等共 20 个字段 | [prj_taskmodifylog.md](./tables/项目管理/prj_taskmodifylog.md) |
| 29 | `prj_taskprocess` | 41 | `stageid`(阶段id)、`stageorder`(阶段排序)、`parentids`(上级任务串)、`level_n`(层级) 等共 41 个字段 | [prj_taskprocess.md](./tables/项目管理/prj_taskprocess.md) |
| 30 | `prj_taskshareinfo` | 17 | `id`(标识id)、`relateditemid`(任务id)、`sharetype`(对象类型)、`seclevel`(安全级别(下限)) 等共 17 个字段 | [prj_taskshareinfo.md](./tables/项目管理/prj_taskshareinfo.md) |
| 31 | `prj_template` | 39 | `id`(标识id)、`isselected`(是否指定)、`templetname`(模板名称)、`templetdesc`(描述) 等共 39 个字段 | [prj_template.md](./tables/项目管理/prj_template.md) |
| 32 | `prj_templatetask` | 16 | `stageid`(阶段id)、`id`(标识id)、`templetid`(模板id)、`templettaskid`(任务id) 等共 16 个字段 | [prj_templatetask.md](./tables/项目管理/prj_templatetask.md) |
| 33 | `prj_templettask_needdoc` | 7 | `id`(标识id)、`templettaskid`(任务id)、`docmaincategory`(文档主目录id)、`docsubcategory`(文档子目录id) 等共 7 个字段 | [prj_templettask_needdoc.md](./tables/项目管理/prj_templettask_needdoc.md) |
| 34 | `prj_templettask_needwf` | 5 | `id`(标识id)、`templettaskid`(任务id)、`workflowid`(流程id)、`isnecessary`(是否必需) 等共 5 个字段 | [prj_templettask_needwf.md](./tables/项目管理/prj_templettask_needwf.md) |
| 35 | `prj_templettask_referdoc` | 4 | `id`(标识id)、`templettaskid`(任务id)、`docid`(文档id)、`istemplettask`(是否模板任务) | [prj_templettask_referdoc.md](./tables/项目管理/prj_templettask_referdoc.md) |
| 36 | `prj_tskcardgroup` | 8 | `id`(标识id)、`groupname`(分组名称)、`grouplabel`(分组标签)、`dsporder`(分组顺序) 等共 8 个字段 | [prj_tskcardgroup.md](./tables/项目管理/prj_tskcardgroup.md) |
| 37 | `prj_viewedlog` | 3 | `projid`(项目id)、`userid`(用户id)、`usertype`(用户类型) | [prj_viewedlog.md](./tables/项目管理/prj_viewedlog.md) |
| 38 | `prj_viewlog1` | 6 | `id`(标识)、`viewer`(访问者)、`viewdate`(访问日期)、`viewtime`(访问时间) 等共 6 个字段 | [prj_viewlog1.md](./tables/项目管理/prj_viewlog1.md) |
| 39 | `prj_worktype` | 6 | `id`(标识id)、`fullname`(名称)、`description`(描述)、`worktypecode`(编号) 等共 6 个字段 | [prj_worktype.md](./tables/项目管理/prj_worktype.md) |
| 40 | `prj_xchginfo_viewlog` | 7 | `id`(标识id)、`xchg_id`(相关交流id)、`sortid`(对象id)、`type_n`(类型) 等共 7 个字段 | [prj_xchginfo_viewlog.md](./tables/项目管理/prj_xchginfo_viewlog.md) |
| 41 | `prjdefinefield` | 23 | `qfws`(金额千分位)、`id`(标识id)、`billid`(备用字段)、`fieldname`(字段名) 等共 23 个字段 | [prjdefinefield.md](./tables/项目管理/prjdefinefield.md) |
| 42 | `prjtsk_selectitem` | 12 | `fieldid`(字段id)、`isbill`(备用字段)、`selectvalue`(选项值)、`selectname`(选项显示名称) 等共 12 个字段 | [prjtsk_selectitem.md](./tables/项目管理/prjtsk_selectitem.md) |
| 43 | `prjtsk_specialfield` | 7 | `id`(标识id)、`fieldid`(字段id)、`displayname`(显示名称)、`linkaddress`(链接地址) 等共 7 个字段 | [prjtsk_specialfield.md](./tables/项目管理/prjtsk_specialfield.md) |
| 44 | `prjtskdefinefield` | 22 | `qfws`(金额千分位)、`id`(标识id)、`billid`(备用字段)、`fieldname`(字段名) 等共 22 个字段 | [prjtskdefinefield.md](./tables/项目管理/prjtskdefinefield.md) |
| 45 | `projtemplatemaint` | 3 | `id`(标识id)、`isneedappr`(是否需要审批)、`wfid`(流程id) | [projtemplatemaint.md](./tables/项目管理/projtemplatemaint.md) |
| 46 | `task_log` | 8 | `projectid`(项目id)、`taskid`(任务id)、`logtype`(日志类型)、`submitdate`(提交日期) 等共 8 个字段 | [task_log.md](./tables/项目管理/task_log.md) |
| 47 | `task_modify` | 11 | `projectid`(项目id)、`taskid`(任务id)、`fieldname`(字段名称)、`modifydate`(修改日期) 等共 11 个字段 | [task_modify.md](./tables/项目管理/task_modify.md) |

### 即时通讯-EMESSAGE

> 本模块共收录 `46` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `fileclean` | 4 | `imagefileid`(附件id)、`comefrom`(附件来源)、`filecreatedate`(附件创建日期)、`filecreatetime`(附件创建时间) | [fileclean.md](./tables/即时通讯-EMESSAGE/fileclean.md) |
| 2 | `historymsg` | 13 | `fullamount`(客户端发的完整消息体)、`msgid`(消息id)、`id`(自增id)、`fromuserid`(消息发送方) 等共 13 个字段 | [historymsg.md](./tables/即时通讯-EMESSAGE/historymsg.md) |
| 3 | `historymsgrecently` | 13 | `id`(自增)、`fromuserid`(消息发送方)、`targetid`(会话id)、`targettype`(会话类型) 等共 13 个字段 | [historymsgrecently.md](./tables/即时通讯-EMESSAGE/historymsgrecently.md) |
| 4 | `social_allgroupinfos` | 5 | `id`(主键id)、`groupid`(群id)、`groupname`(群名称)、`createuserid`(创建人id) 等共 5 个字段 | [social_allgroupinfos.md](./tables/即时通讯-EMESSAGE/social_allgroupinfos.md) |
| 5 | `social_broadcast` | 7 | `id`(序列)、`plaintext`(广播内容)、`msgid`(消息id)、`fromuserid`(发起人) 等共 7 个字段 | [social_broadcast.md](./tables/即时通讯-EMESSAGE/social_broadcast.md) |
| 6 | `social_broadcastreceiver` | 3 | `id`(主键id)、`msgid`(广播的id)、`receiverid`(接收人id) | [social_broadcastreceiver.md](./tables/即时通讯-EMESSAGE/social_broadcastreceiver.md) |
| 7 | `social_filedownloadlog` | 5 | `id`(主键id)、`fileid`(文件id)、`userid`(上传人id)、`lastsavepath`(最后上传路径) 等共 5 个字段 | [social_filedownloadlog.md](./tables/即时通讯-EMESSAGE/social_filedownloadlog.md) |
| 8 | `social_historymsgright` | 4 | `id`(自增id)、`userid`(用户id)、`msgid`(消息id)、`isdel`(是否删除) | [social_historymsgright.md](./tables/即时通讯-EMESSAGE/social_historymsgright.md) |
| 9 | `social_imallowwindepart` | 8 | `id`(主键id)、`permissiontype`(允许类型)、`contents`(主要内容)、`seclevel`(开始安全级别) 等共 8 个字段 | [social_imallowwindepart.md](./tables/即时通讯-EMESSAGE/social_imallowwindepart.md) |
| 10 | `social_imattention` | 4 | `id`(主键id)、`userid`(用户id)、`targetid`(聊天对象)、`targettype`(聊天类型) | [social_imattention.md](./tables/即时通讯-EMESSAGE/social_imattention.md) |
| 11 | `social_imchatresource` | 10 | `id`(主键id)、`resourceid`(文档或者流程id)、`resourcename`(文档或者流程的标题)、`resourcedesc`(文档或者流程详细信息) 等共 10 个字段 | [social_imchatresource.md](./tables/即时通讯-EMESSAGE/social_imchatresource.md) |
| 12 | `social_imchatresourceshare` | 4 | `id`(主键id)、`userid`(用户id)、`resourceid`(资源id)、`resourcetype`(资源类型) | [social_imchatresourceshare.md](./tables/即时通讯-EMESSAGE/social_imchatresourceshare.md) |
| 13 | `social_imconversation` | 13 | `id`(主键id)、`userid`(最后发言的用户id)、`targetid`(会话id)、`targettype`(会话类型) 等共 13 个字段 | [social_imconversation.md](./tables/即时通讯-EMESSAGE/social_imconversation.md) |
| 14 | `social_imdelgrouplog` | 7 | `id`(主键id)、`userid`(用户id)、`name`(名称)、`delgroupid`(群组id) 等共 7 个字段 | [social_imdelgrouplog.md](./tables/即时通讯-EMESSAGE/social_imdelgrouplog.md) |
| 15 | `social_imfile` | 12 | `id`(主键id)、`userid`(用户id)、`targetid`(会话id)、`targettype`(会话类型) 等共 12 个字段 | [social_imfile.md](./tables/即时通讯-EMESSAGE/social_imfile.md) |
| 16 | `social_imfileshare` | 3 | `id`(deprecated弃用表)、`userid`(deprecated弃用表)、`fileid`(deprecated弃用表) | [social_imfileshare.md](./tables/即时通讯-EMESSAGE/social_imfileshare.md) |
| 17 | `social_imfilesharegroup` | 2 | `groupid`(Deprecated弃用表)、`fileid`(Deprecated弃用表) | [social_imfilesharegroup.md](./tables/即时通讯-EMESSAGE/social_imfilesharegroup.md) |
| 18 | `social_imfiletemp` | 12 | `id`(主键id)、`userid`(发送人id)、`targetid`(接收人id)、`targettype`(发送类型) 等共 12 个字段 | [social_imfiletemp.md](./tables/即时通讯-EMESSAGE/social_imfiletemp.md) |
| 19 | `social_imforbitlogin` | 8 | `id`(主键id)、`permissiontype`(禁止类型)、`contents`(主要内容)、`seclevel`(开始安全级别) 等共 8 个字段 | [social_imforbitlogin.md](./tables/即时通讯-EMESSAGE/social_imforbitlogin.md) |
| 20 | `social_imgroup` | 3 | `id`(主键id)、`name`(群组名称)、`createuserid`(所属者id) | [social_imgroup.md](./tables/即时通讯-EMESSAGE/social_imgroup.md) |
| 21 | `social_imgroup_rel` | 7 | `id`(主键id)、`rel_id`(群分组id)、`userid`(用户id)、`groupid`(群id) 等共 7 个字段 | [social_imgroup_rel.md](./tables/即时通讯-EMESSAGE/social_imgroup_rel.md) |
| 22 | `social_imhistorylog` | 2 | `id`(主键id)、`historyhour`(公有云获取消息成功时间戳) | [social_imhistorylog.md](./tables/即时通讯-EMESSAGE/social_imhistorylog.md) |
| 23 | `social_immsgcount` | 6 | `id`(主键id)、`msgid`(消息id)、`receiverid`(接收人id)、`status`(消息状态) 等共 6 个字段 | [social_immsgcount.md](./tables/即时通讯-EMESSAGE/social_immsgcount.md) |
| 24 | `social_immsgread` | 6 | `id`(主键id)、`msgid`(消息id)、`receiverid`(接受者id)、`status`(消息状态) 等共 6 个字段 | [social_immsgread.md](./tables/即时通讯-EMESSAGE/social_immsgread.md) |
| 25 | `social_immsgtag` | 4 | `id`(主键id)、`msgid`(消息id)、`tag`(消息标记)、`shareid`(必达id) | [social_immsgtag.md](./tables/即时通讯-EMESSAGE/social_immsgtag.md) |
| 26 | `social_imrecent` | 5 | `id`(主键id)、`userid`(用户id)、`targetid`(聊天对象)、`targettype`(聊天类型) 等共 5 个字段 | [social_imrecent.md](./tables/即时通讯-EMESSAGE/social_imrecent.md) |
| 27 | `social_imrecentconver` | 7 | `id`(主键id)、`userid`(用户id)、`targetid`(目标对话id)、`isdel`(暂时没有该字段) 等共 7 个字段 | [social_imrecentconver.md](./tables/即时通讯-EMESSAGE/social_imrecentconver.md) |
| 28 | `social_imsessionkey` | 7 | `id`(主键id)、`userid`(用户id)、`sessionkey`(session值)、`logindate`(登录时间戳) 等共 7 个字段 | [social_imsessionkey.md](./tables/即时通讯-EMESSAGE/social_imsessionkey.md) |
| 29 | `social_imsetting` | 5 | `id`(主键id)、`userid`(登陆用户id)、`targetid`(接收用户id)、`remindtype`(是否开启新消息通知) 等共 5 个字段 | [social_imsetting.md](./tables/即时通讯-EMESSAGE/social_imsetting.md) |
| 30 | `social_imsignatures` | 4 | `id`(主键id)、`userid`(用户id)、`signatures`(签名内容)、`signdate`(签名时间) | [social_imsignatures.md](./tables/即时通讯-EMESSAGE/social_imsignatures.md) |
| 31 | `social_imsysbroadcast` | 8 | `id`(ID)、`permissiontype`(权限种类)、`contents`(权限种类下的人员/部门/分部/角色的ID)、`seclevel`(安全级别下限) 等共 8 个字段 | [social_imsysbroadcast.md](./tables/即时通讯-EMESSAGE/social_imsysbroadcast.md) |
| 32 | `social_imuserright` | 8 | `id`(主键id)、`permissiontype`(允许类型)、`contents`(内容)、`seclevel`(开始安全级别) 等共 8 个字段 | [social_imuserright.md](./tables/即时通讯-EMESSAGE/social_imuserright.md) |
| 33 | `social_imuserrightmanager` | 9 | `id`(废弃)、`permissiontype`(废弃)、`contents`(废弃)、`seclevel`(废弃) 等共 9 个字段 | [social_imuserrightmanager.md](./tables/即时通讯-EMESSAGE/social_imuserrightmanager.md) |
| 34 | `social_imusersysconfig` | 5 | `id`(主键id)、`userid`(用户id)、`winconfig`(windows客户端设置)、`osxconfig`(macOs客户端配置) 等共 5 个字段 | [social_imusersysconfig.md](./tables/即时通讯-EMESSAGE/social_imusersysconfig.md) |
| 35 | `social_ipconfig` | 3 | `id`(主键id)、`oahost`(oaip)、`emhost`(message ip) | [social_ipconfig.md](./tables/即时通讯-EMESSAGE/social_ipconfig.md) |
| 36 | `social_networksegstr` | 8 | `id`(主键id)、`inceptipaddress`(起始ip)、`endipaddress`(结束ip)、`createrid`(创建者) 等共 8 个字段 | [social_networksegstr.md](./tables/即时通讯-EMESSAGE/social_networksegstr.md) |
| 37 | `social_pc_clientsettings` | 9 | `id`(主键id)、`keytitle`(配置项中文名)、`keyvalue`(配置项值)、`oaidentity`(暂时未知) 等共 9 个字段 | [social_pc_clientsettings.md](./tables/即时通讯-EMESSAGE/social_pc_clientsettings.md) |
| 38 | `social_pc_clientsettings_temp` | 9 | `id`(Deprecated弃用表)、`keytitle`(Deprecated弃用表)、`keyvalue`(Deprecated弃用表)、`oaidentity`(Deprecated弃用表) 等共 9 个字段 | [social_pc_clientsettings_temp.md](./tables/即时通讯-EMESSAGE/social_pc_clientsettings_temp.md) |
| 39 | `social_pc_urlicons` | 12 | `id`(主键id)、`labelindexid`(多语言标签id)、`labeltemp`(设置页面输入的按钮名称)、`icouri`(按钮图标地址) 等共 12 个字段 | [social_pc_urlicons.md](./tables/即时通讯-EMESSAGE/social_pc_urlicons.md) |
| 40 | `social_sysremind` | 7 | `id`(主键id)、`remindtype`(提醒类型)、`requestid`(提醒id)、`requesttitle`(提醒标题) 等共 7 个字段 | [social_sysremind.md](./tables/即时通讯-EMESSAGE/social_sysremind.md) |
| 41 | `social_sysremindreceiver` | 3 | `id`(主键id)、`remindid`(推送id)、`receiverid`(接收人) | [social_sysremindreceiver.md](./tables/即时通讯-EMESSAGE/social_sysremindreceiver.md) |
| 42 | `social_sysremindsetting` | 5 | `id`(主键id)、`remindtype`(提醒类型)、`userid`(用户id)、`ifon`(是否开启) 等共 5 个字段 | [social_sysremindsetting.md](./tables/即时通讯-EMESSAGE/social_sysremindsetting.md) |
| 43 | `social_sysremindtype` | 4 | `id`(主键id)、`remindtype`(提醒类型id)、`remindname`(内部提醒点击时打开的链接)、`surl`(内部提醒点击时打开的链接) | [social_sysremindtype.md](./tables/即时通讯-EMESSAGE/social_sysremindtype.md) |
| 44 | `social_translog` | 7 | `id`(主键id)、`roomname`(群组名)、`transfer`(迁移目的地)、`status`(迁移状态) 等共 7 个字段 | [social_translog.md](./tables/即时通讯-EMESSAGE/social_translog.md) |
| 45 | `social_withdrawmsg` | 4 | `id`(主键id)、`msgid`(消息id)、`userid`(发送人id)、`targetid`(接收人id) | [social_withdrawmsg.md](./tables/即时通讯-EMESSAGE/social_withdrawmsg.md) |
| 46 | `socialpcuserapps` | 4 | `id`(主键id)、`icoid`(应用图标id)、`userid`(用户id)、`showindex`(显示顺序) | [socialpcuserapps.md](./tables/即时通讯-EMESSAGE/socialpcuserapps.md) |

### E9新版考勤表结构

> 本模块共收录 `36` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `KQ_ATT_VACATION` | 14 | `id`(主键id)、`requestid`(requestid)、`dataid`(主表的话对应的id)、`detailid`(明细表的话对应的id) 等共 14 个字段 | [KQ_ATT_VACATION.md](./tables/E9新版考勤表结构/KQ_ATT_VACATION.md) |
| 2 | `KQ_HolidaySet` | 6 | `ID`(主键ID)、`groupId`(考勤组的ID)、`holidayDesc`(节假日描述信息)、`holidayDate`(节假日日期) 等共 6 个字段 | [KQ_HolidaySet.md](./tables/E9新版考勤表结构/KQ_HolidaySet.md) |
| 3 | `KQ_LeaveRules` | 12 | `ID`(主键ID)、`leaveName`(假期类型的名称)、`scopeType`(流程应用范围)、`scopeValue`(流程应用范围) 等共 12 个字段 | [KQ_LeaveRules.md](./tables/E9新版考勤表结构/KQ_LeaveRules.md) |
| 4 | `KQ_OvertimeUnit` | 4 | `ID`(主键ID)、`minimumUnit`(最小加班单位)、`hoursToDay`(日折算时长)、`isDelete`(是否已经删除) | [KQ_OvertimeUnit.md](./tables/E9新版考勤表结构/KQ_OvertimeUnit.md) |
| 5 | `KQ_leaveRulesDetail` | 16 | `ID`(主键ID)、`ruleId`(假期类型的ID)、`ruleName`(假期规则的名称)、`scopeType`(适用范围) 等共 16 个字段 | [KQ_leaveRulesDetail.md](./tables/E9新版考勤表结构/KQ_leaveRulesDetail.md) |
| 6 | `hrmschedulesign` | 18 | `wxsignaddress`(微信端签到地址)、`eb_deviceid`(设备号)、`eb_deviceid_change`(设备号)、`isimport`(是否是从其他系统同步过来) 等共 18 个字段 | [hrmschedulesign.md](./tables/E9新版考勤表结构/hrmschedulesign.md) |
| 7 | `hrmschedulesignimp` | 20 | `id`(ID)、`userid`(人员id)、`usertype`(人员类型)、`signtype`(打卡类型) 等共 20 个字段 | [hrmschedulesignimp.md](./tables/E9新版考勤表结构/hrmschedulesignimp.md) |
| 8 | `hrmschedulesignset` | 11 | `datasourceid`(来源id)、`importtype`(导入类型)、`tablename`(数据表名称)、`workcode`(编号) 等共 11 个字段 | [hrmschedulesignset.md](./tables/E9新版考勤表结构/hrmschedulesignset.md) |
| 9 | `kq_EntryToLeave` | 5 | `ID`(主键ID)、`leaveRulesId`(假期规则的ID)、`lowerLimit`(下限)、`upperLimit`(上限) 等共 5 个字段 | [kq_EntryToLeave.md](./tables/E9新版考勤表结构/kq_EntryToLeave.md) |
| 10 | `kq_ExitRules` | 7 | `ID`(主键ID)、`name`(规则名称)、`minimumUnit`(最小公出单位)、`proportion`(转换比例) 等共 7 个字段 | [kq_ExitRules.md](./tables/E9新版考勤表结构/kq_ExitRules.md) |
| 11 | `kq_MixedModeToLeave` | 8 | `ID`(主键)、`leaveRulesId`(假期规则的ID)、`lowerLimit`(工龄下限)、`upperLimit`(工龄上限) 等共 8 个字段 | [kq_MixedModeToLeave.md](./tables/E9新版考勤表结构/kq_MixedModeToLeave.md) |
| 12 | `kq_OvertimeRestTime` | 7 | `ID`(主键ID)、`ruleId`(加班规则的ID)、`dayType`(日期类型)、`startType`(开始时间的类型) 等共 7 个字段 | [kq_OvertimeRestTime.md](./tables/E9新版考勤表结构/kq_OvertimeRestTime.md) |
| 13 | `kq_OvertimeRules` | 4 | `ID`(主键ID)、`name`(加班规则的名称)、`groupIds`(考勤组的ID)、`isDelete`(是否已删除) | [kq_OvertimeRules.md](./tables/E9新版考勤表结构/kq_OvertimeRules.md) |
| 14 | `kq_OvertimeRulesDetail` | 11 | `Id`(主键ID)、`ruleId`(加班规则的ID)、`dayType`(日期类型)、`overtimeEnable`(是否允许加班) 等共 11 个字段 | [kq_OvertimeRulesDetail.md](./tables/E9新版考勤表结构/kq_OvertimeRulesDetail.md) |
| 15 | `kq_ReportShare` | 10 | `ID`(主键ID)、`reportName`(报表类型)、`resourceType`(对象类型)、`resourceId`(对象) 等共 10 个字段 | [kq_ReportShare.md](./tables/E9新版考勤表结构/kq_ReportShare.md) |
| 16 | `kq_ShiftManagement` | 13 | `id`(主键)、`serial`(班次名称)、`isresttimeopen`(排除休息时间是否开启 1表示开启)、`shiftonoffworkcount`(一天上下班次数) 等共 13 个字段 | [kq_ShiftManagement.md](./tables/E9新版考勤表结构/kq_ShiftManagement.md) |
| 17 | `kq_ShiftOnOffWorkSections` | 10 | `id`(主键)、`serialid`(外键 班次id 对应表ShiftManagement)、`across`(指定时段是否跨天 1表示跨天)、`beginmin`(当设置打卡时段时，预留字段) 等共 10 个字段 | [kq_ShiftOnOffWorkSections.md](./tables/E9新版考勤表结构/kq_ShiftOnOffWorkSections.md) |
| 18 | `kq_ShiftPersonalizedRule` | 16 | `id`(主键)、`serialid`(外键 班次id 对应表ShiftManagement)、`permitlateminutes`(允许迟到分钟数)、`seriouslateminutes`(严重迟到分钟数) 等共 16 个字段 | [kq_ShiftPersonalizedRule.md](./tables/E9新版考勤表结构/kq_ShiftPersonalizedRule.md) |
| 19 | `kq_ShiftPersonalizedRuleDetails` | 8 | `id`(主键)、`personalizedruleid`(外键 班次个性化设置id 对应表ShiftPersonalizedRule)、`enable`(规则是否启用 1表示启用)、`advancetime`(提前时长 存的是分钟数) 等共 8 个字段 | [kq_ShiftPersonalizedRuleDetails.md](./tables/E9新版考勤表结构/kq_ShiftPersonalizedRuleDetails.md) |
| 20 | `kq_ShiftRestTimeSections` | 6 | `id`(主键)、`serialid`(外键 对应ShiftManagement)、`resttype`(休息类型，开始(start)/结束(end))、`across`(指定时段是否跨天 1表示跨天) 等共 6 个字段 | [kq_ShiftRestTimeSections.md](./tables/E9新版考勤表结构/kq_ShiftRestTimeSections.md) |
| 21 | `kq_TravelRules` | 7 | `ID`(主键ID)、`name`(规则名称)、`minimumUnit`(最小出差单位)、`proportion`(换算比例) 等共 7 个字段 | [kq_TravelRules.md](./tables/E9新版考勤表结构/kq_TravelRules.md) |
| 22 | `kq_WorkingAgeToLeave` | 5 | `ID`(主键ID)、`leaveRulesId`(假期规则的ID)、`lowerLimit`(下限)、`upperLimit`(上限) 等共 5 个字段 | [kq_WorkingAgeToLeave.md](./tables/E9新版考勤表结构/kq_WorkingAgeToLeave.md) |
| 23 | `kq_balanceOfLeave` | 12 | `ID`(主键)、`leaveRulesId`(假期类型的ID)、`resourceId`(人员ID)、`belongYear`(所属年份) 等共 12 个字段 | [kq_balanceOfLeave.md](./tables/E9新版考勤表结构/kq_balanceOfLeave.md) |
| 24 | `kq_fixedschedulce` | 5 | `id`(主键ID)、`weekday`(星期几)、`serialid`(班次)、`groupid`(考勤组) 等共 5 个字段 | [kq_fixedschedulce.md](./tables/E9新版考勤表结构/kq_fixedschedulce.md) |
| 25 | `kq_flow_split_leave` | 31 | `id`(主键)、`requestid`(流程的requestid)、`workflowid`(流程的workflowid)、`dataid`(表单主表的id) 等共 31 个字段 | [kq_flow_split_leave.md](./tables/E9新版考勤表结构/kq_flow_split_leave.md) |
| 26 | `kq_format_detail` | 26 | `resourceid`(人员ID)、`kqdate`(考勤日期)、`groupid`(考勤组ID)、`serialid`(班次ID) 等共 26 个字段 | [kq_format_detail.md](./tables/E9新版考勤表结构/kq_format_detail.md) |
| 27 | `kq_format_pool` | 5 | `id`(主键ID)、`resourceid`(人员ID)、`kqdate`(考勤日期)、`status`(状态) 等共 5 个字段 | [kq_format_pool.md](./tables/E9新版考勤表结构/kq_format_pool.md) |
| 28 | `kq_format_total` | 26 | `resourceid`(人员ID)、`kqdate`(考勤日期)、`subcompanyid`(分部ID)、`departmentid`(部门ID) 等共 26 个字段 | [kq_format_total.md](./tables/E9新版考勤表结构/kq_format_total.md) |
| 29 | `kq_group` | 22 | `id`(主键ID)、`groupname`(组名称)、`subcompanyid`(所属分部)、`kqtype`(考勤组类型) 等共 22 个字段 | [kq_group.md](./tables/E9新版考勤表结构/kq_group.md) |
| 30 | `kq_groupmember` | 10 | `id`(主键ID)、`type`(成员类型)、`typevalue`(成员类型值)、`alllevel`(包含下级) 等共 10 个字段 | [kq_groupmember.md](./tables/E9新版考勤表结构/kq_groupmember.md) |
| 31 | `kq_location` | 6 | `id`(主键ID)、`locationname`(办公地点名称)、`longitude`(经度)、`latitude`(纬度) 等共 6 个字段 | [kq_location.md](./tables/E9新版考勤表结构/kq_location.md) |
| 32 | `kq_overtime_signtask` | 7 | `id`(主键)、`resourceid`(人员id)、`signdate`(打卡所属日期)、`signtime`(工作时间的，最后签退时间) 等共 7 个字段 | [kq_overtime_signtask.md](./tables/E9新版考勤表结构/kq_overtime_signtask.md) |
| 33 | `kq_report_check` | 2 | `id`(主键ID)、`check_date`(执行日期) | [kq_report_check.md](./tables/E9新版考勤表结构/kq_report_check.md) |
| 34 | `kq_report_field` | 12 | `id`(主键ID)、`fieldname`(字段名)、`fieldlabel`(字段显示名)、`width`(列宽) 等共 12 个字段 | [kq_report_field.md](./tables/E9新版考勤表结构/kq_report_field.md) |
| 35 | `kq_shiftschedule` | 6 | `id`(主键ID)、`kqdate`(考勤日期)、`serialid`(班次ID)、`resourceid`(人员ID) 等共 6 个字段 | [kq_shiftschedule.md](./tables/E9新版考勤表结构/kq_shiftschedule.md) |
| 36 | `kq_wifi` | 4 | `id`(主键ID)、`wifiname`(wifi名称)、`mac`(mac地址)、`groupid`(考勤组ID) | [kq_wifi.md](./tables/E9新版考勤表结构/kq_wifi.md) |

### 日程管理

> 本模块共收录 `33` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `WorkPlanList_Group` | 9 | `id`(主键)、`name`(名称)、`labelid`(名称的标签id)、`type`(类型) 等共 9 个字段 | [WorkPlanList_Group.md](./tables/日程管理/WorkPlanList_Group.md) |
| 2 | `WorkPlanWeekList_Group` | 6 | `id`(主键)、`name`(数据范围名称)、`groupvalue`(数据范围人员ids)、`workplantype`(日程类型ids) 等共 6 个字段 | [WorkPlanWeekList_Group.md](./tables/日程管理/WorkPlanWeekList_Group.md) |
| 3 | `WorkPlanWeekList_GroupLimit` | 9 | `id`(主键)、`groupid`(一周日程按钮数据范围id)、`objtype`(类型)、`objvalue`(id值) 等共 9 个字段 | [WorkPlanWeekList_GroupLimit.md](./tables/日程管理/WorkPlanWeekList_GroupLimit.md) |
| 4 | `overworkplan` | 4 | `id`(ID)、`workplanname`(结束日程名称)、`workplancolor`(结束日程颜色)、`wavailable`(是否显示) | [overworkplan.md](./tables/日程管理/overworkplan.md) |
| 5 | `workplan` | 72 | `id`(ID)、`deleted`(是否删除)、`urgentlevel`(紧急度)、`agentid`(代理人) 等共 72 个字段 | [workplan.md](./tables/日程管理/workplan.md) |
| 6 | `workplanReceiveScope` | 12 | `id`(id)、`baseId`(关联基本信息ID)、`receiveType`(接收人/创建人区分对象)、`scopeType`(范围类型) 等共 12 个字段 | [workplanReceiveScope.md](./tables/日程管理/workplanReceiveScope.md) |
| 7 | `workplanReceiveScopeSet` | 2 | `id`(id)、`receiveScope`(开启日程接收人范围控制) | [workplanReceiveScopeSet.md](./tables/日程管理/workplanReceiveScopeSet.md) |
| 8 | `workplanScopeBaseInfo` | 3 | `id`(id)、`name`(名称)、`description`(描述) | [workplanScopeBaseInfo.md](./tables/日程管理/workplanScopeBaseInfo.md) |
| 9 | `workplan_attention` | 5 | `id`(ID)、`userid`(用户id)、`usertype`(用户类型id)、`touserid`(接收人id) 等共 5 个字段 | [workplan_attention.md](./tables/日程管理/workplan_attention.md) |
| 10 | `workplan_disremindtime` | 3 | `userid`(用户id)、`usertype`(用户类型)、`remindtime`(提醒时间) | [workplan_disremindtime.md](./tables/日程管理/workplan_disremindtime.md) |
| 11 | `workplan_viewtype` | 2 | `userid`(人员id)、`viewtype`(查看类型) | [workplan_viewtype.md](./tables/日程管理/workplan_viewtype.md) |
| 12 | `workplan_weekviewtype` | 3 | `userid`(用户id)、`usertype`(用户类型)、`viewtype`(上一次查看样式类型) | [workplan_weekviewtype.md](./tables/日程管理/workplan_weekviewtype.md) |
| 13 | `workplanappdetail` | 3 | `workid`(工作计划id)、`resourceid`(创建人Id)、`appworkplanid`(mobile端日程id) | [workplanappdetail.md](./tables/日程管理/workplanappdetail.md) |
| 14 | `workplancreateshareset` | 16 | `companyvirtual`(维度)、`id`(id)、`planid`(共享日程类型)、`sharetype`(共享对象类型) 等共 16 个字段 | [workplancreateshareset.md](./tables/日程管理/workplancreateshareset.md) |
| 15 | `workplaneditlog` | 10 | `id`(主键)、`workplanid`(日程id)、`fieldname`(字段名称)、`oldvalue`(旧值) 等共 10 个字段 | [workplaneditlog.md](./tables/日程管理/workplaneditlog.md) |
| 16 | `workplanexchange` | 5 | `id`(主键)、`workplanid`(日程id)、`memberid`(人员id)、`exchangecount`(未读交流数) 等共 5 个字段 | [workplanexchange.md](./tables/日程管理/workplanexchange.md) |
| 17 | `workplangroup` | 8 | `id`(id)、`planname`(提醒内容)、`cycle`(提醒周期)、`plandate`(当前计划时间) 等共 8 个字段 | [workplangroup.md](./tables/日程管理/workplangroup.md) |
| 18 | `workplanmoduledeldate` | 4 | `moduleid`(日程id)、`creater`(用户id)、`creatertype`(用户类型id)、`deldate`(删除日程时间) | [workplanmoduledeldate.md](./tables/日程管理/workplanmoduledeldate.md) |
| 19 | `workplanmonitor` | 5 | `workplanmonitorid`(主键)、`hrmid`(日程创建人id)、`workplantypeid`(日程类型id)、`operatordate`(最后更新日期) 等共 5 个字段 | [workplanmonitor.md](./tables/日程管理/workplanmonitor.md) |
| 20 | `workplanrevision` | 6 | `id`(ID)、`planid`(计划id)、`operator`(操作者)、`operatetime`(操作时间) 等共 6 个字段 | [workplanrevision.md](./tables/日程管理/workplanrevision.md) |
| 21 | `workplanrevisionlog` | 54 | `id`(ID)、`groupid`(目标计划组id)、`type_n`(工作计划类型)、`name`(计划名称) 等共 54 个字段 | [workplanrevisionlog.md](./tables/日程管理/workplanrevisionlog.md) |
| 22 | `workplanset` | 11 | `viewtype`(未知)、`weekstartday`(日程日历，一览表 周开始第一天)、`id`(ID)、`timerangestart`(日历开始值) 等共 11 个字段 | [workplanset.md](./tables/日程管理/workplanset.md) |
| 23 | `workplansetup` | 3 | `userid`(用户id)、`reporttype`(报表类型)、`reccount`(报表每页记录数) | [workplansetup.md](./tables/日程管理/workplansetup.md) |
| 24 | `workplanshare` | 20 | `companyvirtual`(维度)、`id`(主键)、`workplanid`(日程id)、`sharetype`(共享对象类型) 等共 20 个字段 | [workplanshare.md](./tables/日程管理/workplanshare.md) |
| 25 | `workplansharechange` | 2 | `workid`(日程id)、`fromuser`(接收人) | [workplansharechange.md](./tables/日程管理/workplansharechange.md) |
| 26 | `workplansharedetail` | 13 | `workid`(日程id)、`userid`(人力资源共享对象)、`usertype`(用户类型)、`sharelevel`(共享等级) 等共 13 个字段 | [workplansharedetail.md](./tables/日程管理/workplansharedetail.md) |
| 27 | `workplansharedetail_old` | 10 | `workid`(日程id)、`userid`(人力资源共享对象)、`usertype`(用户类型)、`sharelevel`(共享等级) 等共 10 个字段 | [workplansharedetail_old.md](./tables/日程管理/workplansharedetail_old.md) |
| 28 | `workplanshareset` | 29 | `id`(ID)、`planid`(日程类型id)、`sharetype`(接收人对象类型)、`seclevel`(接收人对象安全级别) 等共 29 个字段 | [workplanshareset.md](./tables/日程管理/workplanshareset.md) |
| 29 | `workplantype` | 6 | `workplantypeid`(日程类型id)、`workplantypename`(日程类型名称)、`workplantypeattribute`(日程类型属性)、`workplantypecolor`(颜色) 等共 6 个字段 | [workplantype.md](./tables/日程管理/workplantype.md) |
| 30 | `workplanupdate` | 2 | `hasupdated`(旧版本更新状态)、`hasupdatednew`(更新状态) | [workplanupdate.md](./tables/日程管理/workplanupdate.md) |
| 31 | `workplanviewlog` | 8 | `id`(ID)、`workplanid`(日程id)、`viewtype`(查看状态)、`userid`(查看用户) 等共 8 个字段 | [workplanviewlog.md](./tables/日程管理/workplanviewlog.md) |
| 32 | `workplanvisitset` | 2 | `workplanvisitsetid`(主键)、`workplanreporttype`(被查看实体的类型) | [workplanvisitset.md](./tables/日程管理/workplanvisitset.md) |
| 33 | `workplanvisitsetdetail` | 8 | `workplanvisitsetdetailid`(主键)、`workplanreporttype`(被查看实体的类型)、`workplanreportcontentid`(被查看实体类型的标识id)、`workplanreportsec`(被访问者安全级别) 等共 8 个字段 | [workplanvisitsetdetail.md](./tables/日程管理/workplanvisitsetdetail.md) |

### 其他

> 本模块共收录 `32` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `bill_meeting` | 41 | `remindbeforestart`(是否开始前提醒)、`remindbeforeend`(是否结束前提醒)、`remindtimesbeforestart`(开始前时间)、`remindtimesbeforeend`(结束前时间) 等共 41 个字段 | [bill_meeting.md](./tables/其他/bill_meeting.md) |
| 2 | `clustersetting` | 7 | `id`(ID)、`ipaddress`(ip地址)、`httpaddress`(http访问地址)、`deployaddress`(部署地址) 等共 7 个字段 | [clustersetting.md](./tables/其他/clustersetting.md) |
| 3 | `customerkbversion` | 3 | `id`(ID)、`name`(KB版本号)、`sysversion`(系统版本号) | [customerkbversion.md](./tables/其他/customerkbversion.md) |
| 4 | `customersysversion` | 2 | `id`(ID)、`name`(系统版本号) | [customersysversion.md](./tables/其他/customersysversion.md) |
| 5 | `distribute_info` | 1 | `distributedatetime`(时间戳) | [distribute_info.md](./tables/其他/distribute_info.md) |
| 6 | `ecologypackageinfo` | 10 | `id`(ID)、`label`(补丁包编号)、`name`(补丁包全称)、`type`(补丁包类型) 等共 10 个字段 | [ecologypackageinfo.md](./tables/其他/ecologypackageinfo.md) |
| 7 | `formactionset` | 16 | `dmlsource`(DML数据来源)、`dmlsourcetype`(DML数据类型)、`dmlsourceorder`(DML数据来源序号)、`createdate`(创建日期) 等共 16 个字段 | [formactionset.md](./tables/其他/formactionset.md) |
| 8 | `kbqcdetail` | 6 | `id`(ID)、`qcnumber`(QC号)、`sysversion`(系统版本)、`kbversion`(KB版本) 等共 6 个字段 | [kbqcdetail.md](./tables/其他/kbqcdetail.md) |
| 9 | `ldapsetparam` | 3 | `id`(主键)、`ldapattr`(ldap里属性名称)、`userattr`(oa里人员字段名称) | [ldapsetparam.md](./tables/其他/ldapsetparam.md) |
| 10 | `mailcontent` | 2 | `mailid`(邮件id)、`mailcontent`(邮件内容) | [mailcontent.md](./tables/其他/mailcontent.md) |
| 11 | `maildeletefile` | 9 | `userid`(操作人id)、`optdate`(操作时间)、`deletedate`(删除时间)、`mailid`(所属邮件id) 等共 9 个字段 | [maildeletefile.md](./tables/其他/maildeletefile.md) |
| 12 | `mailsendapartlog` | 6 | `mailid`(邮件id)、`sendfrom`(发件人)、`sendto`(收件人)、`sendstatus`(发送结果，1成功，0失败) 等共 6 个字段 | [mailsendapartlog.md](./tables/其他/mailsendapartlog.md) |
| 13 | `mailworkremindlog` | 11 | `id`(主键)、`mwrl_uuid`(记录唯一uuid)、`result`(发送结果，1成功，0失败)、`createtime`(记录创建时间，run方法开始执行时间) 等共 11 个字段 | [mailworkremindlog.md](./tables/其他/mailworkremindlog.md) |
| 14 | `mode_deletelogdetail` | 6 | `id`(id)、`logid`(日志id)、`itemtype`(相关类型)、`itemid`(相关id) 等共 6 个字段 | [mode_deletelogdetail.md](./tables/其他/mode_deletelogdetail.md) |
| 15 | `mode_import_template` | 5 | `id`(id)、`modeid`(模块id)、`formid`(表单id)、`fieldid`(字段id) 等共 5 个字段 | [mode_import_template.md](./tables/其他/mode_import_template.md) |
| 16 | `mode_quicksearch_setting` | 6 | `id`(id)、`customid`(查询id)、`isquicksearch`(是否开启快捷查询)、`updatetor`(更新人) 等共 6 个字段 | [mode_quicksearch_setting.md](./tables/其他/mode_quicksearch_setting.md) |
| 17 | `ofs_log` | 25 | `logid`(自增长序列)、`sysid`(异构系统id)、`datatype`(数据类型)、`opertype`(操作类型) 等共 25 个字段 | [ofs_log.md](./tables/其他/ofs_log.md) |
| 18 | `sensitive_logs` | 9 | `id`(ID)、`module`(模块)、`path`(请求路径)、`doccontent`(拦截内容) 等共 9 个字段 | [sensitive_logs.md](./tables/其他/sensitive_logs.md) |
| 19 | `sensitive_settings` | 4 | `id`(ID)、`status`(敏感词启用开关)、`handleway`(敏感词处理方式)、`remindusers`(流程提醒者) | [sensitive_settings.md](./tables/其他/sensitive_settings.md) |
| 20 | `sensitive_words` | 2 | `id`(ID)、`word`(敏感词) | [sensitive_words.md](./tables/其他/sensitive_words.md) |
| 21 | `systemrightdetail` | 4 | `id`(ID)、`rightdetailname`(权限详细名称)、`rightdetail`(权限详细描述)、`rightid`(权限id) | [systemrightdetail.md](./tables/其他/systemrightdetail.md) |
| 22 | `systemrightgroups` | 4 | `id`(ID)、`rightgroupmark`(权限组标识)、`rightgroupname`(权限组名称)、`rightgroupremark`(权限组详述) | [systemrightgroups.md](./tables/其他/systemrightgroups.md) |
| 23 | `systemrightroles` | 4 | `id`(ID)、`rightid`(权限ID)、`roleid`(角色ID)、`rolelevel`(角色级别) | [systemrightroles.md](./tables/其他/systemrightroles.md) |
| 24 | `systemrights` | 4 | `id`(ID)、`rightdesc`(权限描述)、`righttype`(权限类型)、`detachable`(可分权权限) | [systemrights.md](./tables/其他/systemrights.md) |
| 25 | `systemrightslanguage` | 4 | `id`(ID)、`languageid`(语言id)、`rightname`(权限名称)、`rightdesc`(权限描述) | [systemrightslanguage.md](./tables/其他/systemrightslanguage.md) |
| 26 | `systemrighttogroup` | 3 | `id`(ID)、`groupid`(组ID)、`rightid`(权限ID) | [systemrighttogroup.md](./tables/其他/systemrighttogroup.md) |
| 27 | `temphrmgroupmembers` | 4 | `groupid`(组ID)、`userid`(用户ID)、`usertype`(用户类型)、`dsporder`(显示顺序) | [temphrmgroupmembers.md](./tables/其他/temphrmgroupmembers.md) |
| 28 | `templetecheck_matchresult` | 5 | `id`(ID)、`filepath`(文件路径)、`workflowname`(流程名称)、`nodename`(节点名称) 等共 5 个字段 | [templetecheck_matchresult.md](./tables/其他/templetecheck_matchresult.md) |
| 29 | `webmaillist` | 4 | `id`(主键)、`name`(作用不详)、`maildesc`(作用不详)、`userlist`(作用不详) | [webmaillist.md](./tables/其他/webmaillist.md) |
| 30 | `wf_browser_config` | 8 | `type`(浏览框类型)、`clazz`(浏览框实现类)、`description`(描述)、`linkurl`(连接URL) 等共 8 个字段 | [wf_browser_config.md](./tables/其他/wf_browser_config.md) |
| 31 | `wf_flowtime_reporttask_log` | 7 | `id`(ID)、`taskstatus`(耗时计算任务状态)、`startdate`(任务开始时间)、`enddate`(任务结束日期) 等共 7 个字段 | [wf_flowtime_reporttask_log.md](./tables/其他/wf_flowtime_reporttask_log.md) |
| 32 | `workplan_remind_type` | 9 | `id`(id)、`name`(提醒方式中文名)、`label`(提醒方式标签id,支持国际化)、`hastitle`(是否有标题) 等共 9 个字段 | [workplan_remind_type.md](./tables/其他/workplan_remind_type.md) |

### 邮件模块

> 本模块共收录 `32` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `docmailmould` | 8 | `id`(邮件模板id)、`mouldname`(文档模板描述)、`isdefault`(是否是默认)、`mouldtext`(文档模板html) 等共 8 个字段 | [docmailmould.md](./tables/邮件模块/docmailmould.md) |
| 2 | `email_label` | 6 | `id`(ID)、`accountid`(该标签归属用户id)、`name`(标签名称)、`color`(标签颜色) 等共 6 个字段 | [email_label.md](./tables/邮件模块/email_label.md) |
| 3 | `email_label_detail` | 3 | `id`(ID)、`labelid`(标签id)、`mailid`(邮件id) | [email_label_detail.md](./tables/邮件模块/email_label_detail.md) |
| 4 | `emailguide` | 2 | `id`(ID)、`userid`(已使用过向导的用户id) | [emailguide.md](./tables/邮件模块/emailguide.md) |
| 5 | `groupandcontact` | 3 | `id`(ID)、`groupid`(分组id)、`contactid`(联系人id) | [groupandcontact.md](./tables/邮件模块/groupandcontact.md) |
| 6 | `mailaccount` | 24 | `isstarttls`(是否使用TLS方式)、`id`(ID)、`userid`(用户id)、`accountname`(帐户名称) 等共 24 个字段 | [mailaccount.md](./tables/邮件模块/mailaccount.md) |
| 7 | `mailaccountreceivedinfo` | 3 | `accountid`(帐户id)、`receiveddatetime`(接收时间)、`sendfrom`(发送时间) | [mailaccountreceivedinfo.md](./tables/邮件模块/mailaccountreceivedinfo.md) |
| 8 | `mailautorespond` | 5 | `id`(id)、`userid`(人员id)、`isauto`(是否开启)、`iscontactreply`(仅对联系人中的邮件地址进行回复) 等共 5 个字段 | [mailautorespond.md](./tables/邮件模块/mailautorespond.md) |
| 9 | `mailblacklist` | 4 | `id`(id)、`userid`(人员id)、`name`(邮箱地址)、`postfix`(邮箱域名) | [mailblacklist.md](./tables/邮件模块/mailblacklist.md) |
| 10 | `mailconfigureinfo` | 17 | `innermail`(是否使用内部邮件)、`outtermail`(是否使用外部邮件)、`filepath`(邮件附件上传目录)、`totalattachmentsize`(邮件附件上传大小) 等共 17 个字段 | [mailconfigureinfo.md](./tables/邮件模块/mailconfigureinfo.md) |
| 11 | `mailelectronsign` | 14 | `id`(id)、`signid`(签名id)、`name`(签名名称)、`email`(邮件地址) 等共 14 个字段 | [mailelectronsign.md](./tables/邮件模块/mailelectronsign.md) |
| 12 | `mailerrorhint` | 6 | `id`(主键id)、`errorname`(错误异常名称)、`errorhint`(错误提示)、`solution`(解决方案) 等共 6 个字段 | [mailerrorhint.md](./tables/邮件模块/mailerrorhint.md) |
| 13 | `mailinboxfolder` | 6 | `id`(ID)、`webfxtreeid`(树节点id)、`userid`(用户id)、`foldername`(文件夹名称) 等共 6 个字段 | [mailinboxfolder.md](./tables/邮件模块/mailinboxfolder.md) |
| 14 | `maillog` | 6 | `id`(id)、`submiter`(操作者)、`submitdate`(操作时间)、`logtype`(操作类型) 等共 6 个字段 | [maillog.md](./tables/邮件模块/maillog.md) |
| 15 | `mailpassword` | 3 | `resourceid`(用户id)、`resourcemail`(用户邮件地址)、`password`(用户邮件密码) | [mailpassword.md](./tables/邮件模块/mailpassword.md) |
| 16 | `mailreceiveremind` | 5 | `id`(id)、`name`(提醒名称)、`enable`(是否启用)、`content`(提醒内容) 等共 5 个字段 | [mailreceiveremind.md](./tables/邮件模块/mailreceiveremind.md) |
| 17 | `mailresource` | 61 | `tosubcomids`(收件人-分部)、`ccsubcomids`(抄送人-分部)、`bccsubcomids`(密送人-分部)、`togroupids`(收件人-群组) 等共 61 个字段 | [mailresource.md](./tables/邮件模块/mailresource.md) |
| 18 | `mailresourcefile` | 20 | `mrf_uuid`(附件唯一标志uuid)、`htmlcode`(html预览方式imagefileid)、`pdfcode`(pdf预览方式imagefileid)、`storagestatus`(阿里OSS存储状态) 等共 20 个字段 | [mailresourcefile.md](./tables/邮件模块/mailresourcefile.md) |
| 19 | `mailresourcefilebackup` | 2 | `id`(id)、`mailresourcefileid`(附件id) | [mailresourcefilebackup.md](./tables/邮件模块/mailresourcefilebackup.md) |
| 20 | `mailrule` | 9 | `accounttype`(应用账户)、`mailtype`(应用账户类型)、`mailaccountid`(应用帐户id)、`id`(ID) 等共 9 个字段 | [mailrule.md](./tables/邮件模块/mailrule.md) |
| 21 | `mailruleaction` | 8 | `id`(ID)、`ruleid`(邮件规则id)、`asource`(执行对象)、`atargetfolderid`(执行对象(文件夹id)) 等共 8 个字段 | [mailruleaction.md](./tables/邮件模块/mailruleaction.md) |
| 22 | `mailrulecondition` | 7 | `operator`(运行符)、`ctargetpriority`(比较对象(优先级别))、`id`(ID)、`ruleid`(邮件规则id) 等共 7 个字段 | [mailrulecondition.md](./tables/邮件模块/mailrulecondition.md) |
| 23 | `mailsendmain` | 11 | `id`(ID)、`sendfrom`(发件人地址)、`sendcc`(抄送地址)、`sendbcc`(密送地址) 等共 11 个字段 | [mailsendmain.md](./tables/邮件模块/mailsendmain.md) |
| 24 | `mailsendrecord` | 6 | `id`(表mailsendmain id)、`sendto`(收件人地址)、`subject`(邮件标题)、`body`(邮件内容) 等共 6 个字段 | [mailsendrecord.md](./tables/邮件模块/mailsendrecord.md) |
| 25 | `mailsetting` | 7 | `isshowcontentsummary`(是否展示内容摘要)、`id`(ID)、`userid`(用户id)、`mainid`(主目录id) 等共 7 个字段 | [mailsetting.md](./tables/邮件模块/mailsetting.md) |
| 26 | `mailsign` | 7 | `id`(ID)、`userid`(人员id)、`signname`(签名名称)、`signdesc`(签名描述) 等共 7 个字段 | [mailsign.md](./tables/邮件模块/mailsign.md) |
| 27 | `mailtemplate` | 7 | `id`(ID)、`userid`(用户id)、`templatename`(模板名称)、`templatedescription`(模板描述) 等共 7 个字段 | [mailtemplate.md](./tables/邮件模块/mailtemplate.md) |
| 28 | `mailtemplateuser` | 3 | `userid`(用户id)、`templateid`(模板id)、`templatetype`(模板类型) | [mailtemplateuser.md](./tables/邮件模块/mailtemplateuser.md) |
| 29 | `mailuser` | 2 | `mailgroupid`(邮件组id)、`resourceid`(人力资源id) | [mailuser.md](./tables/邮件模块/mailuser.md) |
| 30 | `mailuseraddress` | 19 | `mailgroupid`(邮件组)、`mailaddress`(邮件地址)、`maildesc`(邮件描述)、`id`(id) 等共 19 个字段 | [mailuseraddress.md](./tables/邮件模块/mailuseraddress.md) |
| 31 | `mailusergroup` | 7 | `mailgroupid`(邮件组id)、`mailgroupname`(邮件组名称)、`operatedesc`(描述)、`createrid`(创建人) 等共 7 个字段 | [mailusergroup.md](./tables/邮件模块/mailusergroup.md) |
| 32 | `webmail_domain` | 14 | `domain_id`(邮件服务器id)、`domain`(邮件服务器域名)、`pop_server`(收信服务器地址)、`smtp_server`(发信服务器地址) 等共 14 个字段 | [webmail_domain.md](./tables/邮件模块/webmail_domain.md) |

### 移动引擎

> 本模块共收录 `29` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `appfieldui` | 9 | `id`(主键)、`formid`(表单id)、`appid`(应用id)、`fieldid`(字段id) 等共 9 个字段 | [appfieldui.md](./tables/移动引擎/appfieldui.md) |
| 2 | `appformui对应表` | 14 | `id`(主键)、`formid`(表单id)、`uicontent`(ui内容)、`uitype`(ui类型) 等共 14 个字段 | [appformui对应表.md](./tables/移动引擎/appformui对应表.md) |
| 3 | `apphomepage` | 15 | `color`(颜色)、`pid`(分组ID)、`prew_img`(预览图片)、`version`(版本) 等共 15 个字段 | [apphomepage.md](./tables/移动引擎/apphomepage.md) |
| 4 | `apphomepage_model` | 6 | `isdefault`(是否默认)、`layoutid`(布局ID)、`apphomepageid`(页面id)、`modelid`(模块id) 等共 6 个字段 | [apphomepage_model.md](./tables/移动引擎/apphomepage_model.md) |
| 5 | `apphomepagefolder` | 5 | `id`(主键)、`foldername`(文件夹名称)、`orderid`(显示排序)、`pid`(父级ID) 等共 5 个字段 | [apphomepagefolder.md](./tables/移动引擎/apphomepagefolder.md) |
| 6 | `mobileactionlog` | 11 | `id`(主键)、`node`(节点)、`userid`(用户ID)、`createdate`(创建日期) 等共 11 个字段 | [mobileactionlog.md](./tables/移动引擎/mobileactionlog.md) |
| 7 | `mobileappaccesslog` | 9 | `id`(主键)、`node`(节点)、`userid`(用户ID)、`createdate`(创建日期) 等共 9 个字段 | [mobileappaccesslog.md](./tables/移动引擎/mobileappaccesslog.md) |
| 8 | `mobileappbaseinfo` | 17 | `subcompanyid`(分部ID)、`createdate`(创建日期)、`modifydate`(修改日期)、`creator`(创建人ID) 等共 17 个字段 | [mobileappbaseinfo.md](./tables/移动引擎/mobileappbaseinfo.md) |
| 9 | `mobileappbrowserfieldsinfo` | 4 | `appid`(应用ID)、`browsername`(浏览框名称)、`fields`(字段)、`id`(主键) | [mobileappbrowserfieldsinfo.md](./tables/移动引擎/mobileappbrowserfieldsinfo.md) |
| 10 | `mobileappcategory` | 5 | `id`(主键)、`text`(文本)、`showorder`(显示顺序)、`creator`(创建人) 等共 5 个字段 | [mobileappcategory.md](./tables/移动引擎/mobileappcategory.md) |
| 11 | `mobileappcomment` | 7 | `id`(主键)、`appid`(应用ID)、`userid`(用户ID)、`score`(分数) 等共 7 个字段 | [mobileappcomment.md](./tables/移动引擎/mobileappcomment.md) |
| 12 | `mobileappmodelinfo` | 7 | `id`(主键)、`appid`(所属应用id)、`formid`(表单id)、`isdelete`(是否删除) 等共 7 个字段 | [mobileappmodelinfo.md](./tables/移动引擎/mobileappmodelinfo.md) |
| 13 | `mobileappnewversionviewlog` | 4 | `id`(主键)、`appid`(应用ID)、`userid`(用户ID)、`logdate`(日志产生日期) | [mobileappnewversionviewlog.md](./tables/移动引擎/mobileappnewversionviewlog.md) |
| 14 | `mobileappversion` | 6 | `id`(主键)、`appid`(应用ID)、`serial`(版本标识)、`descriptions`(描述) 等共 6 个字段 | [mobileappversion.md](./tables/移动引擎/mobileappversion.md) |
| 15 | `mobiledevice` | 6 | `id`(主键列)、`devicename`(设备名称)、`picpath`(图片路径)、`width`(宽度) 等共 6 个字段 | [mobiledevice.md](./tables/移动引擎/mobiledevice.md) |
| 16 | `mobileextendcomponent` | 5 | `id`(主键)、`objid`(所属自定义页面id)、`objtype`(所属自定义页面类型)、`mectype`(插件类型) 等共 5 个字段 | [mobileextendcomponent.md](./tables/移动引擎/mobileextendcomponent.md) |
| 17 | `mobilelognode` | 5 | `refnode`(引用节点)、`id`(结点标识)、`name`(名称)、`enabled`(是否启用) 等共 5 个字段 | [mobilelognode.md](./tables/移动引擎/mobilelognode.md) |
| 18 | `mobilemode_api` | 20 | `type`(类型)、`is_sys`(是否系统接口)、`front_request_body_enabled`(启用请求Body)、`front_request_body_desc`(请求Body内容示例) 等共 20 个字段 | [mobilemode_api.md](./tables/移动引擎/mobilemode_api.md) |
| 19 | `mobilemode_api_error_code` | 6 | `id`(主键)、`code`(错误码)、`message`(错误消息)、`remark`(备注) 等共 6 个字段 | [mobilemode_api_error_code.md](./tables/移动引擎/mobilemode_api_error_code.md) |
| 20 | `mobilemode_api_front_param` | 8 | `id`(主键)、`name`(名称)、`type`(类型)、`required`(是否必填) 等共 8 个字段 | [mobilemode_api_front_param.md](./tables/移动引擎/mobilemode_api_front_param.md) |
| 21 | `mobilemode_api_group` | 7 | `id`(主键)、`name`(名称)、`remark`(备注)、`creator`(创建人) 等共 7 个字段 | [mobilemode_api_group.md](./tables/移动引擎/mobilemode_api_group.md) |
| 22 | `mobilemode_api_range` | 5 | `id`(主键)、`type`(类型)、`value`(值)、`api_id`(接口ID) 等共 5 个字段 | [mobilemode_api_range.md](./tables/移动引擎/mobilemode_api_range.md) |
| 23 | `mobilemode_api_result_define` | 6 | `id`(主键)、`name`(名称)、`remark`(备注)、`type`(类型) 等共 6 个字段 | [mobilemode_api_result_define.md](./tables/移动引擎/mobilemode_api_result_define.md) |
| 24 | `mobilemode_api_server_param` | 6 | `id`(主键)、`name`(名称)、`position`(参数位置)、`front_parameter_id`(对应前端参数) 等共 6 个字段 | [mobilemode_api_server_param.md](./tables/移动引擎/mobilemode_api_server_param.md) |
| 25 | `mobilemode_api_system_param` | 6 | `id`(主键)、`name`(名称)、`position`(参数位置)、`system_variable`(系统变量) 等共 6 个字段 | [mobilemode_api_system_param.md](./tables/移动引擎/mobilemode_api_system_param.md) |
| 26 | `mobilemode_plugin_impexp` | 6 | `id`(主键)、`plugin`(插件)、`type`(类型)、`version`(版本) 等共 6 个字段 | [mobilemode_plugin_impexp.md](./tables/移动引擎/mobilemode_plugin_impexp.md) |
| 27 | `mobilemodeusertoken` | 3 | `id`(主键)、`userid`(用户id)、`token`(令牌) | [mobilemodeusertoken.md](./tables/移动引擎/mobilemodeusertoken.md) |
| 28 | `mobilepageaccesslog` | 11 | `id`(主键)、`node`(节点)、`userid`(用户ID)、`createdate`(创建日期) 等共 11 个字段 | [mobilepageaccesslog.md](./tables/移动引擎/mobilepageaccesslog.md) |
| 29 | `mobileportalmeta` | 4 | `id`(主键)、`userid`(用户ID)、`appid`(应用ID)、`createdate`(创建日期) | [mobileportalmeta.md](./tables/移动引擎/mobileportalmeta.md) |

### 资产管理

> 本模块共收录 `27` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `cpt_browdef` | 8 | `fieldid`(字段id)、`fieldkind`(字段类型)、`iscondition`(作为查询条件)、`iscondition_type`(条件类型) 等共 8 个字段 | [cpt_browdef.md](./tables/资产管理/cpt_browdef.md) |
| 2 | `cpt_cptcardgroup` | 8 | `id`(标识id)、`groupname`(分组名称)、`grouplabel`(分组标签)、`dsporder`(分组顺序) 等共 8 个字段 | [cpt_cptcardgroup.md](./tables/资产管理/cpt_cptcardgroup.md) |
| 3 | `cpt_cptcardtab` | 9 | `issystem`(是否是系统标签页)、`linkurl`(标签页链接地址)、`id`(标识id)、`groupname`(标签页名称) 等共 9 个字段 | [cpt_cptcardtab.md](./tables/资产管理/cpt_cptcardtab.md) |
| 4 | `cpt_cptwfconf` | 27 | `cptno`(资产编号)、`zclx`(资产类型)、`rkrq`(入库日期)、`ssbm`(所属部门) 等共 27 个字段 | [cpt_cptwfconf.md](./tables/资产管理/cpt_cptwfconf.md) |
| 5 | `cpt_oauth` | 3 | `id`(标识id)、`auth_flag_`(临时授权类型)、`auth_clazz_`(临时授权实现类) | [cpt_oauth.md](./tables/资产管理/cpt_oauth.md) |
| 6 | `cpt_selectitem` | 13 | `fieldid`(字段id)、`isbill`(备用字段)、`selectvalue`(选项值)、`selectname`(选项名称) 等共 13 个字段 | [cpt_selectitem.md](./tables/资产管理/cpt_selectitem.md) |
| 7 | `cpt_specialfield` | 7 | `id`(标识id)、`fieldid`(字段id)、`displayname`(显示名称)、`linkaddress`(链接url) 等共 7 个字段 | [cpt_specialfield.md](./tables/资产管理/cpt_specialfield.md) |
| 8 | `cptassortmentshare` | 16 | `id`(标识id)、`assortmentid`(资产组id)、`sharetype`(对象类型)、`seclevel`(安全级别) 等共 16 个字段 | [cptassortmentshare.md](./tables/资产管理/cptassortmentshare.md) |
| 9 | `cptborrowbuffer` | 7 | `id`(标识id)、`cptid`(资产id)、`usedate`(借用日期)、`deptid`(部门) 等共 7 个字段 | [cptborrowbuffer.md](./tables/资产管理/cptborrowbuffer.md) |
| 10 | `cptcapital` | 68 | `id`(标识id)、`mark`(编号)、`name`(名称)、`barcode`(条形码) 等共 68 个字段 | [cptcapital.md](./tables/资产管理/cptcapital.md) |
| 11 | `cptcapitalassortment` | 9 | `id`(标识id)、`assortmentname`(名称)、`assortmentremark`(备注)、`supassortmentid`(直接上级资产组id) 等共 9 个字段 | [cptcapitalassortment.md](./tables/资产管理/cptcapitalassortment.md) |
| 12 | `cptcapitalcodeseq` | 13 | `id`(标识id)、`sequenceid`(流水号)、`subcompanyid`(分部)、`departmentid`(部门) 等共 13 个字段 | [cptcapitalcodeseq.md](./tables/资产管理/cptcapitalcodeseq.md) |
| 13 | `cptcapitalcodeseq1` | 13 | `id`(标识id)、`sequenceid`(流水号)、`subcompanyid`(分部)、`departmentid`(部门) 等共 13 个字段 | [cptcapitalcodeseq1.md](./tables/资产管理/cptcapitalcodeseq1.md) |
| 14 | `cptcapitalmodifyfield` | 2 | `field`(字段id)、`name`(字段名称(标签)) | [cptcapitalmodifyfield.md](./tables/资产管理/cptcapitalmodifyfield.md) |
| 15 | `cptcapitalshareinfo` | 18 | `id`(标识id)、`relateditemid`(资产id)、`sharetype`(共享类型)、`seclevel`(安全级别) 等共 18 个字段 | [cptcapitalshareinfo.md](./tables/资产管理/cptcapitalshareinfo.md) |
| 16 | `cptcapitalstate` | 4 | `id`(标识id)、`name`(名字)、`description`(备注)、`issystem`(是否系统状态) | [cptcapitalstate.md](./tables/资产管理/cptcapitalstate.md) |
| 17 | `cptcapitaltype` | 4 | `id`(标识id)、`name`(名称)、`description`(描述)、`typecode`(编号) | [cptcapitaltype.md](./tables/资产管理/cptcapitaltype.md) |
| 18 | `cptcode` | 10 | `id`(标识id)、`isuse`(编码方式)、`subcompanyflow`(分部流水)、`departmentflow`(部门流水) 等共 10 个字段 | [cptcode.md](./tables/资产管理/cptcode.md) |
| 19 | `cptcode1` | 10 | `id`(标识id)、`isuse`(编码方式)、`subcompanyflow`(分部流水)、`departmentflow`(部门流水) 等共 10 个字段 | [cptcode1.md](./tables/资产管理/cptcode1.md) |
| 20 | `cptcodeset` | 6 | `id`(标识id)、`codeid`(资产编码配置id)、`showname`(显示名)、`showtype`(显示类型) 等共 6 个字段 | [cptcodeset.md](./tables/资产管理/cptcodeset.md) |
| 21 | `cptcodeset1` | 6 | `id`(标识id)、`codeid`(资产资料编码配置id)、`showname`(显示名)、`showtype`(显示类型) 等共 6 个字段 | [cptcodeset1.md](./tables/资产管理/cptcodeset1.md) |
| 22 | `cptdefinefield` | 21 | `id`(标识id)、`billid`(备用字段)、`fieldname`(字段名)、`fieldlabel`(字段标签) 等共 21 个字段 | [cptdefinefield.md](./tables/资产管理/cptdefinefield.md) |
| 23 | `cptsearchdefinition` | 8 | `id`(标识id)、`fieldname`(字段名)、`isconditionstitle`(是否作为字段列或查询条件)、`istitle`(是否作为显示列) 等共 8 个字段 | [cptsearchdefinition.md](./tables/资产管理/cptsearchdefinition.md) |
| 24 | `cptsearchmould` | 120 | `blongsubcompany`(所属部门)、`alertnum`(告警数量)、`datafield44`(自定义日期4)、`datafield5`(自定义日期5) 等共 120 个字段 | [cptsearchmould.md](./tables/资产管理/cptsearchmould.md) |
| 25 | `cptstockindetail` | 12 | `id`(标识id)、`cptstockinid`(资产入库主表id)、`cpttype`(资产资料)、`plannumber`(入库数量) 等共 12 个字段 | [cptstockindetail.md](./tables/资产管理/cptstockindetail.md) |
| 26 | `cptstockinmain` | 8 | `id`(标识id)、`invoice`(发票号)、`buyerid`(申请人)、`supplierid`(供应商) 等共 8 个字段 | [cptstockinmain.md](./tables/资产管理/cptstockinmain.md) |
| 27 | `cptuselog` | 15 | `id`(标识id)、`capitalid`(资产id)、`usedate`(流转日期)、`usedeptid`(流转部门) 等共 15 个字段 | [cptuselog.md](./tables/资产管理/cptuselog.md) |

### 工作微博

> 本模块共收录 `26` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `blog_app` | 6 | `id`(主键id)、`name`(应用名称)、`isactive`(是否激活)、`apptype`(应用类型) 等共 6 个字段 | [blog_app.md](./tables/工作微博/blog_app.md) |
| 2 | `blog_appdatas` | 7 | `id`(主键id)、`userid`(人员id)、`workdate`(工作日)、`createdate`(创建日期) 等共 7 个字段 | [blog_appdatas.md](./tables/工作微博/blog_appdatas.md) |
| 3 | `blog_appitem` | 5 | `id`(主键id)、`itemname`(应用项名称)、`value`(应用项值)、`type`(类型) 等共 5 个字段 | [blog_appitem.md](./tables/工作微博/blog_appitem.md) |
| 4 | `blog_at` | 2 | `discussid`(微博id)、`userid`(人员id) | [blog_at.md](./tables/工作微博/blog_at.md) |
| 5 | `blog_attention` | 3 | `id`(主键id)、`userid`(人员id)、`attentionid`(关注人id) | [blog_attention.md](./tables/工作微博/blog_attention.md) |
| 6 | `blog_cancelattention` | 3 | `id`(主键id)、`userid`(人员id)、`attentionid`(关注人id) | [blog_cancelattention.md](./tables/工作微博/blog_cancelattention.md) |
| 7 | `blog_discuss` | 10 | `id`(主键id)、`userid`(人员id)、`createdate`(创建日期)、`createtime`(创建时间) 等共 10 个字段 | [blog_discuss.md](./tables/工作微博/blog_discuss.md) |
| 8 | `blog_group` | 3 | `id`(主键id)、`groupname`(分组名称)、`userid`(人员id) | [blog_group.md](./tables/工作微博/blog_group.md) |
| 9 | `blog_location` | 5 | `id`(主键id)、`discussid`(微博id)、`location`(位置)、`createtime`(创建时间) 等共 5 个字段 | [blog_location.md](./tables/工作微博/blog_location.md) |
| 10 | `blog_notes` | 5 | `id`(主键id)、`userid`(人员id)、`updatedate`(更新时间)、`content`(内容) 等共 5 个字段 | [blog_notes.md](./tables/工作微博/blog_notes.md) |
| 11 | `blog_read` | 3 | `id`(主键id)、`userid`(人员id)、`blogid`(微博人员id) | [blog_read.md](./tables/工作微博/blog_read.md) |
| 12 | `blog_remind` | 8 | `id`(主键id)、`remindid`(提醒id)、`relatedid`(相关人id)、`remindtype`(提醒类型) 等共 8 个字段 | [blog_remind.md](./tables/工作微博/blog_remind.md) |
| 13 | `blog_reply` | 11 | `createdate`(创建日期)、`createtime`(创建时间)、`content`(内容)、`comefrom`(来源) 等共 11 个字段 | [blog_reply.md](./tables/工作微博/blog_reply.md) |
| 14 | `blog_reporttemp` | 6 | `id`(主键id)、`userid`(人员id)、`tempname`(模板名称)、`isdisplay`(是否显示) 等共 6 个字段 | [blog_reporttemp.md](./tables/工作微博/blog_reporttemp.md) |
| 15 | `blog_setting` | 5 | `id`(主键id)、`userid`(人员id)、`isreceive`(是否接受申请关注)、`maxattention`(最大关注) 等共 5 个字段 | [blog_setting.md](./tables/工作微博/blog_setting.md) |
| 16 | `blog_share` | 12 | `jobtitlescopeid`(岗位范围)、`id`(主键id)、`blogid`(微博人员id)、`type`(类型) 等共 12 个字段 | [blog_share.md](./tables/工作微博/blog_share.md) |
| 17 | `blog_share_base` | 2 | `id`(主键id)、`sharename`(分享名称) | [blog_share_base.md](./tables/工作微博/blog_share_base.md) |
| 18 | `blog_specifiedshare` | 14 | `shareid`(分享id)、`datatype`(数据类型)、`containlower`(是否含下级)、`rolelevel`(角色类型) 等共 14 个字段 | [blog_specifiedshare.md](./tables/工作微博/blog_specifiedshare.md) |
| 19 | `blog_syssetting` | 12 | `makeupis`(补交是否含工作日)、`caneditis`(编辑是否含工作日)、`id`(主键id)、`allowrequest`(允许请求) 等共 12 个字段 | [blog_syssetting.md](./tables/工作微博/blog_syssetting.md) |
| 20 | `blog_tempcondition` | 4 | `id`(主键id)、`tempid`(报表id)、`type`(类型)、`content`(内容) | [blog_tempcondition.md](./tables/工作微博/blog_tempcondition.md) |
| 21 | `blog_template` | 8 | `id`(主键id)、`tempname`(模板名称)、`isused`(是否启用)、`tempcontent`(模板内容) 等共 8 个字段 | [blog_template.md](./tables/工作微博/blog_template.md) |
| 22 | `blog_templateuser` | 2 | `userid`(人员id)、`templateid`(模板id) | [blog_templateuser.md](./tables/工作微博/blog_templateuser.md) |
| 23 | `blog_tempshare` | 10 | `jobtitlescopeid`(岗位范围)、`id`(主键id)、`tempid`(模板id)、`type`(类型) 等共 10 个字段 | [blog_tempshare.md](./tables/工作微博/blog_tempshare.md) |
| 24 | `blog_usergroup` | 3 | `id`(主键id)、`groupid`(分组id)、`userid`(人员id) | [blog_usergroup.md](./tables/工作微博/blog_usergroup.md) |
| 25 | `blog_visit` | 5 | `id`(主键id)、`userid`(人员id)、`blogid`(访问微博人员id)、`visitdate`(访问日期) 等共 5 个字段 | [blog_visit.md](./tables/工作微博/blog_visit.md) |
| 26 | `blog_zan` | 4 | `id`(主键id)、`blogid`(微博id)、`userid`(人员id)、`zantime`(点赞时间) | [blog_zan.md](./tables/工作微博/blog_zan.md) |

### 协作管理

> 本模块共收录 `21` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `cotype_sharemanager` | 11 | `id`(id)、`cotypeid`(协作区类型id)、`sharetype`(负责人类型)、`sharevalue`(负责人) 等共 11 个字段 | [cotype_sharemanager.md](./tables/协作管理/cotype_sharemanager.md) |
| 2 | `cotype_sharemembers` | 11 | `id`(id)、`cotypeid`(协作区类型id)、`sharetype`(负责人类型)、`sharevalue`(负责人) 等共 11 个字段 | [cotype_sharemembers.md](./tables/协作管理/cotype_sharemembers.md) |
| 3 | `cowork_app` | 6 | `id`(id)、`name`(名称)、`isactive`(是否启用)、`apptype`(应用类型) 等共 6 个字段 | [cowork_app.md](./tables/协作管理/cowork_app.md) |
| 4 | `cowork_apply_info` | 8 | `id`(id)、`coworkid`(协作ID)、`status`(审批状态)、`resourceid`(人员ID) 等共 8 个字段 | [cowork_apply_info.md](./tables/协作管理/cowork_apply_info.md) |
| 5 | `cowork_base_set` | 8 | `coworkstate`(协作主题结束后仍可回复)、`id`(id)、`itemstate`(默认开启主题标题)、`infostate`(废弃了，无用) 等共 8 个字段 | [cowork_base_set.md](./tables/协作管理/cowork_base_set.md) |
| 6 | `cowork_collect` | 7 | `createtime`(收藏时间)、`iscollect`(是否收藏)、`id`(id)、`itemid`(协作id) 等共 7 个字段 | [cowork_collect.md](./tables/协作管理/cowork_collect.md) |
| 7 | `cowork_discuss` | 24 | `remarkback`(内容备份)、`deluserid`(删除人)、`deltime`(删除时间)、`coworkid`(协作ID) 等共 24 个字段 | [cowork_discuss.md](./tables/协作管理/cowork_discuss.md) |
| 8 | `cowork_hidden` | 3 | `id`(id)、`coworkid`(协作ID)、`userid`(用户ID) | [cowork_hidden.md](./tables/协作管理/cowork_hidden.md) |
| 9 | `cowork_important` | 3 | `id`(id)、`coworkid`(协作ID)、`userid`(将协作标记为重要的用户id) | [cowork_important.md](./tables/协作管理/cowork_important.md) |
| 10 | `cowork_item_label` | 3 | `id`(id)、`coworkid`(协作Id)、`labelid`(标签id) | [cowork_item_label.md](./tables/协作管理/cowork_item_label.md) |
| 11 | `cowork_items` | 35 | `endtime`(结束时间)、`beingtime`(开始时间)、`id`(id)、`name`(协作事项名称) 等共 35 个字段 | [cowork_items.md](./tables/协作管理/cowork_items.md) |
| 12 | `cowork_label` | 10 | `id`(id)、`userid`(用户id)、`name`(标签名称)、`labelcolor`(标签颜色) 等共 10 个字段 | [cowork_label.md](./tables/协作管理/cowork_label.md) |
| 13 | `cowork_log` | 7 | `coworkid`(协作ID)、`type`(类型)、`modifydate`(修改日期)、`modifytime`(修改时间) 等共 7 个字段 | [cowork_log.md](./tables/协作管理/cowork_log.md) |
| 14 | `cowork_maintypes` | 4 | `id`(id)、`typename`(协作区类别名称)、`category`(附件目录)、`sequence`(显示顺序) | [cowork_maintypes.md](./tables/协作管理/cowork_maintypes.md) |
| 15 | `cowork_quiter` | 6 | `id`(id)、`itemid`(协作id)、`userid`(退出协作者)、`quitdate`(退出日期) 等共 6 个字段 | [cowork_quiter.md](./tables/协作管理/cowork_quiter.md) |
| 16 | `cowork_read` | 3 | `id`(id)、`coworkid`(协作id)、`userid`(用户id) | [cowork_read.md](./tables/协作管理/cowork_read.md) |
| 17 | `cowork_remind` | 8 | `id`(id)、`reminderid`(提醒评论相关人)、`discussid`(评论ID)、`coworkid`(协作ID) 等共 8 个字段 | [cowork_remind.md](./tables/协作管理/cowork_remind.md) |
| 18 | `cowork_types` | 7 | `id`(id)、`typename`(协作区类型名称)、`departmentid`(部门)、`managerid`(负责人) 等共 7 个字段 | [cowork_types.md](./tables/协作管理/cowork_types.md) |
| 19 | `cowork_votes` | 7 | `id`(id)、`itemid`(协作id)、`discussid`(协作交流id)、`userid`(点赞人) 等共 7 个字段 | [cowork_votes.md](./tables/协作管理/cowork_votes.md) |
| 20 | `coworkaccessory` | 4 | `pathcategory`(目录名（中文）)、`maincategory`(主目录id)、`subcategory`(次目录id)、`seccategory`(三级目录id) | [coworkaccessory.md](./tables/协作管理/coworkaccessory.md) |
| 21 | `coworkshare` | 13 | `id`(id)、`sourceid`(人员ID)、`type`(类型)、`content`(协作参与人) 等共 13 个字段 | [coworkshare.md](./tables/协作管理/coworkshare.md) |

### 版本升级

> 本模块共收录 `17` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `autoconfigkey` | 2 | `id`(ID)、`time`(时间戳) | [autoconfigkey.md](./tables/版本升级/autoconfigkey.md) |
| 2 | `autoconfiglog` | 8 | `id`(ID)、`configdetailid`(主表ID)、`configtype`(配置类型)、`filename`(文件名) 等共 8 个字段 | [autoconfiglog.md](./tables/版本升级/autoconfiglog.md) |
| 3 | `clusterupgradeinfo` | 2 | `id`(ID)、`clusterupgradestatus`(集群升级状态) | [clusterupgradeinfo.md](./tables/版本升级/clusterupgradeinfo.md) |
| 4 | `clusterupgradelog` | 4 | `id`(ID)、`settingid`(clustersetting表ID)、`packagename`(补丁包名称)、`status`(升级状态) | [clusterupgradelog.md](./tables/版本升级/clusterupgradelog.md) |
| 5 | `configfilemanager` | 12 | `id`(ID)、`labelid`(标签id)、`filetype`(文件类型)、`filename`(文件名) 等共 12 个字段 | [configfilemanager.md](./tables/版本升级/configfilemanager.md) |
| 6 | `configpropertiesfile` | 12 | `id`(ID)、`configfileid`(关联的主表ID)、`attrname`(属性名)、`attrvalue`(属性值) 等共 12 个字段 | [configpropertiesfile.md](./tables/版本升级/configpropertiesfile.md) |
| 7 | `configxmlfile` | 11 | `id`(ID)、`configfileid`(关联主表的ID)、`attrvalue`(属性值)、`attrnotes`(属性说明) 等共 11 个字段 | [configxmlfile.md](./tables/版本升级/configxmlfile.md) |
| 8 | `dbupgradeaction` | 9 | `id`(ID)、`name`(action名称)、`mainsequence`(数据迁移步骤sequence)、`detailsequence`(数据迁移明细步骤sequence) 等共 9 个字段 | [dbupgradeaction.md](./tables/版本升级/dbupgradeaction.md) |
| 9 | `dbupgradedetail` | 6 | `id`(ID)、`name`(过程名称)、`status`(执行状态)、`used`(是否启用) 等共 6 个字段 | [dbupgradedetail.md](./tables/版本升级/dbupgradedetail.md) |
| 10 | `dbupgradelog` | 9 | `id`(ID)、`modifyname`(表名/存储过程/方法名等)、`modifyfieldname`(表字段名)、`modifytype`(类型) 等共 9 个字段 | [dbupgradelog.md](./tables/版本升级/dbupgradelog.md) |
| 11 | `dbupgrademain` | 6 | `id`(ID)、`name`(过程名称)、`status`(执行状态)、`used`(是否启用) 等共 6 个字段 | [dbupgrademain.md](./tables/版本升级/dbupgrademain.md) |
| 12 | `ecologyuplist` | 7 | `id`(id)、`label`(补丁包编号)、`versionno`(补丁包号（全称）)、`content`(补丁包内容) 等共 7 个字段 | [ecologyuplist.md](./tables/版本升级/ecologyuplist.md) |
| 13 | `monitorguidelog` | 4 | `id`(ID)、`createdate`(创建日期)、`createtime`(创建时间)、`status`(状态) | [monitorguidelog.md](./tables/版本升级/monitorguidelog.md) |
| 14 | `sqlcounter` | 4 | `id`(ID)、`runned`(已执行脚本数量)、`total`(脚本总数)、`runfilename`(正在执行的脚本名称) | [sqlcounter.md](./tables/版本升级/sqlcounter.md) |
| 15 | `sqlfileloginfo` | 6 | `id`(ID)、`sqlfilename`(脚本名称)、`rundate`(执行日期)、`runtime`(执行时间) 等共 6 个字段 | [sqlfileloginfo.md](./tables/版本升级/sqlfileloginfo.md) |
| 16 | `upgradecheckinfo` | 2 | `id`(ID)、`checkdburl`(是否已确认) | [upgradecheckinfo.md](./tables/版本升级/upgradecheckinfo.md) |
| 17 | `upgradefiletag` | 4 | `id`(ID)、`filepath`(文件路径)、`time`(生成时间)、`md5code`(文件内容MD5码) | [upgradefiletag.md](./tables/版本升级/upgradefiletag.md) |

### 网上调查

> 本模块共收录 `17` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `bill_votingapprove` | 3 | `id`(id)、`votingname`(votingid)、`requestid`(流程id) | [bill_votingapprove.md](./tables/网上调查/bill_votingapprove.md) |
| 2 | `voting` | 35 | `subcompanyid`(分部id)、`id`(主键id)、`subject`(主题)、`detail`(废弃字段) 等共 35 个字段 | [voting.md](./tables/网上调查/voting.md) |
| 3 | `voting_type` | 3 | `id`(调查di)、`typename`(调查名称)、`approver`(审批工作流id) | [voting_type.md](./tables/网上调查/voting_type.md) |
| 4 | `votingconfig` | 11 | `id`(id)、`doc`(相关文档)、`flow`(相关流程)、`customer`(相关客户) 等共 11 个字段 | [votingconfig.md](./tables/网上调查/votingconfig.md) |
| 5 | `votingmaintdetail` | 3 | `id`(id)、`createrid`(创建人id)、`approverid`(审批人id) | [votingmaintdetail.md](./tables/网上调查/votingmaintdetail.md) |
| 6 | `votingoption` | 11 | `id`(id)、`votingid`(调查id)、`questionid`(问题id)、`optioncount`(选项数量) 等共 11 个字段 | [votingoption.md](./tables/网上调查/votingoption.md) |
| 7 | `votingpath` | 6 | `id`(id)、`type`(是附件还是图片)、`title`(附件标题)、`optionid`(选项id) 等共 6 个字段 | [votingpath.md](./tables/网上调查/votingpath.md) |
| 8 | `votingquestion` | 19 | `id`(id)、`description`(描述)、`votingid`(调查id)、`ismulti`(是否是多选) 等共 19 个字段 | [votingquestion.md](./tables/网上调查/votingquestion.md) |
| 9 | `votingremark` | 6 | `votingid`(调查id)、`resourceid`(人员id)、`useranony`(是否匿名)、`remark`(填空题或选择题其他选项) 等共 6 个字段 | [votingremark.md](./tables/网上调查/votingremark.md) |
| 10 | `votingresource` | 6 | `votingid`(调查id)、`questionid`(问题id)、`optionid`(选项id)、`resourceid`(人员id) 等共 6 个字段 | [votingresource.md](./tables/网上调查/votingresource.md) |
| 11 | `votingresourceremark` | 7 | `votingid`(调查id)、`questionid`(问题id)、`resourceid`(选项id)、`useranony`(是否匿名) 等共 7 个字段 | [votingresourceremark.md](./tables/网上调查/votingresourceremark.md) |
| 12 | `votingresourcetemp` | 7 | `votingid`(调查id)、`questionid`(问题id)、`optionid`(选项id)、`resourceid`(用户id) 等共 7 个字段 | [votingresourcetemp.md](./tables/网上调查/votingresourcetemp.md) |
| 13 | `votingshare` | 15 | `id`(id)、`votingid`(调查id)、`sharetype`(共享类型)、`resourceid`(用户id) 等共 15 个字段 | [votingshare.md](./tables/网上调查/votingshare.md) |
| 14 | `votingsharedetail` | 2 | `votingid`(调查id)、`resourceid`(人员id) | [votingsharedetail.md](./tables/网上调查/votingsharedetail.md) |
| 15 | `votingviewer` | 15 | `id`(id)、`votingid`(调查id)、`sharetype`(共享类型)、`resourceid`(人员id) 等共 15 个字段 | [votingviewer.md](./tables/网上调查/votingviewer.md) |
| 16 | `votingviewerdetail` | 2 | `votingid`(调查id)、`resourceid`(人员id) | [votingviewerdetail.md](./tables/网上调查/votingviewerdetail.md) |
| 17 | `votingviewset` | 2 | `votingid`(调查id)、`viewjson`(废弃) | [votingviewset.md](./tables/网上调查/votingviewset.md) |

### 短信模块

> 本模块共收录 `11` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `sms_interface` | 9 | `id`(主键id)、`name`(接口相关名称)、`keyword`(关键字)、`type`(接口类型) 等共 9 个字段 | [sms_interface.md](./tables/短信模块/sms_interface.md) |
| 2 | `sms_message` | 16 | `id`(主键id)、`message`(短信内容)、`recievenumber`(接收短信号码)、`sendnumber`(发送短信号码) 等共 16 个字段 | [sms_message.md](./tables/短信模块/sms_message.md) |
| 3 | `sms_reminder_mode` | 2 | `modekey`(大模块key)、`modename`(大模块名称) | [sms_reminder_mode.md](./tables/短信模块/sms_reminder_mode.md) |
| 4 | `sms_reminder_set` | 7 | `id`(主键id)、`prefix`(提醒前缀)、`prefixconnector`(前缀连接符)、`suffix`(提醒后缀) 等共 7 个字段 | [sms_reminder_set.md](./tables/短信模块/sms_reminder_set.md) |
| 5 | `sms_reminder_type` | 3 | `type`(提醒类型)、`typename`(提醒名称)、`modekey`(对应大模块key) | [sms_reminder_type.md](./tables/短信模块/sms_reminder_type.md) |
| 6 | `sms_set` | 11 | `subcomp`(页面发送分部)、`sign`(签名)、`showreply`(是否显示短信发送页面回复帮助)、`signpos`(签名位置) 等共 11 个字段 | [sms_set.md](./tables/短信模块/sms_set.md) |
| 7 | `sms_template` | 5 | `id`(主键id)、`userid`(用户id)、`title`(显示标题)、`content`(模板内容) 等共 5 个字段 | [sms_template.md](./tables/短信模块/sms_template.md) |
| 8 | `smspropertis` | 3 | `id`(主键)、`prop`(属性)、`val`(值) | [smspropertis.md](./tables/短信模块/smspropertis.md) |
| 9 | `smsvoting` | 17 | `id`(主键id)、`creater`(创建人)、`createdate`(创建日期)、`createtime`(创建时间) 等共 17 个字段 | [smsvoting.md](./tables/短信模块/smsvoting.md) |
| 10 | `smsvotingdetail` | 5 | `id`(主键id)、`smsvotingid`(对应投票id)、`regcontent`(投票选项)、`remark`(说明) 等共 5 个字段 | [smsvotingdetail.md](./tables/短信模块/smsvotingdetail.md) |
| 11 | `smsvotinghrm` | 8 | `id`(主键id)、`smsvotingid`(对应投票id)、`smsvotingdetailid`(对应投票明细id)、`userid`(投票人) 等共 8 个字段 | [smsvotinghrm.md](./tables/短信模块/smsvotinghrm.md) |

### 车辆管理

> 本模块共收录 `7` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `CarInfo` | 14 | `id`(id)、`carNo`(车牌号)、`carType`(车辆类型)、`factoryNo`(生产型号) 等共 14 个字段 | [CarInfo.md](./tables/车辆管理/CarInfo.md) |
| 2 | `CarUseApprove` | 20 | `id`(id)、`carid`(车辆信息)、`driver`(司机)、`userid`(使用人) 等共 20 个字段 | [CarUseApprove.md](./tables/车辆管理/CarUseApprove.md) |
| 3 | `carType` | 4 | `id`(id)、`name`(车辆名称)、`description`(详细描述)、`usefee`(使用里数) | [carType.md](./tables/车辆管理/carType.md) |
| 4 | `car_share` | 25 | `id`(主键)、`carid`(车辆id)、`userid`(人力资源)、`usertype`(共享人员类型) 等共 25 个字段 | [car_share.md](./tables/车辆管理/car_share.md) |
| 5 | `carbasic` | 8 | `id`(ID)、`workflowid`(流程id)、`workflowname`(流程名称)、`typeid`(流程类型id) 等共 8 个字段 | [carbasic.md](./tables/车辆管理/carbasic.md) |
| 6 | `mode_carrelatemode` | 5 | `id`(ID)、`mainid`(主表id)、`carfieldid`(车辆系统表中字段id)、`modefieldid`(当前自定义表字段id) 等共 5 个字段 | [mode_carrelatemode.md](./tables/车辆管理/mode_carrelatemode.md) |
| 7 | `mode_carremindset` | 8 | `timerangeend`(显示时间段结束)、`timerangestart`(显示时间段开始)、`dspunit`(最小占用显示单位)、`usedcolor`(占用颜色) 等共 8 个字段 | [mode_carremindset.md](./tables/车辆管理/mode_carremindset.md) |

### 微搜

> 本模块共收录 `6` 张数据表。

| 序号 | 数据库表名 | 字段数 | 关键字段预览 | 详细定义文件 |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `fullsearch_hotkeys` | 5 | `id`(主键)、`userid`(用户id)、`hotkey`(搜索关键字)、`intcount`(统计次数) 等共 5 个字段 | [fullsearch_hotkeys.md](./tables/微搜/fullsearch_hotkeys.md) |
| 2 | `fullsearch_resultsub` | 13 | `id`(主键)、`createdate`(创建日期)、`createtime`(创建时间)、`searchkey`(搜索关键字) 等共 13 个字段 | [fullsearch_resultsub.md](./tables/微搜/fullsearch_resultsub.md) |
| 3 | `fullsearch_robot` | 10 | `id`(主键)、`title`(标题)、`keywords`(关键字)、`url`(固定链接) 等共 10 个字段 | [fullsearch_robot.md](./tables/微搜/fullsearch_robot.md) |
| 4 | `fullsearch_searchset` | 4 | `id`(主键)、`userid`(用户id)、`searchfield`(查询字段)、`sortfield`(排序方式) | [fullsearch_searchset.md](./tables/微搜/fullsearch_searchset.md) |
| 5 | `fullsearch_viewset` | 8 | `id`(主键)、`userid`(用户id)、`contenttype`(类型)、`canshowfield`(可显示字段) 等共 8 个字段 | [fullsearch_viewset.md](./tables/微搜/fullsearch_viewset.md) |
| 6 | `searchsetinfo` | 3 | `keyinfo`(接口设置键描述信息)、`value`(接口设置值)、`keyname`(接口设置键) | [searchsetinfo.md](./tables/微搜/searchsetinfo.md) |

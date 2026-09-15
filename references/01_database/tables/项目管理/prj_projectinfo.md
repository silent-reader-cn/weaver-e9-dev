# 泛微OA 数据表: `prj_projectinfo`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_projectinfo`
- **字段总数**: `76`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `tinyintfield3` | 自定义选择字段3 | `integer` | - | 是 | 自定义选择字段3 |
| 2 | `tinyintfield4` | 自定义选择字段4 | `integer` | - | 是 | 自定义选择字段4 |
| 3 | `tinyintfield5` | 自定义选择字段5 | `integer` | - | 是 | 自定义选择字段5 |
| 4 | `subcompanyid1` | 分部 | `integer` | - | 是 | 分部 |
| 5 | `members` | 项目成员id | `varchar2` | 3000 | 是 | 项目成员id |
| 6 | `contractids` | 项目客户id | `varchar2` | 1000 | 是 | 项目客户id |
| 7 | `requestid` | 项目审批流程id | `integer` | - | 否 | 项目审批流程id |
| 8 | `procode` | 项目编码 | `varchar2` | 400 | 是 | 项目编码 |
| 9 | `protemplateid` | 项目模板 | `integer` | - | 是 | 项目模板 |
| 10 | `factbegindate` | 备用字段 | `char` | 10 | 是 | 备用字段 |
| 11 | `factenddate` | 备用字段 | `char` | 10 | 是 | 备用字段 |
| 12 | `accessory` | 项目附件 | `varchar2` | 1000 | 是 | 项目附件 |
| 13 | `relationxml` | wbs任务结构 | `long` | 0 | 是 | e8里已经弃用 |
| 14 | `guid1` | uuid标识 | `char` | 36 | 是 | uuid标识 |
| 15 | `isfromws` | 是否webservice创建的项目 | `char` | 1 | 是 | 是否webservice创建的项目 |
| 16 | `ws_other` | 备用字段 | `varchar2` | 4000 | 是 | 备用字段 |
| 17 | `ws_coworkid` | 用webservice创建的项目生成该项目的协作id | `integer` | - | 是 | 用webservice创建的项目生成该项目的协作id |
| 18 | `ecology_pinyin_search` | 联想输入简拼 | `varchar2` | 1000 | 是 | 联想输入简拼 |
| 19 | `from_module_` | 来自于其他模块 | `varchar2` | 80 | 是 | 来自于其他模块(该字段目前预留,暂未使用) |
| 20 | `passnoworktime` | 工期计算跳过非工作日 | `char` | 1 | 是 | 工期计算跳过非工作日 |
| 21 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 22 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 23 | `description` | 相关客户 | `varchar2` | 1500 | 是 | 相关客户 |
| 24 | `prjtype` | 项目类型 | `integer` | - | 是 | 项目类型 |
| 25 | `worktype` | 工作类型 | `integer` | - | 是 | 工作类型 |
| 26 | `securelevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 27 | `status` | 状态 | `integer` | - | 是 | 状态 |
| 28 | `isblock` | 成员可见 | `integer` | - | 是 | 成员可见 |
| 29 | `managerview` | 客户可见 | `integer` | - | 是 | 客户可见 |
| 30 | `parentview` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 31 | `budgetmoney` | 预算 | `number` | (12,3) | 是 | 预算 |
| 32 | `moneyindeed` | 备用字段 | `number` | (12,3) | 是 | 备用字段 |
| 33 | `budgetincome` | 备用字段 | `number` | (12,3) | 是 | 备用字段 |
| 34 | `imcomeindeed` | 备用字段 | `number` | (12,3) | 是 | 备用字段 |
| 35 | `planbegindate` | 预计开始日期 | `varchar2` | 80 | 是 | 预计开始日期 |
| 36 | `planbegintime` | 预计开始时间 | `varchar2` | 40 | 是 | 预计开始时间 |
| 37 | `planenddate` | 预计结束日期 | `varchar2` | 80 | 是 | 预计结束日期 |
| 38 | `planendtime` | 预计结束时间 | `varchar2` | 40 | 是 | 预计结束时间 |
| 39 | `truebegindate` | 实际开始日期 | `varchar2` | 80 | 是 | 实际开始日期 |
| 40 | `truebegintime` | 实际开始时间 | `varchar2` | 40 | 是 | 实际开始时间 |
| 41 | `trueenddate` | 实际结束日期 | `varchar2` | 80 | 是 | 实际结束日期 |
| 42 | `trueendtime` | 实际结束时间 | `varchar2` | 40 | 是 | 实际结束时间 |
| 43 | `planmanhour` | 预计工时 | `integer` | - | 是 | 预计工时 |
| 44 | `truemanhour` | 实际工时 | `integer` | - | 是 | 实际工时 |
| 45 | `picid` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 46 | `intro` | 备用字段 | `varchar2` | 1000 | 是 | 备用字段 |
| 47 | `parentid` | 上级项目id | `integer` | - | 是 | 上级项目id |
| 48 | `envaluedoc` | 评价书 | `integer` | - | 是 | 评价书 |
| 49 | `confirmdoc` | 确认书 | `integer` | - | 是 | 确认书 |
| 50 | `proposedoc` | 建议书 | `integer` | - | 是 | 建议书 |
| 51 | `manager` | 项目经理 | `integer` | - | 是 | 项目经理 |
| 52 | `department` | 项目经理部门 | `integer` | - | 是 | 项目经理部门 |
| 53 | `creater` | 创建者 | `integer` | - | 是 | 创建者 |
| 54 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 55 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 56 | `isprocessed` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 57 | `processer` | 备用字段 | `integer` | - | 是 | 备用字段 |
| 58 | `processdate` | 备用字段 | `varchar2` | 80 | 是 | 备用字段 |
| 59 | `processtime` | 备用字段 | `varchar2` | 64 | 是 | 备用字段 |
| 60 | `datefield1` | 自定义日期字段1 | `varchar2` | 80 | 是 | 自定义日期字段1 |
| 61 | `datefield2` | 自定义日期字段2 | `varchar2` | 80 | 是 | 自定义日期字段2 |
| 62 | `datefield3` | 自定义日期字段3 | `varchar2` | 80 | 是 | 自定义日期字段3 |
| 63 | `datefield4` | 自定义日期字段4 | `varchar2` | 80 | 是 | 自定义日期字段4 |
| 64 | `datefield5` | 自定义日期字段5 | `varchar2` | 80 | 是 | 自定义日期字段5 |
| 65 | `numberfield1` | 自定义数字字段1 | `float` | 22 | 是 | 自定义数字字段1 |
| 66 | `numberfield2` | 自定义数字字段2 | `float` | 22 | 是 | 自定义数字字段2 |
| 67 | `numberfield3` | 自定义数字字段3 | `float` | 22 | 是 | 自定义数字字段3 |
| 68 | `numberfield4` | 自定义数字字段4 | `float` | 22 | 是 | 自定义数字字段4 |
| 69 | `numberfield5` | 自定义数字字段5 | `float` | 22 | 是 | 自定义数字字段5 |
| 70 | `textfield1` | 自定义文本字段1 | `varchar2` | 800 | 是 | 自定义文本字段1 |
| 71 | `textfield2` | 自定义文本字段2 | `varchar2` | 800 | 是 | 自定义文本字段2 |
| 72 | `textfield3` | 自定义文本字段3 | `varchar2` | 800 | 是 | 自定义文本字段3 |
| 73 | `textfield4` | 自定义文本字段4 | `varchar2` | 800 | 是 | 自定义文本字段4 |
| 74 | `textfield5` | 自定义文本字段5 | `varchar2` | 800 | 是 | 自定义文本字段5 |
| 75 | `tinyintfield1` | 自定义选择字段1 | `integer` | - | 是 | 自定义选择字段1 |
| 76 | `tinyintfield2` | 自定义选择字段2 | `integer` | - | 是 | 自定义选择字段2 |

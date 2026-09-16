# 泛微OA 数据表: `hrmcareerapply`

- **中文名称**: 人力资源应聘信息表－基本信息
- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerapply`
- **主键**: `id`
- **字段数**: `114`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `folk` | 民族 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 民族 |
| 2 | `islabouunion` | 是否为工会会员 | `char` | 1 | 是 | 否 | 否 | - | - | 是否为工会会员 |
| 3 | `tempresidentnumber` | 暂住证号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 暂住证号 |
| 4 | `nowstep` | 当前所处阶段 | `integer` | - | 是 | 否 | 否 | - | (0) | 当前所处阶段 |
| 5 | `isinform` | 是否已通知 | `integer` | - | 是 | 否 | 否 | - | (0) | 是否已通知 /*0、未通知；1、已通知*/ |
| 6 | `height` | 身高 | `number` | (38,2) | 是 | 否 | 否 | - | - | 身高 |
| 7 | `weight` | 体重 | `number` | (38,2) | 是 | 否 | 否 | - | - | 体重 |
| 8 | `picture` | 照片id | `integer` | - | 是 | 否 | 否 | - | - | 照片id |
| 9 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | 分部id |
| 10 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 11 | `ischeck` | 是否已审核 | `char` | 1 | 是 | 否 | 否 | - | - | 是否已审核 |
| 12 | `ishire` | 是否已雇佣 | `char` | 1 | 是 | 否 | 否 | - | - | 是否已雇佣 |
| 13 | `loginid` | 系统登陆帐号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 系统登陆帐号 |
| 14 | `password` | 系统登陆密码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 系统登陆密码 |
| 15 | `firstname` | 姓 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 姓 |
| 16 | `lastname` | 名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 名 |
| 17 | `aliasname` | 别名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 别名 |
| 18 | `titleid` | 称谓 | `integer` | - | 是 | 否 | 否 | - | - | 称谓 |
| 19 | `sex` | 性别 | `char` | 1 | 是 | 否 | 否 | - | - | 性别 |
| 20 | `birthday` | 生日 | `char` | 10 | 是 | 否 | 否 | - | - | 生日 |
| 21 | `nationality` | 国家 | `integer` | - | 是 | 否 | 否 | - | - | 国家 |
| 22 | `defaultlanguage` | 默认语言 | `integer` | - | 是 | 否 | 否 | - | - | 默认语言 |
| 23 | `systemlanguage` | 系统语言 | `integer` | - | 是 | 否 | 否 | - | - | 系统语言 |
| 24 | `certificatecategory` | 证书 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 证书 |
| 25 | `certificatenum` | 证书号码 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 证书号码 |
| 26 | `nativeplace` | 籍贯 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 籍贯 |
| 27 | `educationlevel` | 学历 | `integer` | - | 是 | 否 | 否 | - | - | 学历 |
| 28 | `bememberdate` | 入团日期 | `char` | 10 | 是 | 否 | 否 | - | - | 入团日期 |
| 29 | `bepartydate` | 入党日期 | `char` | 10 | 是 | 否 | 否 | - | - | 入党日期 |
| 30 | `bedemocracydate` | 恢复群众身份日期 | `char` | 10 | 是 | 否 | 否 | - | - | 恢复群众身份日期 |
| 31 | `regresidentplace` | 户口 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 户口 |
| 32 | `healthinfo` | 健康状况 | `char` | 1 | 是 | 否 | 否 | - | - | 健康状况 |
| 33 | `residentplace` | 住址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 住址 |
| 34 | `policy` | 政治面貌 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 政治面貌 |
| 35 | `degree` | 学位 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 学位 |
| 36 | `homepage` | 个人主页 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 个人主页 |
| 37 | `maritalstatus` | 婚姻状况 | `char` | 1 | 是 | 否 | 否 | - | - | 婚姻状况 |
| 38 | `marrydate` | 结婚日期 | `char` | 10 | 是 | 否 | 否 | - | - | 结婚日期 |
| 39 | `train` | 培训情况 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 培训情况 |
| 40 | `resourceimageid` | 图片id | `integer` | - | 是 | 否 | 否 | - | - | 图片id |
| 41 | `officephone` | 电话 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 电话 |
| 42 | `mobile` | 手机 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 手机 |
| 43 | `mobilecall` | 其他电话 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 其他电话 |
| 44 | `email` | 电子邮件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 电子邮件 |
| 45 | `countryid` | 国家id | `integer` | - | 是 | 否 | 否 | - | - | 国家id |
| 46 | `locationid` | 工作地点 | `integer` | - | 是 | 否 | 否 | - | - | 工作地点 |
| 47 | `workroom` | 办公室 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 办公室 |
| 48 | `homeaddress` | 家庭住址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 家庭住址 |
| 49 | `homepostcode` | 住址邮编 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 住址邮编 |
| 50 | `homephone` | 家庭电话 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 家庭电话 |
| 51 | `timezone` | 时区 | `integer` | - | 是 | 否 | 否 | - | - | 时区 |
| 52 | `worktype` | 工作类别 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 工作类别 |
| 53 | `usekind` | 用工性质 | `integer` | - | 是 | 否 | 否 | - | - | 用工性质 |
| 54 | `workcode` | 编号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 编号 |
| 55 | `contractbegintime` | 合同开始时间 | `char` | 10 | 是 | 否 | 否 | - | - | 合同开始时间 |
| 56 | `startdate` | 合同开始日期 | `char` | 10 | 是 | 否 | 否 | - | - | 合同开始日期 |
| 57 | `enddate` | 合同结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | 合同结束日期 |
| 58 | `contractdate` | 合同到期日期 | `char` | 10 | 是 | 否 | 否 | - | - | 合同到期日期 |
| 59 | `resourcetype` | 用户类别 | `char` | 1 | 是 | 否 | 否 | - | - | 用户类别 |
| 60 | `jobtitle` | 岗位 | `integer` | - | 是 | 否 | 否 | - | - | 岗位 |
| 61 | `jobgroup` | 职务类别 | `integer` | - | 是 | 否 | 否 | - | - | 职务类别 |
| 62 | `jobright` | 工作权利 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 工作权利 |
| 63 | `jobcall` | 职称 | `integer` | - | 是 | 否 | 否 | - | - | 职称 |
| 64 | `jobtype` | 工作类别 | `integer` | - | 是 | 否 | 否 | - | - | 工作类别 |
| 65 | `jobactivity` | 工作职责 | `integer` | - | 是 | 否 | 否 | - | - | 工作职责 |
| 66 | `jobactivitydesc` | 工作职责描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 工作职责描述 |
| 67 | `joblevel` | 职级 | `integer` | - | 是 | 否 | 否 | - | - | 职级 |
| 68 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别 |
| 69 | `departmentid` | 部门id | `integer` | - | 是 | 否 | 否 | - | - | 部门id |
| 70 | `subcompanyid1` | 分部1 | `integer` | - | 是 | 否 | 否 | - | - | 分部1 |
| 71 | `subcompanyid2` | 分部2 | `integer` | - | 是 | 否 | 否 | - | - | 分部2 |
| 72 | `subcompanyid3` | 分部3 | `integer` | - | 是 | 否 | 否 | - | - | 分部3 |
| 73 | `subcompanyid4` | 分部4 | `integer` | - | 是 | 否 | 否 | - | - | 分部4 |
| 74 | `costcenterid` | 成本中心 | `integer` | - | 是 | 否 | 否 | - | - | 成本中心 |
| 75 | `managerid` | 直接上级 | `integer` | - | 是 | 否 | 否 | - | - | 直接上级 |
| 76 | `assistantid` | 助理 | `integer` | - | 是 | 否 | 否 | - | - | 助理 |
| 77 | `purchaselimit` | 购买上限 | `number` | (10,3) | 是 | 否 | 否 | - | - | 购买上限 |
| 78 | `currencyid` | 币种 | `integer` | - | 是 | 否 | 否 | - | - | 币种 |
| 79 | `bankid1` | 工资银行1 | `integer` | - | 是 | 否 | 否 | - | - | 工资银行1 |
| 80 | `accountid1` | 银行帐号1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 银行帐号1 |
| 81 | `bankid2` | 工资银行2 | `integer` | - | 是 | 否 | 否 | - | - | 工资银行2 |
| 82 | `accountid2` | 银行帐号2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 银行帐号2 |
| 83 | `securityno` | 社会安全号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 社会安全号 |
| 84 | `accumfundaccount` | 公积金号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 公积金号 |
| 85 | `creditcard` | 信用卡号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 信用卡号 |
| 86 | `expirydate` | 到期日期 | `char` | 10 | 是 | 否 | 否 | - | - | 到期日期 |
| 87 | `datefield1` | 冗余日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余日期字段 |
| 88 | `datefield2` | 冗余日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余日期字段 |
| 89 | `datefield3` | 冗余日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余日期字段 |
| 90 | `datefield4` | 冗余日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余日期字段 |
| 91 | `datefield5` | 冗余日期字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余日期字段 |
| 92 | `numberfield1` | 冗余数字字段 | `float` | 53 | 是 | 否 | 否 | - | - | 冗余数字字段 |
| 93 | `numberfield2` | 冗余数字字段 | `float` | 53 | 是 | 否 | 否 | - | - | 冗余数字字段 |
| 94 | `numberfield3` | 冗余数字字段 | `float` | 53 | 是 | 否 | 否 | - | - | 冗余数字字段 |
| 95 | `numberfield4` | 冗余数字字段 | `float` | 53 | 是 | 否 | 否 | - | - | 冗余数字字段 |
| 96 | `numberfield5` | 冗余数字字段 | `float` | 53 | 是 | 否 | 否 | - | - | 冗余数字字段 |
| 97 | `textfield1` | 冗余文本字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余文本字段 |
| 98 | `textfield2` | 冗余文本字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余文本字段 |
| 99 | `textfield3` | 冗余文本字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余文本字段 |
| 100 | `textfield4` | 冗余文本字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余文本字段 |
| 101 | `textfield5` | 冗余文本字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 冗余文本字段 |
| 102 | `tinyintfield1` | 冗余判断字段 | `integer` | - | 是 | 否 | 否 | - | - | 冗余判断字段 |
| 103 | `tinyintfield2` | 冗余判断字段 | `integer` | - | 是 | 否 | 否 | - | - | 冗余判断字段 |
| 104 | `tinyintfield3` | 冗余判断字段 | `integer` | - | 是 | 否 | 否 | - | - | 冗余判断字段 |
| 105 | `tinyintfield4` | 冗余判断字段 | `integer` | - | 是 | 否 | 否 | - | - | 冗余判断字段 |
| 106 | `tinyintfield5` | 冗余判断字段 | `integer` | - | 是 | 否 | 否 | - | - | 冗余判断字段 |
| 107 | `createrid` | 创建人id | `integer` | - | 是 | 否 | 否 | - | - | 创建人id |
| 108 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | 创建日期 |
| 109 | `lastmodid` | 最后修改人id | `integer` | - | 是 | 否 | 否 | - | - | 最后修改人id |
| 110 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最后修改日期 |
| 111 | `lastlogindate` | 最后登陆日期 | `char` | 10 | 是 | 否 | 否 | - | - | 最后登陆日期 |
| 112 | `careerid` | 招聘职务id | `integer` | - | 是 | 否 | 否 | - | - | 招聘职务id |
| 113 | `numberid` | 应聘人编号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 应聘人编号 |
| 114 | `careerinviteid` | 所应聘的招聘信息 | `integer` | - | 是 | 否 | 否 | - | - | 所应聘的招聘信息 |

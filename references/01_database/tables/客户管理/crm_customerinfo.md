# 泛微OA 数据表: `crm_customerinfo`

- **中文名称**: 客户信息表
- **所属模块**: `客户管理`
- **数据库表名**: `crm_customerinfo`
- **主键**: `id`
- **字段数**: `97`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `seasflag` | 公海标志 | `integer` | - | 是 | 否 | 否 | - | - | 1:公海客户，2，公海客户申请中，3：申请成功 |
| 2 | `oldmanager` | 1 | `integer` | - | 是 | 否 | 否 | - | - | 原客户经理，用于公海客户 |
| 3 | `kh` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `approvedate` | 1 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 5 | `dkh` | 1 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 6 | `reew` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `creditamount` | 信用额度 | `number` | (10,2) | 是 | 否 | 否 | - | - | - |
| 8 | `credittime` | 信用期间 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `evaluation` | 客户价值 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `bankname` | 银行名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `accountname` | 账户名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `accounts` | 账号 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `crmcode` | 客户编码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 14 | `sex` | 性别 | `integer` | - | 是 | 否 | 否 | - | (0) | - |
| 15 | `idcardno` | 身份证号 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 16 | `twname` | 繁体名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 17 | `introduction` | 介绍 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 18 | `ecology_pinyin_search` | 名称拼音 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 19 | `district` | 区县 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `salt` | 盐 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 21 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 22 | `name` | 名称 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 23 | `language` | 语言 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `engname` | 英文名 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `address1` | 地址1 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 26 | `address2` | 地址2 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 27 | `address3` | 地址3 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 28 | `zipcode` | 邮编 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 29 | `city` | 城市 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 30 | `country` | 国家 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 31 | `province` | 省份 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 32 | `county` | 区县 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 33 | `phone` | 电话 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 34 | `fax` | 传真 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 35 | `email` | 邮箱 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 36 | `website` | 网站 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 37 | `source` | 联系方式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 38 | `sector` | 行业部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 39 | `size_n` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 40 | `manager` | 客户经理 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 41 | `agent` | 代理商 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 42 | `parentid` | 上一级客户id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 43 | `department` | 部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 44 | `fincode` | 财务代码 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 45 | `currency` | 货币id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 46 | `contractlevel` | 合同金额 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 47 | `creditlevel` | 信用等级 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 48 | `creditoffset` | 信用等级之外的信用额度调整 | `number` | (12,3) | 是 | 否 | 否 | - | - | - |
| 49 | `discount` | 折扣率 | `number` | (12,3) | 是 | 否 | 否 | - | - | - |
| 50 | `taxnumber` | 增值税号码 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 51 | `bankacount` | 银行账号 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 52 | `invoiceacount` | 发票客户 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 53 | `deliverytype` | 送货类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 54 | `paymentterm` | 支付条件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `paymentway` | 支付方式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 56 | `saleconfirm` | 销售确认书 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 57 | `creditcard` | 信用卡号 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 58 | `creditexpire` | 信用卡到期日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 59 | `documentid` | 文档ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 60 | `picid` | 图片id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 61 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 62 | `typebegin` | 起始日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 63 | `description` | 描述 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 64 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 65 | `rating` | 级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 66 | `datefield1` | 自定义字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 67 | `datefield2` | 自定义字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 68 | `datefield3` | 自定义字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 69 | `datefield4` | 自定义字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 70 | `datefield5` | 自定义字段 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 71 | `numberfield1` | 自定义字段自定义字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 72 | `numberfield2` | 自定义字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 73 | `numberfield3` | 自定义字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 74 | `numberfield4` | 自定义字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 75 | `numberfield5` | 自定义字段 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 76 | `textfield1` | 自定义字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 77 | `textfield2` | 自定义字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 78 | `textfield3` | 自定义字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 79 | `textfield4` | 自定义字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 80 | `textfield5` | 自定义字段 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 81 | `tinyintfield1` | 自定义字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 82 | `tinyintfield2` | 自定义字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 83 | `tinyintfield3` | 自定义字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 84 | `tinyintfield4` | 自定义字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 85 | `tinyintfield5` | 自定义字段 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 86 | `deleted` | 是否删除 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 87 | `subcompanyid1` | 分部 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 88 | `seclevel` | 安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 89 | `portalloginid` | 门户登录账号 | `varchar2` | 480 | 是 | 否 | 否 | - | - | - |
| 90 | `portalpassword` | 门户登录密码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 91 | `portalstatus` | 门户状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 92 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 93 | `introductiondocid` | 背景资料 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 94 | `lat1` | 维度 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 95 | `lng1` | 经度 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 96 | `tyxzk` | 1 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 97 | `check1` | 1 | `char` | 1 | 是 | 否 | 否 | - | - | - |

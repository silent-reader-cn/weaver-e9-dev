# 泛微OA 数据表: `mode_remindjob`

- **中文名称**: 提醒基本信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_remindjob`
- **主键**: `id`
- **字段数**: `60`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `formtype` | 数据表单类型 | `integer` | - | 是 | 否 | 否 | - | - | 0:代表主表<br>1:代表明细表1<br>2:代表明细表2<br>... |
| 2 | `remindsms` | 短信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `remindemail` | 邮件提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `remindworkflow` | 流程提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `remindwechat` | 云桥微信提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `remindemobile` | emobile提醒 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `remindemobile_msgtype` | 提醒方式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `remindemobile_msgurl` | 提醒的链接 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `triggerworkflowsetid` | 触发的流程id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `sqlwherejson` | sql提醒条件 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 11 | `workflowtype` | 流程类型 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 12 | `remindcontentaddress` | 提醒内容 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 14 | `name` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `isenable` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 16 | `remindtype` | 提醒类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：即时提醒<br>2：到期提醒<br>3：循环提醒 |
| 17 | `formid` | 表单名称 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |
| 18 | `modeid` | 模块名称 | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表的id |
| 19 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应modetreefield表的id |
| 20 | `createtime` | 创建时间 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 21 | `creator` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `remindtimetype` | 到期时间类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：常量<br>2：字段 |
| 23 | `reminddatefield` | 到期日期字段 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 24 | `remindtimefield` | 到期时间字段 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 25 | `reminddate` | 到期日期常量 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 26 | `remindtime` | 到期时间常量 | `varchar2` | 160 | 是 | 否 | 否 | - | - | - |
| 27 | `incrementway` | 时间增量 | `integer` | - | 是 | 否 | 否 | - | - | 1：提前<br>2：延迟 |
| 28 | `incrementtype` | 时间增量类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：整数常量<br>2：整数字段 |
| 29 | `incrementfield` | 时间增量整数字段 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 30 | `incrementnum` | 时间增量增长量 | `integer` | - | 是 | 否 | 否 | - | - | 提前或延迟的常量 |
| 31 | `incrementunit` | 时间增量单位 | `integer` | - | 是 | 否 | 否 | - | - | 1：分钟<br>2：小时<br>3：天 |
| 32 | `remindway` | 提醒方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：微信提醒<br>2：短信提醒<br>3：邮件提醒<br>4：流程提醒 |
| 33 | `sendertype` | 创建人类型 | `integer` | - | 是 | 否 | 否 | - | - | 短信发送人/流程创建人类型。<br>1：系统管理员<br>2：模块创建人<br>3：单人力资源字段 |
| 34 | `senderfield` | 创建人字段 | `integer` | - | 是 | 否 | 否 | - | - | 单人力资源字段，对应workflow_billfield表的id |
| 35 | `subject` | 发送标题 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 邮件标题/流程标题，可取字段的值作为变量 |
| 36 | `reminddml` | dml方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 保留 |
| 37 | `remindjava` | java提醒方式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 保留 |
| 38 | `conditionstype` | 条件类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：字段<br>2：sql |
| 39 | `conditionsfield` | 条件字段sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 字段类型sql |
| 40 | `conditionsfieldcn` | 条件字段显示名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 字段类型sql显示名称 |
| 41 | `conditionssql` | 条件sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | sql类型的sqlwhere |
| 42 | `conditionsjava` | java条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 保留 |
| 43 | `remindcontenttype` | 提醒内容类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：文本<br>2：java |
| 44 | `remindcontenttext` | 提醒内容文本 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 45 | `remindcontentjava` | 提醒内容java | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 46 | `receivertype` | 提醒接收人员类型 | `integer` | - | 是 | 否 | 否 | - | - | 1:人员<br>2:分部<br>3:部门<br>4:角色<br>5:所有人<br>6:模块创建人 |
| 47 | `receiverdetail` | 提醒接收人员对象id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 48 | `receiverfieldtype` | 提醒接收人员字段类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：人员<br>2：部门<br>3：分部 |
| 49 | `receiverfield` | 提醒接收人员字段 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 50 | `receiverlevel` | 提醒接收人员安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 51 | `triggerway` | 定时器触发方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：简单规则<br>2：表达式 |
| 52 | `triggertype` | 定时器运行频率 | `integer` | - | 是 | 否 | 否 | - | - | 1：分钟<br>2：小时<br>3：天<br>4：周<br>5：月<br>6：仅一次 |
| 53 | `triggerexpression` | 定时器表达式 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 54 | `triggercycletime` | 定时器循环周期 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 55 | `weeks` | 周 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 56 | `months` | 月 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 57 | `days` | 天 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 58 | `remindtimetype2` | 提醒类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 59 | `remindtimevalue` | 提醒时间的值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 60 | `remindcontenturl` | 链接 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |

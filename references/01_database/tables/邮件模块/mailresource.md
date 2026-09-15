# 泛微OA 数据表: `mailresource`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailresource`
- **字段总数**: `61`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `tosubcomids` | 收件人-分部 | `clob` | 4000 | 是 | - |
| 2 | `ccsubcomids` | 抄送人-分部 | `clob` | 4000 | 是 | - |
| 3 | `bccsubcomids` | 密送人-分部 | `clob` | 4000 | 是 | - |
| 4 | `togroupids` | 收件人-群组 | `clob` | 4000 | 是 | - |
| 5 | `ccgroupids` | 抄送人-群组 | `clob` | 4000 | 是 | - |
| 6 | `bccgroupids` | 密送人-群组 | `clob` | 4000 | 是 | - |
| 7 | `mr_uuid` | 已发送邮件唯一标志 | `varchar2` | 50 | 是 | - |
| 8 | `isautoreceive` | 是否为自动接收入库的 | `char` | 1 | 是 | 1：是 |
| 9 | `receivetime` | 入库时间 | `varchar2` | 1000 | 是 | - |
| 10 | `issendapart` | 是否为分别发送 | `char` | 1 | 是 | 1：是 |
| 11 | `id` | ID | `integer` | - | 否 | - |
| 12 | `resourceid` | 发送人 | `integer` | - | 是 | - |
| 13 | `priority` | 优先级 | `char` | 1 | 是 | - |
| 14 | `sendfrom` | 发件人邮件地址 | `varchar2` | 4000 | 是 | - |
| 15 | `sendcc_bak` | 废弃字段！ | `varchar2` | 4000 | 是 | - |
| 16 | `tmpsendbcc_bak` | 废弃字段！ | `varchar2` | 4000 | 是 | - |
| 17 | `sendto_bak` | 废弃字段！ | `varchar2` | 4000 | 是 | - |
| 18 | `senddate` | 发送日期 | `varchar2` | 240 | 是 | - |
| 19 | `size_n` | 邮件大小 | `integer` | - | 是 | - |
| 20 | `subject` | 主题 | `varchar2` | 1200 | 是 | - |
| 21 | `content` | 内容 | `varchar2` | 4000 | 是 | - |
| 22 | `mailtype` | 邮件类型 | `char` | 1 | 是 | - |
| 23 | `hashtmlimage` | 是否包含html图片 | `char` | 1 | 是 | - |
| 24 | `attachmentnumber` | 附件数量 | `integer` | - | 是 | - |
| 25 | `status` | 邮件状态 | `char` | 1 | 是 | 0:未读，1:已读 |
| 26 | `folderid` | 文件夹id | `integer` | - | 是 | - |
| 27 | `mailaccountid` | 邮件帐户id | `integer` | - | 是 | - |
| 28 | `istemp` | 临时存放的邮件，用于发送邮件时规则应用 | `char` | 1 | 是 | 0:非，1:临时邮件 |
| 29 | `emlname` | eml文件名 | `varchar2` | 400 | 是 | - |
| 30 | `emltime` | 生成eml的时间 | `varchar2` | 240 | 是 | - |
| 31 | `haseml` | 是否有eml文件 | `integer` | - | 是 | -1：没有，&gt; -1 有 |
| 32 | `emlpath` | eml文件保存的路径 | `varchar2` | 1000 | 是 | - |
| 33 | `originalmailid` | 源邮件 | `integer` | - | 是 | 对应原邮件的id |
| 34 | `star` | 星标 | `integer` | - | 是 | 1：有 |
| 35 | `isinternal` | 内部邮件 | `integer` | - | 是 | 1：是内部邮件 |
| 36 | `canview` | 可查看 | `integer` | - | 是 | - |
| 37 | `ccdpids` | 抄送部门id | `varchar2` | 4000 | 是 | - |
| 38 | `bccdpids` | 密送部门id | `varchar2` | 4000 | 是 | - |
| 39 | `todpids` | 收件部门id | `varchar2` | 4000 | 是 | - |
| 40 | `toall` | 收件人为所有人 | `varchar2` | 80 | 是 | - |
| 41 | `ccall` | 抄送人为所有人 | `varchar2` | 80 | 是 | - |
| 42 | `bccall` | 密送人为所有人 | `varchar2` | 80 | 是 | - |
| 43 | `toids` | 内部邮件收件人 | `varchar2` | 4000 | 是 | - |
| 44 | `ccids` | 内部邮件抄送人 | `varchar2` | 4000 | 是 | - |
| 45 | `bccids` | 内部邮件密送人 | `varchar2` | 4000 | 是 | - |
| 46 | `readdate` | 阅读时间 | `varchar2` | 240 | 是 | - |
| 47 | `timingdate` | 定时发送日期 | `varchar2` | 30 | 是 | - |
| 48 | `timingdatestate` | 定时发送状态 | `integer` | - | 是 | - |
| 49 | `needreceipt` | 是否回执 | `integer` | - | 是 | - |
| 50 | `recallstate` | 回执状态 | `char` | 1 | 是 | - |
| 51 | `receiveneedreceipt` | 是否接受到回执请求 | `char` | 1 | 是 | - |
| 52 | `messageid` | 外部邮件id | `varchar2` | 1000 | 是 | - |
| 53 | `waitdeal` | 是否待办 | `varchar2` | 20 | 是 | - |
| 54 | `waitdealtime` | 待办时间 | `varchar2` | 160 | 是 | - |
| 55 | `waitdealnote` | 待办内容 | `varchar2` | 1000 | 是 | - |
| 56 | `wdremindtime` | 待办提醒时间 | `varchar2` | 20 | 是 | - |
| 57 | `waitdealway` | 待办提醒方式 | `varchar2` | 80 | 是 | - |
| 58 | `flag` | 回复、转发、回复并转发标志 | `integer` | - | 是 | 回复、转发、回复并转发标志 |
| 59 | `sendto` | 接受人邮件地址 | `clob` | 4000 | 是 | - |
| 60 | `sendcc` | 转发人邮件地址 | `clob` | 4000 | 是 | - |
| 61 | `sendbcc` | 密送人邮件地址 | `clob` | 4000 | 是 | - |

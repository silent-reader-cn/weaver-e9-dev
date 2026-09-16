# 泛微OA 数据表: `cowork_items`

- **中文名称**: 协作事项表
- **所属模块**: `协作管理`
- **数据库表名**: `cowork_items`
- **主键**: `id`
- **字段数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `endtime` | 结束时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 2 | `beingtime` | 开始时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 4 | `name` | 协作事项名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `typeid` | 协作类型id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `levelvalue` | 级别 | `integer` | - | 是 | 否 | 否 | - | - | 0、正常；1、紧急 |
| 7 | `creater` | 创建人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 10 | `begindate` | 开始日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 11 | `enddate` | 结束日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `relatedprj` | 相关项目 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 14 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 16 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 1、正常；2、结束 |
| 17 | `userids` | 将该协作标示为“重要协作”的人员ID | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 18 | `coworkers` | 协作参与者 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 19 | `isnew` | 是否查看 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 20 | `readers` | 查看人 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `lastdiscussant` | 协作的最后回复人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `coworkmanager` | 协作的管理者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `accessory` | 该协作在创建时添加的附件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 24 | `mutil_prjs` | 相关项目 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `principal` | 负责人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `replynum` | 回复数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `readnum` | 查看排序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 28 | `lastupdatedate` | 最后更新日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 29 | `lastupdatetime` | 最后更新时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 30 | `isapproval` | 是否需要审批 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 31 | `isanonymous` | 是否允许匿名 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 32 | `approvalatatus` | 批量审批 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 33 | `istop` | 是否置顶 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 34 | `isapply` | 是否允许申请 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 35 | `remark` | 备注 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `cowork_items`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_items`
- **字段总数**: `35`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `endtime` | 结束时间 | `varchar2` | 8 | 是 | - |
| 2 | `beingtime` | 开始时间 | `varchar2` | 8 | 是 | - |
| 3 | `id` | id | `integer` | - | 否 | - |
| 4 | `name` | 协作事项名称 | `varchar2` | 800 | 是 | - |
| 5 | `typeid` | 协作类型id | `integer` | - | 是 | - |
| 6 | `levelvalue` | 级别 | `integer` | - | 是 | 0、正常；1、紧急 |
| 7 | `creater` | 创建人 | `integer` | - | 是 | - |
| 8 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 9 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 10 | `begindate` | 开始日期 | `char` | 10 | 是 | - |
| 11 | `enddate` | 结束日期 | `char` | 10 | 是 | - |
| 12 | `relatedprj` | 相关项目 | `varchar2` | 1000 | 是 | - |
| 13 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | - |
| 14 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | - |
| 15 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | - |
| 16 | `status` | 状态 | `integer` | - | 是 | 1、正常；2、结束 |
| 17 | `userids` | 将该协作标示为“重要协作”的人员ID | `varchar2` | 4000 | 是 | - |
| 18 | `coworkers` | 协作参与者 | `clob` | 4000 | 是 | - |
| 19 | `isnew` | 是否查看 | `clob` | 4000 | 是 | - |
| 20 | `readers` | 查看人 | `clob` | 4000 | 是 | - |
| 21 | `lastdiscussant` | 协作的最后回复人 | `integer` | - | 是 | - |
| 22 | `coworkmanager` | 协作的管理者 | `integer` | - | 是 | - |
| 23 | `accessory` | 该协作在创建时添加的附件 | `varchar2` | 1000 | 是 | - |
| 24 | `mutil_prjs` | 相关项目 | `varchar2` | 1000 | 是 | - |
| 25 | `principal` | 负责人 | `integer` | - | 是 | - |
| 26 | `replynum` | 回复数 | `integer` | - | 是 | - |
| 27 | `readnum` | 查看排序 | `integer` | - | 是 | - |
| 28 | `lastupdatedate` | 最后更新日期 | `varchar2` | 80 | 是 | - |
| 29 | `lastupdatetime` | 最后更新时间 | `varchar2` | 80 | 是 | - |
| 30 | `isapproval` | 是否需要审批 | `integer` | - | 是 | - |
| 31 | `isanonymous` | 是否允许匿名 | `integer` | - | 是 | - |
| 32 | `approvalatatus` | 批量审批 | `integer` | - | 是 | - |
| 33 | `istop` | 是否置顶 | `integer` | - | 是 | - |
| 34 | `isapply` | 是否允许申请 | `char` | 1 | 是 | - |
| 35 | `remark` | 备注 | `clob` | 4000 | 是 | - |

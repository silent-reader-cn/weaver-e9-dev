# 泛微OA 数据表: `cowork_discuss`

- **中文名称**: 协作区讨论记录表
- **所属模块**: `协作管理`
- **数据库表名**: `cowork_discuss`
- **主键**: `id`
- **字段数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `remarkback` | 内容备份 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 2 | `deluserid` | 删除人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `deltime` | 删除时间 | `varchar2` | 19 | 是 | 否 | 否 | - | - | - |
| 4 | `coworkid` | 协作ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `discussant` | 讨论参与者id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `createdate` | 发表日期 | `char` | 10 | 是 | 否 | 否 | - | - | - |
| 7 | `createtime` | 发表时间 | `char` | 8 | 是 | 否 | 否 | - | - | - |
| 8 | `relatedprj` | 相关任务 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 9 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 11 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `ralatedaccessory` | 附件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `remark` | 内容 | `clob` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `mutil_prjs` | 相关项目 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `id` | id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 16 | `floornum` | 楼号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `replayid` | 回复ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `topdiscussid` | 被评论的留言ID | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 19 | `commentid` | 评论ID | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 20 | `commentuserid` | 被评论人id | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 21 | `istop` | 是否置顶 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 22 | `approvalatatus` | 审批状态 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 23 | `isanonymous` | 是否匿名 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 24 | `isdel` | 是否删除 | `integer` | - | 是 | 否 | 否 | - | 0 | - |

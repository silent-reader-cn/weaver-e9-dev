# 泛微OA 数据表: `cowork_discuss`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_discuss`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `remarkback` | 内容备份 | `clob` | 4000 | 是 | - |
| 2 | `deluserid` | 删除人 | `integer` | - | 是 | - |
| 3 | `deltime` | 删除时间 | `varchar2` | 19 | 是 | - |
| 4 | `coworkid` | 协作ID | `integer` | - | 是 | - |
| 5 | `discussant` | 讨论参与者id | `integer` | - | 是 | - |
| 6 | `createdate` | 发表日期 | `char` | 10 | 是 | - |
| 7 | `createtime` | 发表时间 | `char` | 8 | 是 | - |
| 8 | `relatedprj` | 相关任务 | `varchar2` | 1000 | 是 | - |
| 9 | `relatedcus` | 相关客户 | `varchar2` | 1000 | 是 | - |
| 10 | `relatedwf` | 相关流程 | `varchar2` | 1000 | 是 | - |
| 11 | `relateddoc` | 相关文档 | `varchar2` | 1000 | 是 | - |
| 12 | `ralatedaccessory` | 附件 | `varchar2` | 1000 | 是 | - |
| 13 | `remark` | 内容 | `clob` | 4000 | 是 | - |
| 14 | `mutil_prjs` | 相关项目 | `varchar2` | 1000 | 是 | - |
| 15 | `id` | id | `integer` | - | 否 | - |
| 16 | `floornum` | 楼号 | `integer` | - | 是 | - |
| 17 | `replayid` | 回复ID | `integer` | - | 是 | - |
| 18 | `topdiscussid` | 被评论的留言ID | `integer` | - | 是 | - |
| 19 | `commentid` | 评论ID | `integer` | - | 是 | - |
| 20 | `commentuserid` | 被评论人id | `integer` | - | 是 | - |
| 21 | `istop` | 是否置顶 | `integer` | - | 是 | - |
| 22 | `approvalatatus` | 审批状态 | `integer` | - | 是 | - |
| 23 | `isanonymous` | 是否匿名 | `integer` | - | 是 | - |
| 24 | `isdel` | 是否删除 | `integer` | - | 是 | - |

# 泛微OA 数据表: `docsearchmould`

- **所属模块**: `知识管理`
- **数据库表名**: `docsearchmould`
- **字段总数**: `43`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 查询模板id | `integer` | - | 否 | - |
| 2 | `mouldname` | 查询模板描述 | `varchar2` | 1000 | 是 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | - |
| 4 | `docsubject` | 文档主题 | `varchar2` | 1000 | 是 | - |
| 5 | `doccontent` | 文档内容 | `varchar2` | 1000 | 是 | - |
| 6 | `containreply` | 是否包括回复 | `char` | 1 | 是 | 0:不包括，1:包括 |
| 7 | `maincategory` | 文档主目录 | `integer` | - | 是 | - |
| 8 | `subcategory` | 文档分目录 | `integer` | - | 是 | - |
| 9 | `seccategory` | 文档子目录 | `integer` | - | 是 | - |
| 10 | `docid` | 文档id | `integer` | - | 是 | - |
| 11 | `createrid` | 文档创建者id | `integer` | - | 是 | - |
| 12 | `departmentid` | 文档创建者部门id | `integer` | - | 是 | - |
| 13 | `doclangurage` | 文档语言 | `integer` | - | 是 | - |
| 14 | `hrmresid` | 文档人力资源id | `integer` | - | 是 | - |
| 15 | `itemid` | 物品id | `integer` | - | 是 | - |
| 16 | `itemmaincategoryid` | 物品种类id | `integer` | - | 是 | - |
| 17 | `crmid` | crm id | `integer` | - | 是 | - |
| 18 | `projectid` | 项目id | `integer` | - | 是 | - |
| 19 | `financeid` | 财务-交易id | `integer` | - | 是 | - |
| 20 | `docpublishtype` | 文档发布种类 | `char` | 1 | 是 | - |
| 21 | `docstatus` | 文档状态 | `char` | 1 | 是 | - |
| 22 | `keyword` | 文档关键字 | `varchar2` | 1000 | 是 | - |
| 23 | `ownerid` | 文档所有者 | `integer` | - | 是 | - |
| 24 | `docno` | 文档归档号 | `varchar2` | 480 | 是 | - |
| 25 | `doclastmoddatefrom` | 文档最后修改日期 从 | `char` | 10 | 是 | - |
| 26 | `doclastmoddateto` | 文档最后修改日期 到 | `char` | 10 | 是 | - |
| 27 | `docarchivedatefrom` | 文档归档日期 从 | `char` | 10 | 是 | - |
| 28 | `docarchivedateto` | 归档日期 到 | `char` | 10 | 是 | - |
| 29 | `doccreatedatefrom` | 文档创建日期 从 | `char` | 10 | 是 | - |
| 30 | `doccreatedateto` | 文档创建日期 到 | `char` | 10 | 是 | - |
| 31 | `docapprovedatefrom` | 文档审批日期，从 | `char` | 10 | 是 | - |
| 32 | `docapprovedateto` | 文档审批日期，到 | `char` | 10 | 是 | - |
| 33 | `replaydoccountfrom` | 回复文档总数 从 | `integer` | - | 是 | - |
| 34 | `replaydoccountto` | 回复文档总数 到 | `integer` | - | 是 | - |
| 35 | `accessorycountfrom` | 附件总数 从 | `integer` | - | 是 | - |
| 36 | `accessorycountto` | 附件总数 到 | `integer` | - | 是 | - |
| 37 | `doclastmoduserid` | 文档最后修改者id | `integer` | - | 是 | - |
| 38 | `docarchiveuserid` | 文档归档者id | `integer` | - | 是 | - |
| 39 | `docapproveuserid` | 文档审批者id | `integer` | - | 是 | - |
| 40 | `assetid` | 相关资产id | `integer` | - | 是 | - |
| 41 | `createrid2` | 创建人2 | `integer` | - | 是 | - |
| 42 | `ownerid2` | 所有者2 | `integer` | - | 是 | - |
| 43 | `treedocfieldid` | 体系类别,树状文档字段 | `integer` | - | 是 | - |

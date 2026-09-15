# 泛微OA 数据表: `workflow_createdoc`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_createdoc`
- **字段总数**: `38`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `opentextinformnode` | 打开正文节点 | `varchar2` | 1000 | 是 | - |
| 2 | `istextinform` | 是否展示在表单 | `char` | 1 | 是 | - |
| 3 | `odoctype` | 文档类型 | `integer` | - | 是 | - |
| 4 | `id` | ID | `integer` | - | 否 | - |
| 5 | `workflowid` | 工作流程id | `integer` | - | 是 | - |
| 6 | `status` | 状态 | `char` | 1 | 是 | 1：启用，0：不启用 |
| 7 | `flowcodefield` | 流程编码字段 | `integer` | - | 是 | - |
| 8 | `flowdocfield` | 创建文档字段 | `integer` | - | 是 | - |
| 9 | `flowdoccatfield` | 文件存放目录 | `integer` | - | 是 | - |
| 10 | `defaultview` | 默认显示目录 | `varchar2` | 1000 | 是 | - |
| 11 | `usetempletnode` | 套红节点 | `integer` | - | 是 | - |
| 12 | `documenttitlefield` | 文档标题字段 | `integer` | - | 是 | - |
| 13 | `printnodes` | 打印节点 | `varchar2` | 1000 | 是 | - |
| 14 | `newtextnodes` | 是否只能新建正文 | `varchar2` | 80 | 是 | - |
| 15 | `iscompellentmark` | 是否必须保留痕迹 | `varchar2` | 8 | 是 | - |
| 16 | `iscancelcheck` | 是否取消审阅 | `varchar2` | 8 | 是 | - |
| 17 | `signaturenodes` | 签章节点 | `varchar2` | 1000 | 是 | - |
| 18 | `isworkflowdraft` | 是否存为流程草稿 | `char` | 1 | 是 | 1:是，0或其它为否 |
| 19 | `defaultdoctype` | 默认文档类型 | `char` | 1 | 是 | 1：office word 2：wps文字 |
| 20 | `extfile2doc` | 流程附件是否转为正文附件 | `integer` | - | 是 | 1：转，0：不转 |
| 21 | `ishidethetraces` | 编辑正文时默认隐藏痕迹 | `char` | 1 | 是 | 1:是，0或其它为否 |
| 22 | `wfstatus` | 流程状态 | `integer` | - | 是 | - |
| 23 | `savescriptnode` | 保存脚本节点 | `varchar2` | 1000 | 是 | - |
| 24 | `papersstoragedirectory` | 文档存放目录 | `varchar2` | 800 | 是 | - |
| 25 | `opentextdefaultnode` | 是否默认打开正文 | `varchar2` | 1000 | 是 | - |
| 26 | `savetempfile` | 是否保留正文版本 | `varchar2` | 8 | 是 | - |
| 27 | `cleancopynodes` | 清高节点 | `varchar2` | 1000 | 是 | - |
| 28 | `issuednum` | 文档编号存放字段 | `integer` | - | 是 | - |
| 29 | `topictype` | 主题词字段 | `integer` | - | 是 | - |
| 30 | `urgencydegree` | 紧急程度字段 | `integer` | - | 是 | - |
| 31 | `secretlevel` | 秘密等级字段 | `integer` | - | 是 | - |
| 32 | `useeditmouldnodes` | 编辑模板节点 | `varchar2` | 4000 | 是 | - |
| 33 | `sendunit` | 发文单位 | `integer` | - | 是 | - |
| 34 | `receiveunit` | 收文单位 | `integer` | - | 是 | - |
| 35 | `issueduserid` | 签发人 | `integer` | - | 是 | - |
| 36 | `writtendate` | 写入日期 | `integer` | - | 是 | - |
| 37 | `issueddate` | 发布日期 | `integer` | - | 是 | - |
| 38 | `mustsignaturenodes` | 必须签章节点 | `varchar2` | 4000 | 是 | - |

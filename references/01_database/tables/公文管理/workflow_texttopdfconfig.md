# 泛微OA 数据表: `workflow_texttopdfconfig`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_texttopdfconfig`
- **字段总数**: `19`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 序号 |
| 2 | `workflowid` | 流程id | `integer` | - | 是 | 流程id |
| 3 | `topdfnodeid` | 转换节点id | `integer` | - | 是 | 转换节点id |
| 4 | `pdfsavesecid` | 转成pdf存放固定目录id | `integer` | - | 是 | 转成pdf存放固定目录id |
| 5 | `catalogtype2` | 转成pdf存放目录类型 | `char` | 1 | 是 | 转成pdf存放目录类型 0：固定目录 1：选择目录 |
| 6 | `selectcatalog2` | 转成pdf后存放选择字段id | `integer` | - | 是 | 转成pdf后存放选择字段id |
| 7 | `pdfdocstatus` | 转成pdf后的文档状态 | `integer` | - | 是 | 转成pdf后的文档状态 |
| 8 | `pdffieldid` | 转成pdf后的存放字段 | `integer` | - | 是 | 转成pdf后的存放字段 |
| 9 | `decryptpdfsavesecid` | 转成脱密pdf后的存放目录id | `integer` | - | 是 | 转成脱密pdf后的存放目录id |
| 10 | `decryptcatalogtype2` | 转成脱密pdf后的存放目录类型 | `char` | 1 | 是 | 转成脱密pdf后的存放目录类型 0：固定目录 1：选择目录 |
| 11 | `decryptselectcatalog2` | 转成脱密pdf后的存放选择类型字段id | `integer` | - | 是 | 转成脱密pdf后的存放选择类型字段id |
| 12 | `decryptpdfdocstatus` | 转成脱密pdf后的文档状态 | `integer` | - | 是 | 转成脱密pdf后的文档状态 |
| 13 | `decryptpdffieldid` | 转成脱密pdf后的存放字段id | `integer` | - | 是 | 转成脱密pdf后的存放字段id |
| 14 | `operationtype` | 触发类型 | `integer` | - | 是 | 触发类型 1：提交流程时 0：保存文档时 |
| 15 | `checktype` | 转换类型 | `char` | 10 | 是 | 转换类型 |
| 16 | `filetopdffile` | 流程附件转为pdf副本附件 | `integer` | - | 是 | 流程附件转为pdf副本附件 |
| 17 | `filetopdf` | 正文/流程中的office附件转为pdf格式 | `integer` | - | 是 | 正文/流程中的office附件转为pdf格式 |
| 18 | `filemaxsize` | 转换附件最大值 | `integer` | - | 是 | 转换附件最大值 |
| 19 | `drawbackflag` | 退回时是否触发 | `char` | 1 | 是 | 退回时是否触发 1：触发 0：不触发 |

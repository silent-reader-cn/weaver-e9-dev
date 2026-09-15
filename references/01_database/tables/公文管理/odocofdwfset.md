# 泛微OA 数据表: `odocofdwfset`

- **所属模块**: `公文管理`
- **数据库表名**: `odocofdwfset`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `workflowid` | 工作流编号 | `integer` | - | 是 | - |
| 3 | `convertnodes` | 转换节点 | `varchar2` | 400 | 是 | - |
| 4 | `signaturenodes` | 签章结点 | `varchar2` | 400 | 是 | - |
| 5 | `postilnodes` | 批注节点 | `varchar2` | 400 | 是 | - |
| 6 | `textfieldid` | 正文字段编号 | `integer` | - | 是 | - |
| 7 | `ofdtextfieldid` | OFD字段编号 | `integer` | - | 是 | - |
| 8 | `savesecid` | 保存目录编号 | `integer` | - | 是 | - |
| 9 | `catalogtype2` | 目录类型 | `char` | 1 | 是 | - |
| 10 | `selectcatalog2` | 选择目录 | `integer` | - | 是 | - |
| 11 | `ofddocstatus` | OFD文档状态 | `integer` | - | 是 | - |
| 12 | `isatttoofd` | 是否开启流程附件转为OFD附件 | `char` | 1 | 是 | - |

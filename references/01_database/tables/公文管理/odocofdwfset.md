# 泛微OA 数据表: `odocofdwfset`

- **中文名称**: OFD流程配置表
- **所属模块**: `公文管理`
- **数据库表名**: `odocofdwfset`
- **主键**: `id`
- **字段数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `workflowid` | 工作流编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `convertnodes` | 转换节点 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 4 | `signaturenodes` | 签章结点 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 5 | `postilnodes` | 批注节点 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 6 | `textfieldid` | 正文字段编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `ofdtextfieldid` | OFD字段编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `savesecid` | 保存目录编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `catalogtype2` | 目录类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 10 | `selectcatalog2` | 选择目录 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `ofddocstatus` | OFD文档状态 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `isatttoofd` | 是否开启流程附件转为OFD附件 | `char` | 1 | 是 | 否 | 否 | - | - | - |

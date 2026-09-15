# 泛微OA 数据表: `workflow_communicationcontent`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_communicationcontent`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `communicationid` | 相关交流主表ID | `integer` | - | 是 | workflow_communicationbase |
| 3 | `showremark` | 显示内容 | `varchar2` | 4000 | 是 | - |
| 4 | `quoteremark` | 引用内容 | `varchar2` | 4000 | 是 | - |
| 5 | `myremark` | 我的显示内容 | `varchar2` | 4000 | 是 | - |
| 6 | `createuser` | 创建人 | `integer` | - | 是 | - |
| 7 | `approvenum` | 点赞数 | `integer` | - | 是 | - |
| 8 | `flownum` | 未使用(扩展) | `integer` | - | 是 | - |
| 9 | `createdate` | 创建日期 | `char` | 20 | 是 | - |
| 10 | `createtime` | 创建时间 | `char` | 20 | 是 | - |
| 11 | `quotecontentid` | 引用内容iD | `integer` | - | 是 | workflow_communicationquote |
| 12 | `isdelete` | 是否删除 | `integer` | - | 是 | - |
| 13 | `projectids` | 相关项目 | `varchar2` | 4000 | 是 | - |
| 14 | `relatedacc` | 相关附件 | `varchar2` | 4000 | 是 | - |
| 15 | `relatedcus` | 相关客户 | `varchar2` | 4000 | 是 | - |
| 16 | `relateddoc` | 相关文档 | `varchar2` | 4000 | 是 | - |
| 17 | `relatedprj` | 相关任务 | `varchar2` | 4000 | 是 | - |
| 18 | `relatedwf` | 相关流程 | `varchar2` | 4000 | 是 | - |

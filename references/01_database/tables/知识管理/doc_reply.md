# 泛微OA 数据表: `doc_reply`

- **所属模块**: `知识管理`
- **数据库表名**: `doc_reply`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 回复id | `integer` | - | 否 | - |
| 2 | `docid` | 文档id | `varchar2` | 160 | 否 | - |
| 3 | `userid` | 回复对象 | `varchar2` | 160 | 否 | - |
| 4 | `reply_parentid` | 主回复（根节点回复） | `integer` | - | 否 | - |
| 5 | `content` | 回复内容 | `clob` | 4000 | 否 | - |
| 6 | `ruserid` | 被回复对象 | `varchar2` | 160 | 否 | - |
| 7 | `rtype` | 回复类型 | `integer` | - | 否 | 0：对文档进行回复 1：对文档的回复进行回复 |
| 8 | `replydate` | 回复日期 | `varchar2` | 160 | 否 | - |
| 9 | `replytime` | 回复时间 | `varchar2` | 160 | 否 | - |
| 10 | `orderno` | 回复排序 | `varchar2` | 1000 | 是 | - |
| 11 | `parentid` | 父级回复 | `integer` | - | 是 | - |

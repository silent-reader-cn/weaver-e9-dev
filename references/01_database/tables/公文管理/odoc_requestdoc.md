# 泛微OA 数据表: `odoc_requestdoc`

- **所属模块**: `公文管理`
- **数据库表名**: `odoc_requestdoc`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `requestid` | 请求编号 | `integer` | - | 否 | - |
| 3 | `docid` | 文档编号 | `integer` | - | 是 | - |
| 4 | `officaltype` | 公文过程 | `integer` | - | 是 | - |
| 5 | `odoctype` | 公文种类' | `integer` | - | 是 | - |
| 6 | `topictype` | 主题分类 | `integer` | - | 是 | - |
| 7 | `issued_num` | 文号 | `varchar2` | 1000 | 是 | - |
| 8 | `issued_userid` | 签发人 | `integer` | - | 是 | - |
| 9 | `issued_usertype` | 签发用户类型 | `integer` | - | 是 | - |
| 10 | `issued_date` | 签发日期 | `char` | 10 | 是 | - |
| 11 | `issued_unit` | 发文单位 | `varchar2` | 4000 | 是 | - |
| 12 | `written_date` | 成文日期 | `char` | 10 | 是 | - |
| 13 | `islasttime` | 是否最后一次 | `char` | 1 | 是 | - |

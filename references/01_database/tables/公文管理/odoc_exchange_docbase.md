# 泛微OA 数据表: `odoc_exchange_docbase`

- **所属模块**: `公文管理`
- **数据库表名**: `odoc_exchange_docbase`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `document_identifier` | 公文标识 | `varchar2` | 200 | 否 | - |
| 3 | `document_title` | 公文标题 | `varchar2` | 1000 | 是 | - |
| 4 | `issued_number_of_document` | 发文号 | `varchar2` | 100 | 是 | - |
| 5 | `xmlimagefileid` | xml生成的imagefileid | `integer` | - | 是 | - |
| 6 | `json` | Json数据 | `clob` | 4000 | 是 | - |
| 7 | `docimagefileid` | 正文生成的imagefileid | `integer` | - | 是 | - |
| 8 | `attachimagefileids` | 附件生成的imagefileids | `varchar2` | 500 | 是 | - |
| 9 | `send_companyid` | 发文单位编号 | `integer` | - | 是 | - |
| 10 | `send_date` | 发送日期 | `varchar2` | 10 | 是 | - |
| 11 | `send_time` | 发送时间 | `varchar2` | 10 | 是 | - |
| 12 | `status` | 状态 | `varchar2` | 2 | 是 | - |

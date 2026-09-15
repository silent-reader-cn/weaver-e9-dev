# 泛微OA 数据表: `exchange_receive_doc_info_oa`

- **所属模块**: `公文管理`
- **数据库表名**: `exchange_receive_doc_info_oa`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `receive_date` | 接收日期 | `varchar2` | 10 | 是 | - |
| 2 | `receive_time` | 接收时间 | `varchar2` | 10 | 是 | - |
| 3 | `id` | 编号 | `integer` | - | 否 | - |
| 4 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | - |
| 5 | `document_title` | 公文标题 | `varchar2` | 1000 | 是 | - |
| 6 | `sending_department` | 发送单位 | `varchar2` | 200 | 是 | - |
| 7 | `receive_status` | 接收状态 | `char` | 1 | 是 | - |
| 8 | `main_receiver_department` | 主送单位编号 | `varchar2` | 200 | 是 | - |
| 9 | `requestid` | 请求编号 | `integer` | - | 是 | - |
| 10 | `issued_number_of_document` | 发文号 | `varchar2` | 200 | 是 | - |
| 11 | `document_attachments` | 附件编号 | `varchar2` | 200 | 是 | - |
| 12 | `document_text` | 正文编号 | `integer` | - | 是 | - |
| 13 | `copy_to_department` | 抄送单位 | `varchar2` | 200 | 是 | - |
| 14 | `printing_and_sending_dep` | 印发单位 | `varchar2` | 200 | 是 | - |
| 15 | `json` | json数据 | `clob` | 4000 | 是 | - |

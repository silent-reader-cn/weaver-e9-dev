# 泛微OA 数据表: `exchange_senddocinfo_oa`

- **所属模块**: `公文管理`
- **数据库表名**: `exchange_senddocinfo_oa`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | - |
| 3 | `document_title` | 公文标题 | `varchar2` | 1000 | 是 | - |
| 4 | `send_company_id` | 发文单位编号 | `integer` | - | 是 | - |
| 5 | `request_id` | 请求编号 | `integer` | - | 是 | - |
| 6 | `document_type` | 公文类型 | `char` | 2 | 是 | - |
| 7 | `create_date` | 创建日期 | `varchar2` | 10 | 是 | - |
| 8 | `create_time` | 创建时间 | `varchar2` | 10 | 是 | - |
| 9 | `sub_request_id` | 自请求编号 | `integer` | - | 是 | - |
| 10 | `issued_number_of_document` | 发文号 | `varchar2` | 100 | 是 | - |
| 11 | `send_status` | 发送状态 | `char` | 1 | 是 | - |

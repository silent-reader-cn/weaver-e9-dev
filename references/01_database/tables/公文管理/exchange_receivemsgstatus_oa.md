# 泛微OA 数据表: `exchange_receivemsgstatus_oa`

- **所属模块**: `公文管理`
- **数据库表名**: `exchange_receivemsgstatus_oa`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `receive_doc_info_oa_id` | 收文信息编号 | `integer` | - | 是 | - |
| 2 | `id` | 编号 | `integer` | - | 否 | - |
| 3 | `operator` | 操作人编号 | `integer` | - | 是 | - |
| 4 | `operate_date` | 操作日期 | `varchar2` | 10 | 是 | - |
| 5 | `operate_time` | 操作时间 | `varchar2` | 10 | 是 | - |
| 6 | `operate_status` | 操作状态 | `char` | 1 | 是 | - |
| 7 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | - |
| 8 | `receiver_department` | 收文单位编号 | `varchar2` | 200 | 是 | - |
| 9 | `note` | 备注 | `varchar2` | 2000 | 是 | - |
| 10 | `sending_department` | 发送单位编号 | `varchar2` | 200 | 是 | - |

# 泛微OA 数据表: `exchange_receivemsgstatus_oa`

- **中文名称**: 接入系统-收文状态表
- **所属模块**: `公文管理`
- **数据库表名**: `exchange_receivemsgstatus_oa`
- **主键**: `id`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `receive_doc_info_oa_id` | 收文信息编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `operator` | 操作人编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `operate_date` | 操作日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 5 | `operate_time` | 操作时间 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 6 | `operate_status` | 操作状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 7 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 8 | `receiver_department` | 收文单位编号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 9 | `note` | 备注 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | - |
| 10 | `sending_department` | 发送单位编号 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |

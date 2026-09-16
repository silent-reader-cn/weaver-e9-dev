# 泛微OA 数据表: `exchange_receiveunitlist_oa`

- **中文名称**: 接入系统-收文单位信息表
- **所属模块**: `公文管理`
- **数据库表名**: `exchange_receiveunitlist_oa`
- **主键**: `id`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `oper_date` | 操作日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 2 | `oper_time` | 操作时间 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 3 | `type` | 类型 | `varchar2` | 1 | 是 | 否 | 否 | - | 0 | - |
| 4 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 6 | `receive_company_id` | 接收单位编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `doc_status` | 文档状态 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `oper_status` | 操作状态 | `char` | 2 | 是 | 否 | 否 | - | - | - |
| 9 | `response_msg` | 反馈信息 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |

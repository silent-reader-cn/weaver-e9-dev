# 泛微OA 数据表: `odoc_exchange_recieveinfo`

- **中文名称**: 交换平台-收文信息表
- **所属模块**: `公文管理`
- **数据库表名**: `odoc_exchange_recieveinfo`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `is_received` | 是否已经接收 | `varchar2` | 1 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 编号 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `document_identifier` | 公文标识 | `varchar2` | 200 | 是 | 否 | 否 | - | - | - |
| 4 | `receive_companyid` | 接收单位编号 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `xml_imagefileid` | 收到xml生成的imagefileid | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `status` | 状态 | `varchar2` | 2 | 是 | 否 | 否 | - | - | - |

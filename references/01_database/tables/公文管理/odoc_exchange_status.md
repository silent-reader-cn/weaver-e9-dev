# 泛微OA 数据表: `odoc_exchange_status`

- **所属模块**: `公文管理`
- **数据库表名**: `odoc_exchange_status`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `note` | 备注 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | 编号 | `integer` | - | 否 | - |
| 3 | `receiveid` | 收文单位编号 | `integer` | - | 是 | - |
| 4 | `operator` | 操作人编号 | `varchar2` | 200 | 是 | - |
| 5 | `operate_date` | 操作日期 | `varchar2` | 10 | 是 | - |
| 6 | `operate_time` | 操作时间 | `varchar2` | 10 | 是 | - |
| 7 | `status` | 状态 | `varchar2` | 2 | 是 | - |
| 8 | `is_received_status` | 是否已经接收 | `char` | 1 | 是 | - |
| 9 | `is_current_status` | 是否当前状态 | `char` | 1 | 是 | - |

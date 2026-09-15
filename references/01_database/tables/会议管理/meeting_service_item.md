# 泛微OA 数据表: `meeting_service_item`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_service_item`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `hrmids` | 负责人 | `varchar2` | 1000 | 是 | - |
| 2 | `id` | ID | `integer` | - | 否 | - |
| 3 | `type` | 服务类型id | `integer` | - | 是 | - |
| 4 | `itemname` | 服务项目名称 | `varchar2` | 1000 | 是 | - |

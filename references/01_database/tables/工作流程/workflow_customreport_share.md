# 泛微OA 数据表: `workflow_customreport_share`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customreport_share`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `reportid` | 报表ID | `integer` | - | 否 | - |
| 3 | `sharetype` | 共享类型 | `char` | 1 | 是 | - |
| 4 | `sharedobj` | 共享类型对象ID | `varchar2` | 1000 | 是 | - |
| 5 | `seclevel` | 安全级别最小值 | `char` | 4 | 是 | - |
| 6 | `seclevelmax` | 安全级别最大值 | `char` | 4 | 是 | - |
| 7 | `sharelevel` | 共享级别 | `char` | 1 | 是 | - |

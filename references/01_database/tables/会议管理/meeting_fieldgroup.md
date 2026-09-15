# 泛微OA 数据表: `meeting_fieldgroup`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_fieldgroup`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | 0 | 否 | 主键 |
| 2 | `grouplabel` | 分组标签id,支持国际化 | `integer` | 0 | 是 | 分组标签id,支持国际化 |
| 3 | `grouporder` | 组排序 | `integer` | 0 | 是 | 组排序 |
| 4 | `grouptype` | 分组类型 | `integer` | 0 | 是 | 和meeting_defined中的scopeid 对应 |
| 5 | `isshow` | 是否显示 | `integer` | 0 | 否 | 是否显示 ；1：显示 |

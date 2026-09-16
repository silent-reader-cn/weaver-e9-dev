# 泛微OA 数据表: `meeting_fieldgroup`

- **中文名称**: 会议卡片分组
- **所属模块**: `会议管理`
- **数据库表名**: `meeting_fieldgroup`
- **主键**: `id`
- **字段数**: `5`

> 说明：会议卡片分组信息

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | 0 | 否 | 否 | 否 | - | - | 主键 |
| 2 | `grouplabel` | 分组标签id,支持国际化 | `integer` | 0 | 是 | 否 | 否 | - | - | 分组标签id,支持国际化 |
| 3 | `grouporder` | 组排序 | `integer` | 0 | 是 | 否 | 否 | - | - | 组排序 |
| 4 | `grouptype` | 分组类型 | `integer` | 0 | 是 | 是 | 否 | meeting_defined的scopeid | - | 和meeting_defined中的scopeid 对应 |
| 5 | `isshow` | 是否显示 | `integer` | 0 | 否 | 否 | 否 | - | 1 | 是否显示 ；1：显示 |

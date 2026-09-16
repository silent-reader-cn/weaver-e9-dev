# 泛微OA 数据表: `workflow_customreport_field`

- **中文名称**: 报表分析字段
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_customreport_field`
- **主键**: `reportid + fieldid`
- **字段数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `reportid` | 报表ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `fieldid` | 字段ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `tablename` | 字段所属表名 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 4 | `isdetail` | 是否明细字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 5 | `isshow` | 是否显示 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 6 | `showorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 7 | `colwidth` | 未使用 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 8 | `isgroup` | 是否查询分组字段 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `sortby` | 排序方式 | `char` | 2 | 是 | 否 | 否 | - | - | - |
| 10 | `sortorder` | 排序顺序 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `workflow_fielddata_cache`

- **中文名称**: 流程自定义浏览框数据缓存表
- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fielddata_cache`
- **主键**: `id`
- **字段数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `requestid` | 请求ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `fieldid` | 字段ID | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 4 | `detailid` | 明细ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 5 | `fieldvalue` | 字段值 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `fieldvalueshowname` | 字段中中文串 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

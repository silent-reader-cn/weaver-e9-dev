# 泛微OA 数据表: `workflow_fielddata_cache`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_fielddata_cache`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `requestid` | 请求ID | `integer` | - | 否 | - |
| 3 | `fieldid` | 字段ID | `varchar2` | 800 | 否 | - |
| 4 | `detailid` | 明细ID | `integer` | - | 是 | - |
| 5 | `fieldvalue` | 字段值 | `varchar2` | 1000 | 是 | - |
| 6 | `fieldvalueshowname` | 字段中中文串 | `varchar2` | 4000 | 是 | - |

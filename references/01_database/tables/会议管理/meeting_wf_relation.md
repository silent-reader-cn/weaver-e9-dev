# 泛微OA 数据表: `meeting_wf_relation`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_wf_relation`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `defined` | meeting_defind表中的scopeid | `integer` | - | 是 | - |
| 2 | `fieldid` | 会议卡片字段id | `integer` | - | 是 | - |
| 3 | `fieldname` | 会议卡片字段名称 | `varchar2` | 240 | 是 | - |
| 4 | `billid` | 会议表单id, formid | `integer` | - | 是 | - |
| 5 | `bill_fieldname` | 流程表单中对应的字段名称 | `varchar2` | 480 | 是 | - |

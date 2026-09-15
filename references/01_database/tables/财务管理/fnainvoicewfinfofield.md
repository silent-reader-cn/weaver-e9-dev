# 泛微OA 数据表: `fnainvoicewfinfofield`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoicewfinfofield`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 2 | `fieldname` | 字段数据库名 | `varchar2` | 112 | 是 | - |
| 3 | `tabindex` | 页签顺序 | `integer` | - | 是 | - |
| 4 | `dtlnumber` | 明细表id | `integer` | - | 是 | - |
| 5 | `isdtl` | 是否是明细表 | `integer` | - | 是 | 0.明细表 1.主表 |
| 6 | `id` | 主键 | `integer` | - | 否 | - |
| 7 | `mainid` | 票据流程定义表ID | `integer` | - | 是 | 对应FnaInvoiceWfInfo表的id |
| 8 | `workflowid` | 流程id | `integer` | - | 是 | - |
| 9 | `formid` | 表单id | `integer` | - | 是 | - |

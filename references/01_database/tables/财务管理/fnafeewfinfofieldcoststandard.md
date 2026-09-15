# 泛微OA 数据表: `fnafeewfinfofieldcoststandard`

- **所属模块**: `财务管理`
- **数据库表名**: `fnafeewfinfofieldcoststandard`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `mainid` | fnafeewfinfocoststandard.id | `integer` | - | 是 | - |
| 3 | `workflowid` | wfid | `integer` | - | 是 | - |
| 4 | `formid` | 表单id | `integer` | - | 是 | - |
| 5 | `fieldtype` | 字段类型 | `integer` | - | 是 | - |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 7 | `fcsguid1` | 费用标准uuid | `char` | 32 | 是 | - |
| 8 | `tabindex` | 主表、明细表序号 | `integer` | - | 是 | - |
| 9 | `showalltype` | 是否显示全部字段 | `integer` | - | 是 | - |
| 10 | `dtlnumber` | 明细表序号 | `integer` | - | 是 | - |
| 11 | `fieldvalue` | 字段值 | `varchar2` | 4000 | 是 | - |
| 12 | `fieldvaltype` | 字段值类型 | `integer` | - | 是 | - |
| 13 | `fieldvaluewfsys` | 字段系统默认值 | `integer` | - | 是 | - |
| 14 | `iswffieldlinkage` | （作废） | `integer` | - | 是 | - |
| 15 | `isdtl` | 是否是明细表字段 | `integer` | - | 是 | - |

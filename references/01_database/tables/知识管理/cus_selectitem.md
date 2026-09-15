# 泛微OA 数据表: `cus_selectitem`

- **所属模块**: `知识管理`
- **数据库表名**: `cus_selectitem`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `hrm_isdefault` | 默认 | `char` | 1 | 是 | - |
| 2 | `fieldid` | 字段id | `integer` | - | 否 | - |
| 3 | `selectvalue` | 下拉框选项值 | `integer` | - | 否 | - |
| 4 | `selectname` | 下拉框选项显示名称 | `varchar2` | 1000 | 是 | - |
| 5 | `fieldorder` | 选项显示顺序 | `integer` | - | 否 | - |
| 6 | `doc_isdefault` | 是否默认_文档专用 | `integer` | - | 是 | - |
| 7 | `cancel` | 是否作废 | `integer` | - | 是 | - |
| 8 | `prj_isdefault` | 是否默认_项目专用 | `char` | 1 | 是 | - |

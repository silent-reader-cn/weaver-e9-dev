# 泛微OA 数据表: `hrm_rp_sub_template_con`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_rp_sub_template_con`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `template_id` | 模板id | `integer` | - | 否 | hrm_rp_sub_template表的 id值 |
| 3 | `col_name` | 字段名称 | `varchar2` | 400 | 是 | 字段名称 |
| 4 | `con_htmltype` | 组件类型 | `varchar2` | 400 | 是 | 组件类型 |
| 5 | `con_type` | 分类 | `varchar2` | 400 | 是 | 分类 |
| 6 | `con_opt` | 条件1 | `varchar2` | 400 | 是 | 条件1 |
| 7 | `con_value` | 值1 | `varchar2` | 400 | 是 | 值1 |
| 8 | `con_opt1` | 条件2 | `varchar2` | 400 | 是 | 条件2 |
| 9 | `con_value1` | 值2 | `varchar2` | 400 | 是 | 值2 |

# 泛微OA 数据表: `hrm_rp_sub_template`

- **所属模块**: `人力资源`
- **数据库表名**: `hrm_rp_sub_template`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `name` | 模板名称 | `varchar2` | 1000 | 是 | 模板名称 |
| 3 | `author` | 创建人id | `integer` | - | 否 | 创建人id |
| 4 | `create_date` | 创建时间 | `timestamp(6)` | 11 | 否 | 创建时间 |
| 5 | `scope` | 使用范围 | `varchar2` | 1000 | 是 | 使用范围 |
| 6 | `delflag` | 是否删除 | `integer` | - | 否 | 0是默认，1是删除 |

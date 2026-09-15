# 泛微OA 数据表: `crm_selectitem`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_selectitem`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `fieldid` | 字段ID | `integer` | - | 否 | 字段ID |
| 2 | `selectvalue` | 选项值 | `integer` | - | 否 | 选项值 |
| 3 | `selectname` | 选项名称 | `varchar2` | 1000 | 是 | 选项名称 |
| 4 | `fieldorder` | 选项排序 | `integer` | - | 否 | 选项排序 |
| 5 | `isdel` | 是否删除 | `integer` | - | 是 | 0：未删除 |

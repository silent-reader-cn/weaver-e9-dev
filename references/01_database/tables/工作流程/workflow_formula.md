# 泛微OA 数据表: `workflow_formula`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formula`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `desclabel` | 多语言描述信息 | `varchar2` | 1000 | 是 | 函数的描述信息，多语言字段，如果为空则取description中的信息 |
| 2 | `description` | 描述信息 | `varchar2` | 4000 | 是 | 描述信息 |
| 3 | `filename` | 自定义函数文件名 | `varchar2` | 1000 | 是 | 自定义函数的函数内容存储在js文件中，此字段为所在js文件的文件名 |
| 4 | `showorder` | 显示顺序 | `integer` | 100 | 是 | 显示顺序 |
| 5 | `id` | 主键编码 | `integer` | 100 | 否 | 主键字段 |
| 6 | `name` | 函数名称 | `varchar2` | 1000 | 是 | 函数名称，使用函数时使用此名称 |
| 7 | `type` | 函数类型 | `integer` | 100 | 是 | 函数类型，对应workflow_formula_type表中的id字段 |
| 8 | `isdef` | 是否是自定义函数 | `integer` | 1 | 是 | 0：不是自定义函数，1：是自定义函数 |

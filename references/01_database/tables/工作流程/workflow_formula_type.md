# 泛微OA 数据表: `workflow_formula_type`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formula_type`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键编码 | `integer` | 100 | 是 | 主键 |
| 2 | `languageid` | 多语言描述信息 | `integer` | 100 | 是 | 函数描述的多语言字段信息 |
| 3 | `description` | 描述信息 | `varchar2` | 1000 | 是 | 描述信息 |
| 4 | `showorder` | 显示顺序 | `integer` | 100 | 是 | 函数类型的显示顺序 |

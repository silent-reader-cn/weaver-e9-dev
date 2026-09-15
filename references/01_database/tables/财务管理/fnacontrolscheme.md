# 泛微OA 数据表: `fnacontrolscheme`

- **所属模块**: `财务管理`
- **数据库表名**: `fnacontrolscheme`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `name` | 方案名称 | `char` | 60 | 是 | - |
| 3 | `code` | 方案编码 | `char` | 60 | 是 | - |
| 4 | `fnayearid` | 预算年度开始 | `integer` | - | 是 | - |
| 5 | `fnayearidend` | 预算年度结束 | `integer` | - | 是 | 无表示使用有效 |
| 6 | `enabled` | 启用方案 | `integer` | - | 是 | 1：启用；其他：不启用； |

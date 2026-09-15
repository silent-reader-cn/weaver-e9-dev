# 泛微OA 数据表: `workflow_formula_db`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_formula_db`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键编码 | `integer` | 100 | 是 | 自增长主键 |
| 2 | `name` | 函数名 | `varchar2` | 1000 | 是 | 函数名称 |
| 3 | `desclabel` | 多语言描述信息 | `varchar2` | 1000 | 是 | 函数的描述信息，多语言字段，如果为空则取description中的信息 |
| 4 | `description` | 描述信息 | `varchar2` | 4000 | 是 | 函数的描述信息 |
| 5 | `sqlfororacle` | oracle数据库中的sql语句 | `clob` | 4000 | 是 | 函数对应的oracle数据库中的sql语句 |
| 6 | `sqlforsqlserver` | sqlserver数据库中的sql语句 | `clob` | 4000 | 是 | 函数对应的sqlserver数据库中的sql语句 |
| 7 | `sqlformysql` | mysql数据库中的sql语句 | `clob` | 4000 | 是 | 函数对应的mysql数据库中的sql语句 |
| 8 | `paramcount` | 参数个数 | `integer` | 100 | 是 | 函数的参数个数 |
| 9 | `resulttype` | 返回结果类型 | `varchar2` | 1000 | 是 | 函数的返回结果类型 |
| 10 | `showorder` | 显示顺序 | `integer` | 100 | 是 | 函数的显示顺序 |

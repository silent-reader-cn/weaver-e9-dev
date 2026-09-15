# 泛微OA 数据表: `cptcodeset`

- **所属模块**: `资产管理`
- **数据库表名**: `cptcodeset`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `codeid` | 资产编码配置id | `integer` | - | 是 | 资产编码配置id |
| 3 | `showname` | 显示名 | `varchar2` | 80 | 是 | 显示名 |
| 4 | `showtype` | 显示类型 | `integer` | - | 是 | 显示类型 |
| 5 | `value` | 值 | `varchar2` | 800 | 是 | 值 |
| 6 | `codeorder` | 顺序 | `integer` | - | 是 | 顺序 |

# 泛微OA 数据表: `wsregistemethod`

- **所属模块**: `集成模块`
- **数据库表名**: `wsregistemethod`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 自增长主键 | `integer` | - | 否 | 自增长主键 |
| 2 | `mainid` | 接口主键id | `integer` | - | 是 | 关联wsregiste信息表id |
| 3 | `methodname` | 方法名称 | `varchar2` | 1000 | 是 | 方法名称 |
| 4 | `methoddesc` | 方法描述 | `varchar2` | 1000 | 是 | 方法描述 |
| 5 | `methodreturntype` | 方法返回类型 | `varchar2` | 1000 | 是 | 方法返回类型 |

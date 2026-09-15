# 泛微OA 数据表: `esb_route`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_route`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布服务标识 | `varchar2` | 800 | 是 | - |
| 2 | `routeid` | 路由标识 | `varchar2` | 800 | 是 | - |
| 3 | `serviceid` | 服务标识 | `varchar2` | 800 | 是 | - |
| 4 | `runlevel` | 运行级别 | `integer` | - | 是 | - |
| 5 | `description` | 说明 | `clob` | 4000 | 是 | - |
| 6 | `async` | 是否异步执行 | `integer` | - | 是 | 1:是，0:否 |

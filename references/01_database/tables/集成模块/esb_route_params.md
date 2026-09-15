# 泛微OA 数据表: `esb_route_params`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_route_params`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布服务标识 | `varchar2` | 800 | 是 | - |
| 2 | `routeid` | 路由标识 | `varchar2` | 800 | 是 | - |
| 3 | `serviceid` | 服务标识 | `varchar2` | 800 | 是 | - |
| 4 | `paramkey` | 参数标识 | `varchar2` | 1000 | 是 | - |
| 5 | `assigntype` | 赋值类型 | `varchar2` | 800 | 是 | 1:调用时传递，2:固定值，3_routeid:路由返回值 |
| 6 | `assignvalue` | 赋值内容 | `varchar2` | 1000 | 是 | - |
| 7 | `transmittype` | 参数类型 | `varchar2` | 800 | 是 | - |
| 8 | `showname` | 显示名称 | `varchar2` | 800 | 是 | - |
| 9 | `ext` | 扩展字段 | `varchar2` | 1000 | 是 | - |

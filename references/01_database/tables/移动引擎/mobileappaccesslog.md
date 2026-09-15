# 泛微OA 数据表: `mobileappaccesslog`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobileappaccesslog`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `varchar2` | 50 | 否 | - |
| 2 | `node` | 节点 | `varchar2` | 400 | 是 | 节点 |
| 3 | `userid` | 用户ID | `integer` | - | 是 | 用户ID |
| 4 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | 创建日期 |
| 5 | `ip` | IP | `varchar2` | 1000 | 是 | IP |
| 6 | `os` | 操作平台 | `varchar2` | 400 | 是 | 操作平台 |
| 7 | `client` | 终端 | `varchar2` | 400 | 是 | 终端 |
| 8 | `appid` | 应用ID | `integer` | - | 是 | 应用ID |
| 9 | `createtime` | 创建时间 | `varchar2` | 400 | 是 | 创建时间 |

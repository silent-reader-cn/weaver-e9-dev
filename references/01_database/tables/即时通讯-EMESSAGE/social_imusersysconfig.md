# 泛微OA 数据表: `social_imusersysconfig`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imusersysconfig`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 3 | `winconfig` | windows客户端设置 | `varchar2` | 1000 | 是 | windows客户端设置 |
| 4 | `osxconfig` | macOs客户端配置 | `varchar2` | 1000 | 是 | macOs客户端配置 |
| 5 | `webandpcconfig` | web和pc端公共配置 | `varchar2` | 1000 | 是 | web和pc端公共配置 |

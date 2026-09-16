# 泛微OA 数据表: `social_imusersysconfig`

- **中文名称**: emessage用户设置配置
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_imusersysconfig`
- **主键**: `id`
- **字段数**: `5`

> 说明：emessage每个用户的个人配置

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | 主键id |
| 2 | `userid` | 用户id | `integer` | - | 是 | 否 | 否 | - | - | 用户id |
| 3 | `winconfig` | windows客户端设置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | windows客户端设置 |
| 4 | `osxconfig` | macOs客户端配置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | macOs客户端配置 |
| 5 | `webandpcconfig` | web和pc端公共配置 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | web和pc端公共配置 |

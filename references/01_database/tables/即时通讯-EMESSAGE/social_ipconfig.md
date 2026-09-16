# 泛微OA 数据表: `social_ipconfig`

- **中文名称**: ip映射表
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_ipconfig`
- **主键**: `id`
- **字段数**: `3`

> 说明：oa地址对应的message IP地址对应

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `raw` | 16 | 否 | 否 | 否 | - | sys_guid() | 主键id |
| 2 | `oahost` | oaip | `varchar2` | 255 | 否 | 否 | 否 | - | - | oaip |
| 3 | `emhost` | message ip | `varchar2` | 1000 | 是 | 否 | 否 | - | - | message ip |

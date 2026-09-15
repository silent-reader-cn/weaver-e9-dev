# 泛微OA 数据表: `social_ipconfig`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_ipconfig`
- **字段总数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `raw` | 16 | 否 | 主键id |
| 2 | `oahost` | oaip | `varchar2` | 255 | 否 | oaip |
| 3 | `emhost` | message ip | `varchar2` | 1000 | 是 | message ip |

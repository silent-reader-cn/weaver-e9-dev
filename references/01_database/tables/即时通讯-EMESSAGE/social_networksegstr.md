# 泛微OA 数据表: `social_networksegstr`

- **中文名称**: emessage网段策略表
- **所属模块**: `即时通讯/EMESSAGE`
- **数据库表名**: `social_networksegstr`
- **主键**: `id`
- **字段数**: `8`

> 说明：emessage的网段策略存储表

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 否 | 否 | - | - | 主键id |
| 2 | `inceptipaddress` | 起始ip | `varchar2` | 1000 | 否 | 否 | 否 | - | - | 起始ip地址 |
| 3 | `endipaddress` | 结束ip | `varchar2` | 1000 | 否 | 否 | 否 | - | - | 结束ip地址 |
| 4 | `createrid` | 创建者 | `integer` | - | 是 | 否 | 否 | - | - | 创建者id |
| 5 | `createdate` | 创建日期 | `varchar2` | 100 | 是 | 否 | 否 | - | - | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 100 | 是 | 否 | 否 | - | - | 创建时间 |
| 7 | `segmentdesc` | 网段说明 | `varchar2` | 1000 | 否 | 否 | 否 | - | - | 网段文字说明 |
| 8 | `isforbitlogin` | 是否禁止登录 | `integer` | - | 否 | 否 | 否 | - | - | 1代表禁止登录，0代表允许登录 |

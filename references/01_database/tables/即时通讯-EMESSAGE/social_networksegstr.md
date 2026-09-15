# 泛微OA 数据表: `social_networksegstr`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_networksegstr`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `inceptipaddress` | 起始ip | `varchar2` | 1000 | 否 | 起始ip地址 |
| 3 | `endipaddress` | 结束ip | `varchar2` | 1000 | 否 | 结束ip地址 |
| 4 | `createrid` | 创建者 | `integer` | - | 是 | 创建者id |
| 5 | `createdate` | 创建日期 | `varchar2` | 100 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 100 | 是 | 创建时间 |
| 7 | `segmentdesc` | 网段说明 | `varchar2` | 1000 | 否 | 网段文字说明 |
| 8 | `isforbitlogin` | 是否禁止登录 | `integer` | - | 否 | 1代表禁止登录，0代表允许登录 |

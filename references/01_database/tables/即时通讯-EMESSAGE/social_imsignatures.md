# 泛微OA 数据表: `social_imsignatures`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imsignatures`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `userid` | 用户id | `varchar2` | 800 | 是 | 用户id |
| 3 | `signatures` | 签名内容 | `varchar2` | 1000 | 是 | 签名内容 |
| 4 | `signdate` | 签名时间 | `varchar2` | 800 | 是 | 签名时间 |

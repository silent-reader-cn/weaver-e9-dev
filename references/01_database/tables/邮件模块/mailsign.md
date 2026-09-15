# 泛微OA 数据表: `mailsign`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailsign`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `userid` | 人员id | `integer` | - | 是 | - |
| 3 | `signname` | 签名名称 | `varchar2` | 800 | 是 | - |
| 4 | `signdesc` | 签名描述 | `varchar2` | 1000 | 是 | - |
| 5 | `signcontent` | 签名内容 | `varchar2` | 4000 | 是 | - |
| 6 | `isactive` | 是否使用此签名 | `integer` | - | 是 | - |
| 7 | `signtype` | 签名类型 | `integer` | - | 是 | 0：文本签名，1：电子签名 |

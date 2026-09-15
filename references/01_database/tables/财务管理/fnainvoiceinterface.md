# 泛微OA 数据表: `fnainvoiceinterface`

- **所属模块**: `财务管理`
- **数据库表名**: `fnainvoiceinterface`
- **字段总数**: `16`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `tokenurl` | 获取token的接口地址 | `varchar2` | 1000 | 是 | - |
| 2 | `openidurl` | 获取openid的接口地址 | `varchar2` | 1000 | 是 | - |
| 3 | `client_id` | 企业client_id | `varchar2` | 1000 | 是 | - |
| 4 | `client_secret` | client_id密钥 | `clob` | 4000 | 是 | - |
| 5 | `sqm` | 企业授权码 | `clob` | 4000 | 是 | - |
| 6 | `client` | 企业名称 | `varchar2` | 1000 | 是 | - |
| 7 | `gtaxid` | 企业纳税人识别号 | `varchar2` | 1000 | 是 | - |
| 8 | `interfacetype` | 接口详细类型 | `integer` | - | 是 | - |
| 9 | `username` | 用户名 | `varchar2` | 400 | 是 | - |
| 10 | `password` | 密码 | `clob` | 4000 | 是 | - |
| 11 | `lastmodify` | 最后修改时间 | `varchar2` | 160 | 是 | - |
| 12 | `weightpercent` | 置信度 | `number` | (18,2) | 是 | - |
| 13 | `id` | 主键 | `integer` | - | 否 | - |
| 14 | `type` | 接口类型 | `integer` | - | 是 | - |
| 15 | `interfaceurl` | 接口地址 | `varchar2` | 1000 | 是 | - |
| 16 | `status` | 接口状态 | `integer` | - | 是 | - |

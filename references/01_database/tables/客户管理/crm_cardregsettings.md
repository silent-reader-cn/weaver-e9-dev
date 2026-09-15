# 泛微OA 数据表: `crm_cardregsettings`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_cardregsettings`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `isopen` | 是否开启 | `integer` | - | 是 | 1:开启 |
| 3 | `url` | 接口地址 | `varchar2` | 1000 | 是 | 接口地址 |
| 4 | `loginid` | 账号 | `varchar2` | 400 | 是 | 账号 |
| 5 | `password` | 密码 | `varchar2` | 400 | 是 | 密码 |
| 6 | `modifydate` | 更改日期 | `varchar2` | 400 | 是 | 更改日期 |
| 7 | `modifytime` | 更改时间 | `varchar2` | 400 | 是 | 更改时间 |
| 8 | `modifyuser` | 更改人 | `varchar2` | 80 | 是 | 更改人 |

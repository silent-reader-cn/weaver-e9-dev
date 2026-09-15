# 泛微OA 数据表: `crm_customeraddress`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_customeraddress`
- **字段总数**: `44`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `dhwb1` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 2 | `zdy1` | 未知 | `varchar2` | 1000 | 是 | 未知 |
| 3 | `zdy2` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 4 | `c1` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 5 | `c2` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 6 | `c3` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 7 | `dhwb2` | 未知 | `varchar2` | 4000 | 是 | 未知 |
| 8 | `chck1` | 未知 | `char` | 1 | 是 | 未知 |
| 9 | `typeid` | 类型id | `integer` | - | 否 | 类型id |
| 10 | `customerid` | 客户di | `integer` | - | 否 | 客户id |
| 11 | `isequal` | 是否等于客户信息中的地址 | `integer` | - | 是 | 是否等于客户信息中的地址 |
| 12 | `address1` | 地址 | `varchar2` | 1000 | 是 | 地址 |
| 13 | `address2` | 地址 | `varchar2` | 1000 | 是 | 地址 |
| 14 | `address3` | 地址 | `varchar2` | 1000 | 是 | 地址 |
| 15 | `zipcode` | 邮编 | `varchar2` | 80 | 是 | 邮编 |
| 16 | `city` | 市 | `integer` | - | 是 | 市 |
| 17 | `country` | 国家 | `integer` | - | 是 | 国家 |
| 18 | `province` | 省 | `integer` | - | 是 | 省 |
| 19 | `county` | 县 | `varchar2` | 400 | 是 | 县 |
| 20 | `phone` | 电话 | `varchar2` | 400 | 是 | 电话 |
| 21 | `fax` | 传真 | `varchar2` | 400 | 是 | 传真 |
| 22 | `email` | 邮箱 | `varchar2` | 1000 | 是 | 邮箱 |
| 23 | `contacter` | 客户联系人id | `integer` | - | 是 | 客户联系人id |
| 24 | `datefield1` | 自定义日期 | `varchar2` | 80 | 是 | 自定义日期 |
| 25 | `datefield2` | 自定义日期 | `varchar2` | 80 | 是 | 自定义日期 |
| 26 | `datefield3` | 自定义日期 | `varchar2` | 80 | 是 | 自定义日期 |
| 27 | `datefield4` | 自定义日期 | `varchar2` | 80 | 是 | 自定义日期 |
| 28 | `datefield5` | 自定义日期 | `varchar2` | 80 | 是 | 自定义日期 |
| 29 | `numberfield1` | 自定义数值 | `float` | 22 | 是 | 自定义数值 |
| 30 | `numberfield2` | 自定义数值 | `float` | 22 | 是 | 自定义数值 |
| 31 | `numberfield3` | 自定义数值 | `float` | 22 | 是 | 自定义数值 |
| 32 | `numberfield4` | 自定义数值 | `float` | 22 | 是 | 自定义数值 |
| 33 | `numberfield5` | 自定义数值 | `float` | 22 | 是 | 自定义数值 |
| 34 | `textfield2` | 自定义文本 | `varchar2` | 800 | 是 | 自定义文本 |
| 35 | `textfield3` | 自定义文本 | `varchar2` | 800 | 是 | 自定义文本 |
| 36 | `textfield4` | 自定义文本 | `varchar2` | 800 | 是 | 自定义文本 |
| 37 | `textfield5` | 自定义文本 | `varchar2` | 800 | 是 | 自定义文本 |
| 38 | `tinyintfield1` | 自定义判断 | `integer` | - | 是 | 自定义判断 |
| 39 | `tinyintfield2` | 自定义判断 | `integer` | - | 是 | 自定义判断 |
| 40 | `tinyintfield3` | 自定义判断 | `integer` | - | 是 | 自定义判断 |
| 41 | `tinyintfield4` | 自定义判断 | `integer` | - | 是 | 自定义判断 |
| 42 | `tinyintfield5` | 自定义判断 | `integer` | - | 是 | 自定义判断 |
| 43 | `id` | id | `integer` | - | 否 | id |
| 44 | `district` | 区id | `integer` | - | 是 | 区id |

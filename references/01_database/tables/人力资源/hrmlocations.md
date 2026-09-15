# 泛微OA 数据表: `hrmlocations`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmlocations`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `locationname` | 地址信息名称 | `varchar2` | 1000 | 是 | 地址信息名称 |
| 3 | `locationdesc` | 地址信息描述 | `varchar2` | 1000 | 是 | 地址信息描述 |
| 4 | `address1` | 地址1 | `varchar2` | 1000 | 是 | 地址1 |
| 5 | `address2` | 地址2 | `varchar2` | 1000 | 是 | 地址2 |
| 6 | `locationcity` | 所在城市 | `varchar2` | 1000 | 是 | 所在城市 |
| 7 | `postcode` | 邮编 | `varchar2` | 160 | 是 | 邮编 |
| 8 | `countryid` | 所在国家id | `integer` | - | 否 | 所在国家id |
| 9 | `telephone` | 电话 | `varchar2` | 480 | 是 | 电话 |
| 10 | `fax` | 传真 | `varchar2` | 480 | 是 | 传真 |
| 11 | `showorder` | 顺序 | `number` | (15,2) | 是 | 顺序 |

# 泛微OA 数据表: `hrmnetworksegstr`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmnetworksegstr`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `inceptipaddress` | 起始ip地址 | `varchar2` | 1000 | 是 | 起始ip地址 |
| 3 | `endipaddress` | 截止ip地址 | `varchar2` | 1000 | 是 | 截止ip地址 |
| 4 | `createrid` | 创建人id | `integer` | - | 是 | 创建人id |
| 5 | `createdate` | 创建日期 | `char` | 20 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `char` | 20 | 是 | 创建时间 |
| 7 | `segmentdesc` | 网段说明 | `varchar2` | 1000 | 是 | 网段说明 |

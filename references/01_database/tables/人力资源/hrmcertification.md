# 泛微OA 数据表: `hrmcertification`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcertification`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `datefrom` | 开始日期 | `char` | 10 | 是 | 开始日期 |
| 4 | `dateto` | 结束日期 | `char` | 10 | 是 | 结束日期 |
| 5 | `certname` | 证书名称 | `varchar2` | 480 | 是 | 证书名称 |
| 6 | `awardfrom` | 颁发机构 | `varchar2` | 800 | 是 | 颁发机构 |

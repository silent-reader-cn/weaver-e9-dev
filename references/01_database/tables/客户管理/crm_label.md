# 泛微OA 数据表: `crm_label`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_label`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `userid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `name` | 标签名称 | `varchar2` | 1000 | 是 | 标签名称 |
| 4 | `labelcolor` | 标签颜色 | `varchar2` | 1000 | 是 | 标签颜色 |
| 5 | `createdate` | 创建日期 | `varchar2` | 1000 | 是 | 创建日期 |
| 6 | `createtime` | 创建时间 | `varchar2` | 1000 | 是 | 创建时间 |
| 7 | `isused` | 是否启用 | `integer` | - | 是 | 是否启用 |
| 8 | `labelorder` | 标签排序 | `integer` | - | 是 | 标签排序 |
| 9 | `labeltype` | 标签类型 | `varchar2` | 1000 | 是 | 标签类型 |
| 10 | `textcolor` | 字体颜色 | `varchar2` | 1000 | 是 | 字体颜色 |

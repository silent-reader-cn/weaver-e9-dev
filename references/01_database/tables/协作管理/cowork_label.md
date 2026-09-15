# 泛微OA 数据表: `cowork_label`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_label`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `userid` | 用户id | `integer` | - | 是 | - |
| 3 | `name` | 标签名称 | `varchar2` | 1000 | 是 | - |
| 4 | `labelcolor` | 标签颜色 | `varchar2` | 1000 | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 400 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 400 | 是 | - |
| 7 | `isused` | 是否启用 | `integer` | - | 是 | - |
| 8 | `labelorder` | 排序 | `integer` | - | 是 | - |
| 9 | `labeltype` | 标签类型 | `varchar2` | 800 | 是 | - |
| 10 | `textcolor` | 文本颜色 | `varchar2` | 160 | 是 | - |

# 泛微OA 数据表: `cowork_base_set`

- **所属模块**: `协作管理`
- **数据库表名**: `cowork_base_set`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `coworkstate` | 协作主题结束后仍可回复 | `varchar2` | 16 | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `itemstate` | 默认开启主题标题 | `varchar2` | 16 | 是 | - |
| 4 | `infostate` | 废弃了，无用 | `varchar2` | 16 | 是 | - |
| 5 | `userid` | 设置人员 | `integer` | - | 是 | - |
| 6 | `createdate` | 设置日期 | `char` | 10 | 是 | - |
| 7 | `createtime` | 设置时间 | `char` | 8 | 是 | - |
| 8 | `dealchangeminute` | 相关交流及评论可修改、删除时间 | `varchar2` | 1000 | 是 | - |

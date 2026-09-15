# 泛微OA 数据表: `blog_notes`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_notes`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `userid` | 人员id | `integer` | - | 否 | - |
| 3 | `updatedate` | 更新时间 | `varchar2` | 80 | 是 | - |
| 4 | `content` | 内容 | `clob` | 4000 | 是 | - |
| 5 | `isremind` | 是否提醒 | `integer` | - | 是 | - |

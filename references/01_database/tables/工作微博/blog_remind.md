# 泛微OA 数据表: `blog_remind`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_remind`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `remindid` | 提醒id | `integer` | - | 是 | - |
| 3 | `relatedid` | 相关人id | `integer` | - | 是 | - |
| 4 | `remindtype` | 提醒类型 | `integer` | - | 是 | - |
| 5 | `remindvalue` | 提醒值 | `varchar2` | 800 | 是 | - |
| 6 | `status` | 状态 | `integer` | - | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |

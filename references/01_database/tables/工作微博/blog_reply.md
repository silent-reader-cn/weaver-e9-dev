# 泛微OA 数据表: `blog_reply`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_reply`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 2 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |
| 3 | `content` | 内容 | `clob` | 4000 | 是 | - |
| 4 | `comefrom` | 来源 | `integer` | - | 是 | - |
| 5 | `commenttype` | 评论类型 | `integer` | - | 是 | - |
| 6 | `workdate` | 工作日 | `varchar2` | 80 | 是 | - |
| 7 | `bediscussantid` | 微博所属人id | `integer` | - | 是 | - |
| 8 | `relatedid` | 关联人员id | `integer` | - | 是 | - |
| 9 | `id` | 主键id | `integer` | - | 否 | - |
| 10 | `userid` | 人员id | `integer` | - | 是 | - |
| 11 | `discussid` | 微博id | `integer` | - | 是 | - |

# 泛微OA 数据表: `blog_discuss`

- **所属模块**: `工作微博`
- **数据库表名**: `blog_discuss`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `userid` | 人员id | `integer` | - | 是 | - |
| 3 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 4 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |
| 5 | `content` | 内容 | `clob` | 4000 | 是 | - |
| 6 | `lastupdatetime` | 最后更新时间 | `varchar2` | 400 | 是 | - |
| 7 | `isreplenish` | 是否补交 | `integer` | - | 是 | - |
| 8 | `workdate` | 工作日 | `varchar2` | 10 | 是 | - |
| 9 | `score` | 评分 | `integer` | - | 是 | - |
| 10 | `comefrom` | 来源 | `integer` | - | 是 | - |

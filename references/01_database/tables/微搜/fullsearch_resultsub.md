# 泛微OA 数据表: `fullsearch_resultsub`

- **所属模块**: `微搜`
- **数据库表名**: `fullsearch_resultsub`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | 主键 |
| 2 | `createdate` | 创建日期 | `varchar2` | 20 | 否 | 创建日期 |
| 3 | `createtime` | 创建时间 | `varchar2` | 20 | 否 | 创建时间 |
| 4 | `searchkey` | 搜索关键字 | `varchar2` | 200 | 否 | 搜索关键字 |
| 5 | `page` | 当前页 | `integer` | - | 否 | 当前页 |
| 6 | `pagesize` | 每页条数 | `integer` | - | 否 | 每页条数 |
| 7 | `searchtype` | 搜索类型 | `varchar2` | 20 | 否 | 搜索类型 |
| 8 | `loginid` | 登录id | `varchar2` | 50 | 否 | 登录id |
| 9 | `conditionstring` | 高级搜索条件 | `varchar2` | 200 | 否 | 高级搜索条件 |
| 10 | `sort` | 排序条件 | `varchar2` | 20 | 否 | 排序条件 |
| 11 | `contenttype` | 搜索范围 | `varchar2` | 20 | 否 | 搜索范围 |
| 12 | `sourcetype` | 模块类型 | `varchar2` | 20 | 否 | 模块类型 |
| 13 | `searchfield` | 搜索字段 | `varchar2` | 20 | 否 | 搜索字段 |

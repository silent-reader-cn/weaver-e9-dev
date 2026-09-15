# 泛微OA 数据表: `fullsearch_robot`

- **所属模块**: `微搜`
- **数据库表名**: `fullsearch_robot`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `title` | 标题 | `varchar2` | 1000 | 是 | - |
| 3 | `keywords` | 关键字 | `varchar2` | 2000 | 是 | 空格分开 |
| 4 | `url` | 固定链接 | `varchar2` | 2000 | 是 | 链接方式打开是的链接 显示方式为链接时有效 |
| 5 | `createdate` | 创建时间 | `varchar2` | 80 | 是 | 固定 2015-04-01 |
| 6 | `iframeurl` | div显示页面地址 | `varchar2` | 2000 | 是 | 搜索页面直接显示页面地址 显示方式为div时有效 |
| 7 | `width` | div宽度 | `integer` | - | 是 | div宽度 显示方式为div时有效 |
| 8 | `height` | div高度 | `integer` | - | 是 | div高度 显示方式为div时有效 |
| 9 | `showdiv` | 显示方式 | `char` | 1 | 是 | 0 链接方式 1 div展示 |
| 10 | `state` | 状态 | `integer` | - | 是 | 0启用 1禁用 |

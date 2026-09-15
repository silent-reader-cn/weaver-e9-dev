# 泛微OA 数据表: `downloadlog`

- **所属模块**: `知识管理`
- **数据库表名**: `downloadlog`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `userid` | 用户id | `integer` | - | 否 | - |
| 2 | `username` | 用户名称 | `varchar2` | 480 | 是 | - |
| 3 | `downloadtime` | 下载时间 | `char` | 19 | 是 | - |
| 4 | `imageid` | 图片/附件id | `integer` | - | 是 | - |
| 5 | `imagename` | 图片/附件名称 | `varchar2` | 1000 | 是 | - |
| 6 | `docid` | 文档id | `integer` | - | 是 | - |
| 7 | `docname` | 文档名称 | `varchar2` | 1000 | 是 | - |
| 8 | `clientaddress` | ip地址 | `varchar2` | 160 | 是 | - |

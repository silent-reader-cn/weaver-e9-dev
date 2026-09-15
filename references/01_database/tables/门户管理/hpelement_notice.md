# 泛微OA 数据表: `hpelement_notice`

- **所属模块**: `门户管理`
- **数据库表名**: `hpelement_notice`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `title` | 标题 | `varchar2` | 1000 | 是 | - |
| 3 | `content` | 内容 | `clob` | 4000 | 是 | - |
| 4 | `imgsrc` | 图片路径 | `varchar2` | 1000 | 是 | - |
| 5 | `creator` | 创建人 | `integer` | - | 是 | - |
| 6 | `creatortype` | 创建人类型 | `char` | 1 | 是 | - |
| 7 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 8 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 9 | `lastupdatedate` | 最后更新日期 | `varchar2` | 80 | 是 | - |
| 10 | `lastupdatetime` | 最后更新时间 | `varchar2` | 64 | 是 | - |
| 11 | `eid` | 元素id | `integer` | - | 是 | - |
| 12 | `relatedocid` | 关联文档id | `integer` | - | 是 | - |

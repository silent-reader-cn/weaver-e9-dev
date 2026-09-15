# 泛微OA 数据表: `hrmresourcefile`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourcefile`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `fieldid` | 文件id | `integer` | - | 是 | 文件id |
| 4 | `docid` | 文档id | `integer` | - | 是 | 文档id |
| 5 | `docname` | 文档名称 | `varchar2` | 4000 | 是 | 文档名称 |
| 6 | `doccreater` | 文档创建人 | `integer` | - | 是 | 文档创建人 |
| 7 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 8 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 9 | `scopeid` | 范围id | `integer` | - | 是 | 范围id |

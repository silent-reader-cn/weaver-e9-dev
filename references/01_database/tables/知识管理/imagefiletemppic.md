# 泛微OA 数据表: `imagefiletemppic`

- **所属模块**: `知识管理`
- **数据库表名**: `imagefiletemppic`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `imagefileid` | 文件id | `integer` | - | 否 | - |
| 3 | `docid` | 文档id | `integer` | - | 是 | - |
| 4 | `createid` | 创建人id | `integer` | - | 是 | - |
| 5 | `createdate` | 创建日期 | `char` | 10 | 是 | - |
| 6 | `createtime` | 创建时间 | `char` | 8 | 是 | - |
| 7 | `docfiletype` | 文件类型 | `varchar2` | 16 | 是 | 1:图片，2：一般附件 |

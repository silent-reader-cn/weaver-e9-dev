# 泛微OA 数据表: `docimagefile`

- **所属模块**: `知识管理`
- **数据库表名**: `docimagefile`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `signaturecount` | 签章 | `integer` | - | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `docid` | 对应文档id | `integer` | - | 是 | - |
| 4 | `imagefileid` | 图片文件id | `integer` | - | 是 | 由sequenceindex表得到，和imagefile表相关联 |
| 5 | `imagefilename` | 文件名称,包括后缀名 | `varchar2` | 1000 | 是 | - |
| 6 | `imagefiledesc` | 文件描述 | `varchar2` | 1000 | 是 | 由用户给出 |
| 7 | `imagefilewidth` | 文件宽度 | `integer` | - | 是 | 象素 只对文档中的图片文件,不包括附件及附件中的图片文件 |
| 8 | `imagefileheight` | 文件高度 | `integer` | - | 是 | 象素：只对文档中的图片文件,不包括附件及附件中的图片文件 |
| 9 | `imagefielsize` | 文件大小 | `integer` | - | 是 | - |
| 10 | `docfiletype` | 文件类型 | `varchar2` | 16 | 是 | - |

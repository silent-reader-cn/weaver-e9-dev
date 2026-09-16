# 泛微OA 数据表: `workflow_texttopdf`

- **中文名称**: 转PDF记录表
- **所属模块**: `公文管理`
- **数据库表名**: `workflow_texttopdf`
- **主键**: `id`
- **字段数**: `9`

> 说明：流程创建文档-正文转PDF

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | 序号 |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 否 | 否 | - | - | 请求id |
| 3 | `docid` | 被转换的文档id | `integer` | - | 是 | 否 | 否 | - | - | 被转换的文档id |
| 4 | `pdfdocid` | 转成pdf后的文档id | `integer` | - | 是 | 否 | 否 | - | - | 转成pdf后的文档id |
| 5 | `pdfimagefileid` | 转成pdf后的imagefileid | `integer` | - | 是 | 否 | 否 | - | - | 转成pdf后的imagefileid |
| 6 | `decryptpdfdocid` | 转成pdf后的脱密文档id | `integer` | - | 是 | 否 | 否 | - | - | 转成pdf后的脱密文档id |
| 7 | `decryptpdfimagefileid` | 转成脱密pdf后的imagefileid | `integer` | - | 是 | 否 | 否 | - | - | 转成脱密pdf后的imagefileid |
| 8 | `transformdate` | 转换日期 | `char` | 10 | 是 | 否 | 否 | - | - | 转换日期 |
| 9 | `transformtime` | 转换时间 | `char` | 8 | 是 | 否 | 否 | - | - | 转换时间 |

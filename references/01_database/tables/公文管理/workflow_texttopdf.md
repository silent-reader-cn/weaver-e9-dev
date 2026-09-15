# 泛微OA 数据表: `workflow_texttopdf`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_texttopdf`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 序号 |
| 2 | `requestid` | 请求id | `integer` | - | 是 | 请求id |
| 3 | `docid` | 被转换的文档id | `integer` | - | 是 | 被转换的文档id |
| 4 | `pdfdocid` | 转成pdf后的文档id | `integer` | - | 是 | 转成pdf后的文档id |
| 5 | `pdfimagefileid` | 转成pdf后的imagefileid | `integer` | - | 是 | 转成pdf后的imagefileid |
| 6 | `decryptpdfdocid` | 转成pdf后的脱密文档id | `integer` | - | 是 | 转成pdf后的脱密文档id |
| 7 | `decryptpdfimagefileid` | 转成脱密pdf后的imagefileid | `integer` | - | 是 | 转成脱密pdf后的imagefileid |
| 8 | `transformdate` | 转换日期 | `char` | 10 | 是 | 转换日期 |
| 9 | `transformtime` | 转换时间 | `char` | 8 | 是 | 转换时间 |

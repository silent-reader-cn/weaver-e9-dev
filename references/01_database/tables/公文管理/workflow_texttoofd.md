# 泛微OA 数据表: `workflow_texttoofd`

- **所属模块**: `公文管理`
- **数据库表名**: `workflow_texttoofd`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `requestid` | 请求编号 | `integer` | - | 是 | - |
| 3 | `docid` | 正文ID | `integer` | - | 是 | - |
| 4 | `ofddocid` | OFD文档编号（对应docimagefile表中的docid） | `integer` | - | 是 | - |
| 5 | `ofdimagefileid` | OFD文档编号（对应imagefile表中的imagefileid） | `integer` | - | 是 | - |
| 6 | `ofdstate` | 转换状态 | `char` | 2 | 是 | 0：成功 1：失败 |
| 7 | `transformdate` | 转换日期 | `char` | 10 | 是 | - |
| 8 | `transformtime` | 转换时间 | `char` | 8 | 是 | - |

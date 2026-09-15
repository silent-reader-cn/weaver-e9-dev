# 泛微OA 数据表: `social_filedownloadlog`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_filedownloadlog`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | 主键id |
| 2 | `fileid` | 文件id | `varchar2` | 800 | 是 | 文件id |
| 3 | `userid` | 上传人id | `integer` | 0 | 是 | 上传人id |
| 4 | `lastsavepath` | 最后上传路径 | `varchar2` | 1000 | 是 | 最后上传路径 |
| 5 | `downloadcount` | 下载次数 | `integer` | 0 | 是 | 下载次数 |

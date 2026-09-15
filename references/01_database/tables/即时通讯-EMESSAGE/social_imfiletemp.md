# 泛微OA 数据表: `social_imfiletemp`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imfiletemp`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 是 | 主键id |
| 2 | `userid` | 发送人id | `integer` | - | 是 | 发送人id |
| 3 | `targetid` | 接收人id | `varchar2` | 1000 | 是 | 接收人id |
| 4 | `targettype` | 发送类型 | `integer` | - | 是 | 发送类型 |
| 5 | `fileid` | 文件id | `integer` | - | 是 | 文件id |
| 6 | `filename` | 文件名 | `varchar2` | 1000 | 是 | 文件名 |
| 7 | `filesize` | 文件大小 | `integer` | - | 是 | 文件大小 |
| 8 | `filetype` | 文件类型 | `varchar2` | 80 | 是 | 文件类型 |
| 9 | `createdate` | 创建时间 | `varchar2` | 160 | 是 | 创建时间 |
| 10 | `downcount` | 下载次数 | `integer` | - | 是 | 下载次数 |
| 11 | `resourcetype` | 来源类型 | `integer` | - | 是 | 来源类型 |
| 12 | `status` | 状态 | `char` | 1 | 是 | 状态 |

# 泛微OA 数据表: `social_imfile`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_imfile`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `userid` | 用户id | `integer` | - | 否 | 用户id |
| 3 | `targetid` | 会话id | `varchar2` | 1000 | 否 | 会话id |
| 4 | `targettype` | 会话类型 | `integer` | - | 否 | 会话类型 |
| 5 | `fileid` | 文件id | `integer` | - | 否 | 文件id |
| 6 | `filename` | 文件名 | `varchar2` | 1000 | 否 | 文件名 |
| 7 | `filesize` | 文件大小 | `integer` | - | 否 | 文件大小 |
| 8 | `filetype` | 文件类型 | `varchar2` | 80 | 否 | 文件类型 |
| 9 | `createdate` | 创建日期 | `varchar2` | 160 | 否 | 创建日期 |
| 10 | `downcount` | 下载次数 | `integer` | - | 否 | 下载次数 |
| 11 | `resourcetype` | 资源类型 | `integer` | - | 否 | 1代表分享附件，2代表原始上传附件 |
| 12 | `status` | 资源状态 | `char` | 1 | 是 | 资源状态 |

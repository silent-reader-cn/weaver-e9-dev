# 泛微OA 数据表: `docsignature`

- **所属模块**: `人力资源`
- **数据库表名**: `docsignature`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `markid` | 签章id | `integer` | - | 否 | 签章id |
| 2 | `hrmresid` | 签章所属的用户id | `integer` | - | 否 | 签章所属的用户id |
| 3 | `password` | 用户签章的密码 | `varchar2` | 400 | 是 | 用户签章的密码 |
| 4 | `markname` | 签章名称 | `varchar2` | 800 | 是 | 签章名称 |
| 5 | `marktype` | 签章图片的图片文件类型 | `varchar2` | 80 | 是 | 目前只支持jpg |
| 6 | `markpath` | 签章图片的存储路径 | `varchar2` | 1000 | 是 | 签章图片的存储路径 |
| 7 | `marksize` | 签章图片文件的大小 | `integer` | - | 是 | 签章图片文件的大小 |
| 8 | `markdate` | 签章创建日期 | `varchar2` | 152 | 是 | 签章创建日期 |
| 9 | `subcompanyid` | 所属分部id | `integer` | - | 是 | 所属分部id |
| 10 | `sealtype` | 签章类型 | `integer` | - | 是 | 1：个人签章；2公司签章 |
| 11 | `isdefault` | 是否默认 | `char` | 1 | 是 | 是否默认 |

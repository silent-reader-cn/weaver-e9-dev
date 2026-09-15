# 泛微OA 数据表: `outerdatawfsetdetail`

- **所属模块**: `集成模块`
- **数据库表名**: `outerdatawfsetdetail`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 自增长主键 |
| 2 | `mainid` | outerdatawfset表的id | `integer` | - | 是 | outerdatawfset表的id |
| 3 | `wffieldid` | 字段id | `integer` | - | 是 | -1表示标题；-2表示创建人； |
| 4 | `wffieldname` | 字段数据库名 | `varchar2` | 240 | 是 | 字段数据库名 |
| 5 | `wffieldhtmltype` | 字段html类型 | `integer` | - | 是 | 字段html类型 |
| 6 | `wffieldtype` | 字段类型 | `integer` | - | 是 | 字段类型 |
| 7 | `wffielddbtype` | 字段数据库类型 | `varchar2` | 400 | 是 | 字段数据库类型 |
| 8 | `outerfieldname` | 外部字段数据库名 | `varchar2` | 400 | 是 | 外部字段数据库名 |
| 9 | `changetype` | 转换规则类型 | `integer` | - | 是 | 转换规则类型 |
| 10 | `iswriteback` | 回写标记位 | `char` | 1 | 是 | 回写标记位 |
| 11 | `customsql` | 自定义sql | `varchar2` | 2000 | 是 | 自定义sql |
| 12 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 13 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | 创建时间 |
| 14 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 15 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | 修改时间 |
| 16 | `attachment_type` | 附件类型 | `integer` | - | 是 | 1,FTP;2,本地目录;3,数据库;4,URL |
| 17 | `attachment_settings` | 附件设置 | `varchar2` | 2000 | 是 | 附件设置详细信息 |

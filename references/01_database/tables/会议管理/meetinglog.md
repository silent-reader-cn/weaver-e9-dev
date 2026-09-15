# 泛微OA 数据表: `meetinglog`

- **所属模块**: `会议管理`
- **数据库表名**: `meetinglog`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `relatedid` | 会议记录id | `integer` | - | 否 | - |
| 3 | `relatedname` | 会议名称 | `varchar2` | 1000 | 是 | - |
| 4 | `operatetype` | 操作类型 | `varchar2` | 16 | 否 | 1：新建，2：修改，3：删除，4：移动（文档的目录转移），5：复制（文档的复制） |
| 5 | `operatedesc` | 操作描述 | `varchar2` | 2000 | 是 | - |
| 6 | `operateitem` | 操作项目 | `varchar2` | 160 | 是 | 固定值 会议模块为“303” |
| 7 | `operateuserid` | 操作人id | `integer` | - | 否 | - |
| 8 | `operatedate` | 操作日期 | `char` | 10 | 否 | - |
| 9 | `operatetime` | 操作时间 | `char` | 8 | 否 | - |
| 10 | `clientaddress` | 客户端ip | `char` | 15 | 是 | - |
| 11 | `istemplate` | 是否为流程模板 | `integer` | - | 是 | 0：不是，1：是 |
| 12 | `operatesmalltype` | 日志类型 | `integer` | - | 是 | 0：系统维护日志 1：系统操作日志 |
| 13 | `operateusertype` | 操作用户类型 | `integer` | - | 是 | 即登陆类型 |

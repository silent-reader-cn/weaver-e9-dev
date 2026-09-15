# 泛微OA 数据表: `crm_log`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_log`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | id |
| 2 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 3 | `logtype` | 日志类型 | `char` | 2 | 是 | 新建:n，删除:d，编辑:m，门户:p，状态:a，合并:u,批量添加-添加:b,批量更新-更新:d，批量更新-新建:e |
| 4 | `documentid` | 文档id | `integer` | - | 是 | 文档id |
| 5 | `logcontent` | 修改内容 | `varchar2` | 4000 | 是 | 修改内容 |
| 6 | `submitdate` | 修改日期 | `varchar2` | 10 | 是 | 修改日期 |
| 7 | `submittime` | 修改时间 | `varchar2` | 8 | 是 | 修改时间 |
| 8 | `submiter` | 修改者 | `integer` | - | 是 | 修改者 |
| 9 | `clientip` | IP地址 | `char` | 15 | 是 | ip地址 |
| 10 | `submitertype` | 修改者类型 | `integer` | - | 是 | 2：客户；1：内部人员 |
| 11 | `logBizType` | 日志大类 | `integer` | - | 否 | 如：1：客户、2：商机、3：联系人 |
| 12 | `logBizTypeTargetId` | 日志大类的数据id | `integer` | - | 否 | 日志大类队对应的数据id |
| 13 | `logSmallType` | 日志小类 | `integer` | - | 否 | 卡片的页签，具体信息可查看：LogSmallTypeEnum.java |
| 14 | `logSmallTypeTargetId` | 日志小类下的数据id | `integer` | - | 否 | 卡片的页签下的数据id，如;地址管理，那么村的就是某个地址的id |
| 15 | `operateType` | 操作类型 | `integer` | - | 否 | 操作类型，具体查看：OperateTypeEnum.java |
| 16 | `operateTypeDetail` | 操作类型下的具体操作 | `integer` | - | 否 | 操作类型下的具体操作，如新建客户，具体的操作有：普通新建，客户导入、webservice等操作 |
| 17 | `oldValues` | 旧值 | `clob` | - | 否 | 某字段编辑信息前的值，以键值对形式存储 |
| 18 | `newValues` | 新值 | `clob` | - | 否 | 某字段编辑信息后的值，以键值对形式存储 |
| 19 | `params` | 请求参数 | `clob` | - | 否 | 请求的参数 |
| 20 | `deviceType` | 客户端 | `integer` | - | 否 | 客户端：0:PC端，1：移动端 |

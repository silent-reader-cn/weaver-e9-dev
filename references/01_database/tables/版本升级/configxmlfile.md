# 泛微OA 数据表: `configxmlfile`

- **中文名称**: xml文件配置信息表
- **所属模块**: `版本升级`
- **数据库表名**: `configxmlfile`
- **主键**: `ID`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `configfileid` | 关联主表的ID | `integer` | - | 否 | 否 | 否 | - | - | 与configFileManager表的ID关联 |
| 3 | `attrvalue` | 属性值 | `varchar2` | 2000 | 否 | 否 | 否 | - | - | - |
| 4 | `attrnotes` | 属性说明 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 否 | 否 | - | - | - |
| 7 | `issystem` | 是否系统自带 | `integer` | - | 是 | 否 | 否 | - | 0 | 1:系统自带 2:客户创建 |
| 8 | `requisite` | 是否必配 | `integer` | - | 是 | 否 | 否 | - | 0 | 1:必配 2:选配 |
| 9 | `xpath` | xpath路径 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 用于定位xml中某个节点配置内容的路径 |
| 10 | `isdelete` | 是否删除 | `integer` | - | 是 | 否 | 否 | - | 0 | 1:已删除 2:未删除 |
| 11 | `xmldetailid` | 导入时的id | `integer` | - | 是 | 否 | 否 | - | - | 总部导入时的ID |

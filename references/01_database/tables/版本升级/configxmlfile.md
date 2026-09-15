# 泛微OA 数据表: `configxmlfile`

- **所属模块**: `版本升级`
- **数据库表名**: `configxmlfile`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `configfileid` | 关联主表的ID | `integer` | - | 否 | 与configFileManager表的ID关联 |
| 3 | `attrvalue` | 属性值 | `varchar2` | 2000 | 否 | - |
| 4 | `attrnotes` | 属性说明 | `varchar2` | 1000 | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 7 | `issystem` | 是否系统自带 | `integer` | - | 是 | 1:系统自带    2:客户创建 |
| 8 | `requisite` | 是否必配 | `integer` | - | 是 | 1:必配        2:选配 |
| 9 | `xpath` | xpath路径 | `varchar2` | 1000 | 是 | 用于定位xml中某个节点配置内容的路径 |
| 10 | `isdelete` | 是否删除 | `integer` | - | 是 | 1:已删除       2:未删除 |
| 11 | `xmldetailid` | 导入时的id | `integer` | - | 是 | 总部导入时的ID |

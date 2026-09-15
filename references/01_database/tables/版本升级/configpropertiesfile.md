# 泛微OA 数据表: `configpropertiesfile`

- **所属模块**: `版本升级`
- **数据库表名**: `configpropertiesfile`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `configfileid` | 关联的主表ID | `integer` | - | 否 | 与configmanager的ID关联字段, |
| 3 | `attrname` | 属性名 | `varchar2` | 1000 | 否 | - |
| 4 | `attrvalue` | 属性值 | `varchar2` | 1000 | 否 | - |
| 5 | `attrnotes` | 属性说明信息 | `varchar2` | 1000 | 是 | - |
| 6 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 7 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 8 | `issystem` | 是否系统自带 | `integer` | - | 是 | 1:正式系统导出 2:客户自定义创建 |
| 9 | `requisite` | 是否必须配置 | `integer` | - | 是 | 1:必配    2:选配 |
| 10 | `isdelete` | 是否删除 | `integer` | - | 是 | 1:已删除    0:未删除 |
| 11 | `propdetailid` | 导入的id | `integer` | - | 是 | 总部对应的id |
| 12 | `needcheck` | 是否需要检查 | `char` | 1 | 是 | 1:需要    0:不需要 |

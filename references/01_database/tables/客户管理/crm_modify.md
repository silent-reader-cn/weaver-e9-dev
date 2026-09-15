# 泛微OA 数据表: `crm_modify`

- **所属模块**: `客户管理`
- **数据库表名**: `crm_modify`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `customerid` | 客户id | `integer` | - | 是 | 客户id |
| 2 | `tabledesc` | 对应表 | `char` | 1 | 是 | "1"－客户基本信息，"2"－联系人，"3"－地址信息 |
| 3 | `type` | 类型 | `integer` | - | 是 | 如果是地址信息表就是地址类型ID，如果是联系人表就是联系人ID |
| 4 | `addresstype` | 地址类型 | `integer` | - | 是 | 地址类型 |
| 5 | `fieldname` | 字段名 | `varchar2` | 800 | 是 | 字段名 |
| 6 | `modifydate` | 修改日期 | `varchar2` | 10 | 是 | 修改日期 |
| 7 | `modifytime` | 修改时间 | `varchar2` | 8 | 是 | 修改时间 |
| 8 | `original` | 元数据 | `varchar2` | 1000 | 是 | 该之前的数据 |
| 9 | `modified` | 新数据 | `varchar2` | 1000 | 是 | 改之后的数据 |
| 10 | `modifier` | 修改者id | `integer` | - | 是 | 修改者id |
| 11 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |
| 12 | `submitertype` | 操作者类型 | `integer` | - | 是 | 1：内部人员；2：客户门户 |

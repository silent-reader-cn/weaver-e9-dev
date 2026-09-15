# 泛微OA 数据表: `prj_modify`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_modify`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `projectid` | 项目id | `integer` | - | 是 | 项目id |
| 2 | `type` | 日志类型 | `char` | 20 | 是 | 日志类型 |
| 3 | `fieldname` | 字段名 | `varchar2` | 800 | 是 | 字段名 |
| 4 | `modifydate` | 修改日期 | `varchar2` | 10 | 是 | 修改日期 |
| 5 | `modifytime` | 修改时间 | `varchar2` | 8 | 是 | 修改时间 |
| 6 | `original` | 旧值 | `varchar2` | 1000 | 是 | 旧值 |
| 7 | `modified` | 新值 | `varchar2` | 1000 | 是 | 新值 |
| 8 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 9 | `clientip` | 客户端ip | `char` | 15 | 是 | 客户端ip |
| 10 | `submitertype` | 提交类型 | `integer` | - | 是 | 提交类型 |

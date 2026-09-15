# 泛微OA 数据表: `clustersetting`

- **所属模块**: `其他`
- **数据库表名**: `clustersetting`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `ipaddress` | ip地址 | `varchar2` | 1000 | 是 | - |
| 3 | `httpaddress` | http访问地址 | `varchar2` | 1000 | 是 | - |
| 4 | `deployaddress` | 部署地址 | `varchar2` | 1000 | 是 | - |
| 5 | `ismainnode` | 是否主节点 | `char` | 1 | 是 | 0：非主节点 1：主节点 |
| 6 | `type` | 类型 | `varchar2` | 800 | 是 | ecology/emessage/emobile |
| 7 | `doupgrade` | 是否升级 | `char` | 1 | 是 | - |

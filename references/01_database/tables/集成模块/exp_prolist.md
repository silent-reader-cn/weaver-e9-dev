# 泛微OA 数据表: `exp_prolist`

- **所属模块**: `集成模块`
- **数据库表名**: `exp_prolist`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `proname` | 方案名称 | `varchar2` | 1000 | 是 | - |
| 3 | `proid` | 方案信息表id | `integer` | - | 否 | 根据方案类型来决定这个id去哪个表里找，ProType=0， 对应的id在exp_DBProSettings里找;ProType=1， 对应的id在exp_XMLProSettings里找 |
| 4 | `protype` | 方案类型 | `char` | 1 | 是 | 0，数据库；1，XML方案 |
| 5 | `profilesavetype` | 文件保存的位置 | `char` | 1 | 是 | 0,FTP;1,本地 |

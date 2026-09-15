# 泛微OA 数据表: `addepmap`

- **所属模块**: `集成模块`
- **数据库表名**: `addepmap`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键 | `integer` | - | 否 | - |
| 2 | `dep` | 组织架构名称 | `varchar2` | 800 | 是 | - |
| 3 | `pguid` | 上级组织架构guid | `varchar2` | 1000 | 是 | - |
| 4 | `distin` | 组织架构DN | `varchar2` | 2000 | 是 | 对应ou的distinguishedName属性 |
| 5 | `subcomcode` | 上级分部编号 | `varchar2` | 800 | 是 | - |
| 6 | `orgtype` | 组织架构类型 | `varchar2` | 80 | 是 | 1：分部  2：部门 |
| 7 | `guid` | 组织架构guid | `varchar2` | 1000 | 是 | 对应ou的objectGUID属性 |
| 8 | `status` | 状态 | `char` | 1 | 是 | 1：新增  2：修改 |

# 泛微OA 数据表: `prj_prjcardgroup`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_prjcardgroup`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `prjtype` | 项目类型 | `integer` | - | 否 | 项目类型 |
| 3 | `groupname` | 分组名称 | `varchar2` | 480 | 是 | 分组名称 |
| 4 | `grouplabel` | 分组标签 | `integer` | - | 是 | 分组标签 |
| 5 | `dsporder` | 分组顺序 | `number` | (10,2) | 是 | 分组顺序 |
| 6 | `isopen` | 是否启用 | `char` | 1 | 是 | 是否启用 |
| 7 | `ismand` | 是否必需 | `char` | 1 | 是 | 是否必需 |
| 8 | `isused` | 是否已使用 | `char` | 1 | 是 | 是否已使用 |
| 9 | `issystem` | 是否是系统组 | `char` | 1 | 是 | 是否是系统组 |

# 泛微OA 数据表: `prj_templettask_needdoc`

- **中文名称**: 项目模板任务所需文档
- **所属模块**: `项目管理`
- **数据库表名**: `prj_templettask_needdoc`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `templettaskid` | 任务id | `integer` | - | 是 | 否 | 否 | - | - | 任务id |
| 3 | `docmaincategory` | 文档主目录id | `integer` | - | 是 | 否 | 否 | - | - | 文档主目录id |
| 4 | `docsubcategory` | 文档子目录id | `integer` | - | 是 | 否 | 否 | - | - | 文档子目录id |
| 5 | `docseccategory` | 文档分目录id | `integer` | - | 是 | 否 | 否 | - | - | 文档分目录id |
| 6 | `isnecessary` | 是否必需 | `char` | 1 | 是 | 否 | 否 | - | - | 是否必需 |
| 7 | `istemplettask` | 是否模板任务 | `char` | 1 | 是 | 否 | 否 | - | - | 是否模板任务 |

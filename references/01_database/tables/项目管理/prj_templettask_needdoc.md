# 泛微OA 数据表: `prj_templettask_needdoc`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_templettask_needdoc`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `templettaskid` | 任务id | `integer` | - | 是 | 任务id |
| 3 | `docmaincategory` | 文档主目录id | `integer` | - | 是 | 文档主目录id |
| 4 | `docsubcategory` | 文档子目录id | `integer` | - | 是 | 文档子目录id |
| 5 | `docseccategory` | 文档分目录id | `integer` | - | 是 | 文档分目录id |
| 6 | `isnecessary` | 是否必需 | `char` | 1 | 是 | 是否必需 |
| 7 | `istemplettask` | 是否模板任务 | `char` | 1 | 是 | 是否模板任务 |

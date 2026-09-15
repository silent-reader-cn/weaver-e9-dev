# 泛微OA 数据表: `cus_formsetting`

- **所属模块**: `知识管理`
- **数据库表名**: `cus_formsetting`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `module` | 模块 | `varchar2` | 480 | 是 | 可选值：hrm、cpt、prj |
| 3 | `page` | 调用的页面 | `varchar2` | 1000 | 是 | 可选值：hrmresourcebase、hrmresourcepersonal、hrmresourcework等 |
| 4 | `status` | 状态 | `integer` | - | 是 | - |
| 5 | `page_url` | 页面链接 | `varchar2` | 1000 | 是 | - |
| 6 | `base_datatable` | 基础数据表 | `varchar2` | 400 | 是 | - |
| 7 | `base_id` | 基础id | `varchar2` | 400 | 是 | - |
| 8 | `defined_datatable` | 自定义数据表 | `varchar2` | 400 | 是 | - |
| 9 | `base_definedid` | 基础自定义id | `varchar2` | 400 | 是 | - |
| 10 | `scopeid` | 范围id | `integer` | - | 是 | - |

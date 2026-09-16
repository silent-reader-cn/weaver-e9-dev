# 泛微OA 数据表: `Int_FieldMapper`

- **所属模块**: `集成模块`
- **数据库表名**: `Int_FieldMapper`
- **文档收录字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | - | - |
| 2 | `scope` | 配置类型 | `varchar2` | - | - | 1,腾讯邮箱集成;2,coremail集成 |
| 3 | `type` | 字段类型 | `varchar2` | - | - | 1,分部;2,部门;3,岗位;4,人员; |
| 4 | `src_field_inf` | 源字段配置 | `varchar2` | - | - | - |
| 5 | `trgt_field_inf` | 目标字段配置 | `varchar2` | - | - | - |
| 6 | `cnvrt_clazz` | 转换类 | `varchar2` | - | - | - |
| 7 | `direct` | 方向 | `varchar2` | - | - | 0,ec=>第三方;1,第三方=>ec |

# 泛微OA 数据表: `Int_Observers`

- **所属模块**: `集成模块`
- **数据库表名**: `Int_Observers`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识 | `integer` | - | - | - |
| 2 | `scope` | 配置类型 | `varchar2` | - | - | 1,腾讯邮箱集成;2,coremail集成 |
| 3 | `type` | 二级类型 | `varchar2` | - | - | 1,分部;2,部门;3,岗位;4,人员; |
| 4 | `observer_clazz` | 观察者类 | `varchar2` | - | - | - |
| 5 | `mapping_clazz` | 字段映射类 | `varchar2` | - | - | - |
| 6 | `isopen` | 是否启用 | `varchar2` | - | - | - |

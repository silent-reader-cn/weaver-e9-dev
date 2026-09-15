# 泛微OA 数据表: `prj_prjwfactset`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_prjwfactset`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `mainid` | 流程配置主表id | `integer` | - | 是 | 流程配置主表id |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | 字段id |
| 4 | `customervalue` | 动作类型 | `integer` | - | 是 | 动作类型 |
| 5 | `isnode` | 对象类型 | `integer` | - | 是 | 对象类型 |
| 6 | `objid` | 对象id | `integer` | - | 是 | 对象id |
| 7 | `istriggerreject` | 退回是否触发 | `integer` | - | 是 | 退回是否触发 |

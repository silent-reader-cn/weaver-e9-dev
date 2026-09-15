# 泛微OA 数据表: `workflow_createplangroup`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_createplangroup`
- **字段总数**: `4`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `createplanid` | workflow_createplan表主键 | `integer` | - | 是 | workflow_createplan表主键 |
| 3 | `groupid` | 分组id | `integer` | - | 是 | - |
| 4 | `isused` | 是否开启转换 | `integer` | - | 是 | 1、是，2、否 |

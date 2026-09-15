# 泛微OA 数据表: `user_defaultorder_setting`

- **所属模块**: `工作流程`
- **数据库表名**: `user_defaultorder_setting`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `userid` | 用户uid | `integer` | - | 否 | - |
| 3 | `usertype` | 用户类型 | `integer` | - | 否 | 0 oa用户、1客户 |
| 4 | `columnkey` | 列键名 | `varchar2` | 100 | 否 | 表格中的col名称 |
| 5 | `orderkey` | 排序键名 | `varchar2` | 4000 | 否 | 参与排序的键名 |
| 6 | `ordertype` | 排序类型 | `integer` | - | 否 | 升序，降序 |
| 7 | `sortorder` | 参数排序的先后顺序 | `integer` | - | 否 | 该字段，参数排序的先后顺序 |
| 8 | `pageid` | pageid | `varchar2` | 100 | 否 | - |

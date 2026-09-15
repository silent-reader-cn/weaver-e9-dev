# 泛微OA 数据表: `mode_batchset`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_batchset`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `expandid` | 页面扩展id | `integer` | - | 是 | 对应mode_pageexpand表的id |
| 3 | `showorder` | 显示顺序 | `number` | (15,2) | 是 | - |
| 4 | `customsearchid` | 查询列表id | `integer` | - | 是 | 对应mode_customsearch表的id |
| 5 | `isuse` | 是否启用 | `integer` | - | 是 | - |

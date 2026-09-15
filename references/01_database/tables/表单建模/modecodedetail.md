# 泛微OA 数据表: `modecodedetail`

- **所属模块**: `表单建模`
- **数据库表名**: `modecodedetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `uuid` | uuid | `varchar2` | 100 | 是 | - |
| 2 | `id` | ID | `integer` | - | 是 | - |
| 3 | `codemainid` | 字段编码主id | `integer` | - | 是 | 对应modecode表的id |
| 4 | `showname` | 显示名称 | `integer` | - | 是 | 多语言标签id，对应htmllabelindex表的id |
| 5 | `showtype` | 编码类型 | `integer` | - | 是 | - |

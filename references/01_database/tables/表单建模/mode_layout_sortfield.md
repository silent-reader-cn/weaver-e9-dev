# 泛微OA 数据表: `mode_layout_sortfield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_layout_sortfield`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `ordertype` | 排序类型 | `varchar2` | 80 | 是 | 升序或者降序 |
| 2 | `ordernum` | 字段顺序 | `integer` | - | 是 | 字段顺序排序 |
| 3 | `id` | 主键id | `integer` | - | 否 | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | - |
| 5 | `formid` | 表单id | `integer` | - | 是 | - |
| 6 | `layoutid` | 布局id | `integer` | - | 是 | - |
| 7 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 8 | `issort` | 是否排序 | `integer` | - | 是 | 0 |

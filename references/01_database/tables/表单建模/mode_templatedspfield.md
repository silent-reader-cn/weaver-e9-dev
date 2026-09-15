# 泛微OA 数据表: `mode_templatedspfield`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_templatedspfield`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `templateid` | 模板主表id | `integer` | - | 是 | - |
| 3 | `fieldid` | 字段id | `integer` | - | 是 | - |
| 4 | `isshow` | 是否显示 | `integer` | - | 是 | - |
| 5 | `fieldorder` | 排序 | `integer` | - | 是 | - |
| 6 | `topt` | 逻辑符 | `varchar2` | 80 | 是 | - |
| 7 | `topt1` | 逻辑符2 | `varchar2` | 80 | 是 | - |
| 8 | `tvalue` | 值1 | `varchar2` | 800 | 是 | - |
| 9 | `tvalue1` | 值2 | `varchar2` | 800 | 是 | - |
| 10 | `tname` | 名称 | `varchar2` | 800 | 是 | - |

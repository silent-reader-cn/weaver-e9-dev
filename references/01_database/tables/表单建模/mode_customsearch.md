# 泛微OA 数据表: `mode_customsearch`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customsearch`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `iswatermark` | 水印信息 | `integer` | - | 是 | - |
| 2 | `sliderpercentage` | 滑块显示占比 | `varchar2` | 1000 | 是 | - |
| 3 | `isshowquerycondition` | 是否展开查询条件 | `integer` | - | 是 | - |
| 4 | `javafileaddress` | java查询条件 | `varchar2` | 1000 | 是 | - |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `modeid` | 模块名称 | `integer` | - | 是 | 模块id，对应modeinfo表的id |
| 7 | `customname` | 名称 | `varchar2` | 800 | 是 | - |
| 8 | `customdesc` | 描述 | `varchar2` | 4000 | 是 | - |
| 9 | `defaultsql` | 固定查询条件 | `varchar2` | 4000 | 是 | sql类型的查询条件sqlwhere |
| 10 | `disquicksearch` | 隐藏快捷搜索 | `integer` | - | 是 | - |

# 泛微OA 数据表: `mode_batchset`

- **中文名称**: 批量操作设置信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_batchset`
- **主键**: `id`
- **字段数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `expandid` | 页面扩展id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_pageexpand表的id |
| 3 | `showorder` | 显示顺序 | `number` | (15,2) | 是 | 否 | 否 | - | - | - |
| 4 | `customsearchid` | 查询列表id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_customsearch表的id |
| 5 | `isuse` | 是否启用 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 6 | `listbatchname` | 显示名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 7 | `isshortcutbutton` | 快捷按钮 | `integer` | - | 是 | 否 | 否 | - | - | - |

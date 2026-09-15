# 泛微OA 数据表: `meeting_selectitem`

- **所属模块**: `会议管理`
- **数据库表名**: `meeting_selectitem`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `fieldid` | 对应meeting_formfield的id | `integer` | - | 否 | - |
| 3 | `selectvalue` | 选项值 | `integer` | - | 否 | - |
| 4 | `selectname` | 选项名称 | `varchar2` | 1000 | 是 | - |
| 5 | `selectlabel` | 选项名称标签id | `varchar2` | 1000 | 是 | 系统级别的支持国际化 |
| 6 | `listorder` | 排序 | `integer` | - | 否 | - |
| 7 | `isdel` | 是否逻辑删除 | `integer` | - | 是 | 0正常 1删除 |
| 8 | `isdefault` | 是否是默认值 | `char` | 1 | 是 | y:默认 |

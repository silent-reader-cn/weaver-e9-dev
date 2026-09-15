# 泛微OA 数据表: `mode_layout_querysql`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_layout_querysql`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | - |
| 2 | `modeid` | 模块id | `integer` | - | 是 | 对应modeinfo表中id |
| 3 | `formid` | 表单id | `integer` | - | 是 | - |
| 4 | `layoutid` | 布局id | `integer` | - | 是 | 对应布局表id |
| 5 | `detailtype` | 明细类型 | `integer` | - | 是 | - |
| 6 | `querytype` | 查询类型 | `integer` | - | 否 | - |
| 7 | `sqlconetent` | sql条件 | `varchar2` | 3000 | 是 | - |
| 8 | `javafilename` | java后处理文件 | `varchar2` | 1000 | 是 | 老数据使用 |
| 9 | `javafileaddress` | java后处理文件(新移植功能） | `varchar2` | 1000 | 是 | 新数据使用 |

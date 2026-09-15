# 泛微OA 数据表: `docsubcategory`

- **所属模块**: `知识管理`
- **数据库表名**: `docsubcategory`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `maincategoryid` | 主目录id | `integer` | - | 是 | - |
| 3 | `categoryname` | 分目录描述 | `varchar2` | 1000 | 是 | - |
| 4 | `subcategoryid` | 分目录id | `integer` | - | 否 | - |
| 5 | `seccategoryids` | 所有子目录id | `varchar2` | 1000 | 是 | - |
| 6 | `coder` | 分目录编码 | `varchar2` | 800 | 是 | - |
| 7 | `norepeatedname` | 禁止文档重名 | `integer` | - | 是 | 该分目录下禁止新建和修改出重名的文档 |
| 8 | `suborder` | 目录排序 | `float` | 22 | 是 | - |

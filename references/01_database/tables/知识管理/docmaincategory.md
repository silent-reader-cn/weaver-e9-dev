# 泛微OA 数据表: `docmaincategory`

- **所属模块**: `知识管理`
- **数据库表名**: `docmaincategory`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 由用户定义的主目录id | `integer` | - | 否 | 该id唯一 |
| 2 | `categoryname` | 主目录描述 | `varchar2` | 1000 | 是 | - |
| 3 | `categoryiconid` | 主目录图片的id | `integer` | - | 是 | 由sequenceindex表得到 |
| 4 | `categoryorder` | 主目录的显示顺序 | `float` | 22 | 是 | 可以有相同值 |
| 5 | `coder` | 主目录编码 | `varchar2` | 800 | 是 | - |
| 6 | `norepeatedname` | 禁止文档重名 | `integer` | - | 是 | 该主目录下禁止新建和修改出重名的文档 |
| 7 | `subcompanyid` | 分部id | `integer` | - | 是 | - |

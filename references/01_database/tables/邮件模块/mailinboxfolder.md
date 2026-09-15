# 泛微OA 数据表: `mailinboxfolder`

- **所属模块**: `邮件模块`
- **数据库表名**: `mailinboxfolder`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 主键 |
| 2 | `webfxtreeid` | 树节点id | `varchar2` | 1000 | 是 | - |
| 3 | `userid` | 用户id | `integer` | - | 是 | 文件夹所属人id |
| 4 | `foldername` | 文件夹名称 | `varchar2` | 1000 | 是 | 文件夹名称 |
| 5 | `parentid` | 父节点id | `integer` | - | 是 | - |
| 6 | `subcount` | 子节点数量 | `integer` | - | 是 | - |

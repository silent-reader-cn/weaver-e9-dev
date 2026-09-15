# 泛微OA 数据表: `recycle_shareinnerdoc`

- **所属模块**: `知识管理`
- **数据库表名**: `recycle_shareinnerdoc`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `sourceid` | 文档id | `integer` | - | 否 | - |
| 3 | `type` | 共享类型 | `integer` | - | 否 | - |
| 4 | `content` | 共享内容 | `integer` | - | 否 | - |
| 5 | `seclevel` | 安全级别 | `integer` | - | 否 | - |
| 6 | `sharelevel` | 共享级别 | `integer` | - | 否 | - |
| 7 | `srcfrom` | 来源于 | `integer` | - | 否 | - |
| 8 | `opuser` | 操作者 | `integer` | - | 否 | - |
| 9 | `sharesource` | 共享人员 | `integer` | - | 是 | - |
| 10 | `downloadlevel` | 下载级别 | `integer` | - | 是 | - |
| 11 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | - |
| 12 | `joblevel` | 岗位级别 | `char` | 10 | 否 | - |
| 13 | `jobdepartment` | 指定部门 | `char` | 10 | 否 | - |
| 14 | `jobsubcompany` | 指定分部 | `char` | 10 | 否 | - |

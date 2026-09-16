# 泛微OA 数据表: `diraccesscontroldetail`

- **中文名称**: 文档目录授权信息详细表
- **所属模块**: `知识管理`
- **数据库表名**: `diraccesscontroldetail`
- **主键**: `id`
- **字段数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `sourceid` | 目录id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `type` | 授权类型 | `integer` | - | 否 | 否 | 否 | - | - | 1部门＋安全级别<br>2角色＋级别＋安全级别<br>3安全级别<br>4用户类型＋安全级别<br>5人力资源<br>6分部+安全级别 |
| 4 | `content` | 授权内容 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `seclevel` | 安全级别 | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `sharelevel` | 授权级别 | `integer` | - | 否 | 否 | 否 | - | - | 0创建文档<br>1创建目录<br>2移动文档<br>3复制文档 |
| 7 | `sourcetype` | 目录类型 | `integer` | - | 否 | 否 | 否 | - | - | 0主目录<br>1分目录<br>2子目录 |
| 8 | `srcfrom` | 授权来源 | `integer` | - | 否 | 否 | 否 | - | - | 对应 diraccesscontrollist 中的 mainid |
| 9 | `seclevelmax` | 安全级别最大值 | `char` | 10 | 否 | 否 | 否 | - | 255 | - |
| 10 | `includesub` | 包含下级 | `char` | 10 | 是 | 否 | 否 | - | - | 是否含有下级 |
| 11 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 12 | `jobdepartment` | 岗位指定部门 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 13 | `jobsubcompany` | 岗位指定分部 | `integer` | - | 是 | 否 | 否 | - | 0 | - |
| 14 | `jobids` | 岗位 | `integer` | - | 是 | 否 | 否 | - | 0 | - |

# 泛微OA 数据表: `seccreaterdocpope`

- **所属模块**: `知识管理`
- **数据库表名**: `seccreaterdocpope`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `secid` | 目录id | `integer` | - | 否 | - |
| 3 | `pcreater` | 文档创建人权限 | `integer` | - | 否 | - |
| 4 | `pcreatermanager` | 文档创建人直接上级权限 | `integer` | - | 否 | - |
| 5 | `pcreaterjmanager` | 该字段停用 | `integer` | - | 否 | - |
| 6 | `pcreaterdownowner` | 该字段停用 | `integer` | - | 否 | - |
| 7 | `pcreatersubcomp` | 创建人本分部 | `integer` | - | 否 | - |
| 8 | `pcreaterdepart` | 创建人本部门 | `integer` | - | 否 | - |
| 9 | `pcreaterdownownerls` | 该字段停用 | `integer` | - | 否 | - |
| 10 | `pcreatersubcompls` | 创建人本分部最小安全级别 | `integer` | - | 否 | - |
| 11 | `pcreaterdepartls` | 创建人本部门最小安全级别 | `integer` | - | 否 | - |
| 12 | `pcreaterw` | 外部人员 文档创建人 | `integer` | - | 否 | - |
| 13 | `pcreatermanagerw` | 外部人员 创建人经理 | `integer` | - | 否 | - |
| 14 | `pcreaterjmanagerw` | 该字段停用 | `integer` | - | 否 | - |
| 15 | `docseccategorytemplateid` | 目录模板id | `integer` | - | 是 | - |
| 16 | `pcreaterdl` | 文档创建人下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |
| 17 | `pcreatermanagerdl` | 创建人经理下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |
| 18 | `pcreatersubcompdl` | 创建人本分部下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |
| 19 | `pcreaterdepartdl` | 创建人本部门下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |
| 20 | `pcreaterwdl` | 创建人直接上级下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |
| 21 | `pcreatermanagerwdl` | 创建人下载权限 | `integer` | - | 是 | 0：不可下载，1：可下载 |

# 泛微OA 数据表: `kq_groupmember`

- **所属模块**: `E9新版考勤表结构`
- **数据库表名**: `kq_groupmember`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键ID | `integer` | - | 否 | - |
| 2 | `type` | 成员类型 | `integer` | - | 否 | - |
| 3 | `typevalue` | 成员类型值 | `integer` | - | 否 | - |
| 4 | `alllevel` | 包含下级 | `integer` | - | 否 | - |
| 5 | `jobtitlelevel` | 岗位级别 | `integer` | - | 否 | - |
| 6 | `jobtitlelevelvalue` | 岗位级别值 | `integer` | - | 否 | - |
| 7 | `seclevel` | 安全级别最小值 | `integer` | - | 否 | - |
| 8 | `seclevelto` | 安全级别最大值 | `integer` | - | 否 | - |
| 9 | `groupid` | 考勤组ID | `integer` | - | 否 | - |
| 10 | `isDelete` | 是否删除 | `integer` | - | 否 | - |

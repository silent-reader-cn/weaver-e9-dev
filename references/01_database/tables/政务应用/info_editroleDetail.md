# 泛微OA 数据表: `info_editroleDetail`

- **所属模块**: `政务应用`
- **数据库表名**: `info_editroleDetail`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `pathid` | 路径id | `integer` | - | 是 | - |
| 4 | `sharetype` | 权限类型 | `integer` | - | 是 | 1人员、2部门、3分部、4角色、5所有人、6岗位 |
| 5 | `resourceid` | 人员id | `integer` | - | 是 | - |
| 6 | `rightid` | 采编角色主表id | `integer` | - | 是 | - |

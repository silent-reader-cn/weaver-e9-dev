# 泛微OA 数据表: `workplanReceiveScope`

- **所属模块**: `日程管理`
- **数据库表名**: `workplanReceiveScope`
- **字段总数**: `12`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | - | - |
| 2 | `baseId` | 关联基本信息ID | `integer` | - | - | - |
| 3 | `receiveType` | 接收人/创建人区分对象 | `integer` | - | - | 0:创建人  1:接收人 |
| 4 | `scopeType` | 范围类型 | `integer` | - | - | 1：指定人 2：分部 3：部门 4：角色 5：所有人 8: 岗位  9:本分部 10:本分部及下级分部 11:本部门  12:本部门及下级部门 13:所有下级 14:直接下级 |
| 5 | `seclevel` | 安全级别 | `integer` | - | - | - |
| 6 | `seclevelMax` | 安全级别 | `integer` | - | - | - |
| 7 | `objIds` | 对象/接收人ID | `varchar2` | 400 | - | - |
| 8 | `has_child` | 是否有下级 | `integer` | - | - | 0:没有  1:有 |
| 9 | `roleLevel` | 角色级别 | `integer` | - | - | - |
| 10 | `joblevel` | 岗位级别 | `integer` | - | - | - |
| 11 | `joblevelvalue` | 岗位范围 | `varchar2` | 500 | - | - |
| 12 | `createrId` | 创建人 | `integer` | - | - | - |

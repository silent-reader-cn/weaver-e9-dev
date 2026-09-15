# 泛微OA 数据表: `commreceivegroup`

- **所属模块**: `公文管理`
- **数据库表名**: `commreceivegroup`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 编号 | `integer` | - | 否 | - |
| 2 | `unitgroupid` | 组编号 | `integer` | - | 是 | - |
| 3 | `type` | 类型 | `integer` | - | 是 | - |
| 4 | `content` | 类型对应的ID | `integer` | - | 是 | - |
| 5 | `seclevelfrom` | 安全级别起 | `integer` | - | 是 | - |
| 6 | `seclevelto` | 安全级别起 | `integer` | - | 是 | - |
| 7 | `relatedlevel` | 选择角色时，后面对应的总部、分部、部门的ID | `varchar2` | 80 | 否 | - |
| 8 | `subcompanyid` | 岗位级别指定分部的ID | `varchar2` | 80 | 是 | - |
| 9 | `departmentid` | 岗位级别指定部门的ID | `varchar2` | 80 | 是 | - |
| 10 | `lowerlevel` | 是否包含下级 | `varchar2` | 80 | 否 | - |

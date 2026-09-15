# 泛微OA 数据表: `govern_prjsharedetail`

- **所属模块**: `政务应用`
- **数据库表名**: `govern_prjsharedetail`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `sourceid` | 数据id | `integer` | - | 否 | 对应govern_task表id |
| 3 | `categoryid` | 类型id | `integer` | - | 否 | - |
| 4 | `datatype` | 废弃字段 | `integer` | - | 是 | - |
| 5 | `type` | 权限类型 | `integer` | - | 是 | 权限类型1人员2分部3部门4角色5所有人6岗位 |
| 6 | `content` | 共享对象id | `integer` | - | 是 | - |
| 7 | `showlevel` | 安全级别下限 | `integer` | - | 是 | - |
| 8 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | - |
| 9 | `opttype` | 权限级别 | `integer` | - | 是 | 1查看2共享3管理4监控 |
| 10 | `isdefault` | 是否共享权限 | `integer` | - | 是 | 0前端用户共享 1设置生成 |
| 11 | `ruleid` | 权限id | `integer` | - | 否 | 对应govern_shareRule_XX表id |
| 12 | `higherlevel` | 上级关系 暂时不用 | `integer` | - | 是 | - |
| 13 | `rightid` | 权限id | `integer` | - | 否 | 对应govern_rightInfo id 仅默认共享有值 |
| 14 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0、部门；1、分部；2、总部； |
| 15 | `jobleveltext` | 岗位对象 | `varchar2` | 4000 | 是 | 逗号分隔的id串 |

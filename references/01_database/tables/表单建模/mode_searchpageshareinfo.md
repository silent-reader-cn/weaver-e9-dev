# 泛微OA 数据表: `mode_searchpageshareinfo`

- **中文名称**: 查询列表权限信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_searchpageshareinfo`
- **主键**: `id`
- **字段数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 2 | `pageid` | 查询列表id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_customsearch表的id |
| 3 | `righttype` | 权限级别 | `integer` | - | 是 | 否 | 否 | - | - | 1、查看；<br>4、监控； |
| 4 | `sharetype` | 权限类型 | `integer` | - | 是 | 否 | 否 | - | - | 1、人员；<br>2、分部；<br>3、部门；<br>4、角色；<br>5、所有人；<br>6、岗位； |
| 5 | `relatedid` | 共享对象id | `integer` | - | 是 | 否 | 否 | - | - | 如：共享对象为人员时，为人员的id，共享对象为部门时，为部门id，共享对象为岗位时，为岗位id |
| 6 | `rolelevel` | 共享级别(角色) | `integer` | - | 是 | 否 | 否 | - | - | 0、部门；<br>1、分部；<br>2、总部； |
| 7 | `showlevel` | 安全级别下限 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别范围最小值 |
| 8 | `layoutid` | 查看布局id | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 9 | `layoutid1` | 编辑布局id | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 10 | `layoutorder` | 布局优先级 | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 11 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别范围最大值 |
| 12 | `hrmcompanyvirtualtype` | 多维度组织结构id | `integer` | - | 是 | 否 | 否 | - | - | 保存多维度组织结构的id |
| 13 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 0、部门；<br>1、分部；<br>2、总部； |
| 14 | `jobleveltext` | 岗位级别指定对象id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 保存岗位级别对应的对象以逗号分隔的id串 |
| 15 | `browsersharetype` | 浏览框权限 | `integer` | - | 是 | 否 | 否 | - | - | 流程赋权插入权限 |

# 泛微OA 数据表: `Modedatashare_XXX_set`

- **所属模块**: `表单建模`
- **数据库表名**: `Modedatashare_XXX_set`
- **字段总数**: `23`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `browsersharetype` | 浏览框权限类型 | `integer` | - | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `sourceid` | 数据id | `integer` | - | 是 | 数据id，对应的是uf_xxx表中的id，也就是该权限模块的表的数据id |
| 4 | `righttype` | 权限级别 | `integer` | - | 是 | 0:新建;1:查看;2:编辑:3:完全控制;4:监控;5:批量导入;99:没有权限 |
| 5 | `sharetype` | 权限类型 | `integer` | - | 是 | 1,人员;2,分部;3,部门;4,角色;5,所有人;6,岗位;80:创建人本人;81,创建人直接上级;84,创建人分部;85,创建人部门;89,创建人所有上级;90,创建人本岗位 |
| 6 | `relatedid` | 共享对象id | `integer` | - | 是 | 如:共享对象为人员时，是人员的id，共享对象为部门时，是部门的id,共享对象为岗位时，是岗位的id |
| 7 | `rolelevel` | 共享级别(角色) | `integer` | - | 是 | 0:部门;1:分部;2:总部 |
| 8 | `showlevel` | 安全级别下限 | `integer` | - | 是 | 安全界别范围最小值 |
| 9 | `isdefault` | 是否默认共享 | `integer` | - | 是 | 0:非默认共享，为用户手动添加的共享;1:默认共享，根据模块设置的权限生成的权限 |
| 10 | `layoutid` | 查看布局id | `integer` | - | 是 | 对应的modehtmllayoutid表中的id |
| 11 | `layoutid1` | 编辑布局id | `integer` | - | 是 | 对应的modehtmllayoutid表中的id |
| 12 | `layoutorder` | 布局级别 | `integer` | - | 是 | 布局级别越小，优先级别越高 |
| 13 | `isrolelimited` | 是否受角色范围限制 | `integer` | - | 是 | 1:是;2:否;---受范围限制时，角色中的部分人员有权限，不受限制时，按照角色级别，角色中的所有人用于权限 |
| 14 | `rolefieldtype` | 字段类型（角色） | `integer` | - | 是 | 1:人员;2:部门;3:分部 |
| 15 | `rolefield` | 字段id（角色） | `integer` | - | 是 | 对应workflow_billfield表中的id，其中-101表示创建人，-102表示创建人部门，-103表示创建人分部 |
| 16 | `higherlevel` | 上级关系 | `integer` | - | 是 | 仅用在共享在模块主字段为人员时。1.创建人本人，2.创建人直接上级，3.创建人所有上级 |
| 17 | `rightid` | 模块权限设置id | `integer` | - | 是 | 模块权限设置id，对应moderightinfo表中的id |
| 18 | `requestid` | 流程id | `integer` | - | 是 | 对应的是流程的requestid |
| 19 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | 安全级别范围最大值 |
| 20 | `hrmcompanyvirtualtype` | 虚拟公司类型 | `integer` | - | 是 | - |
| 21 | `orgrelation` | 级别关系 | `integer` | - | 是 | - |
| 22 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0.部门，1.分部，2.总部 |
| 23 | `jobleveltext` | 岗位级别制定对象id | `varchar2` | 4000 | 是 | 保存岗位级别对应的对象以逗号分隔的id串 |

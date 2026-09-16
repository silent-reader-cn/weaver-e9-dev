# 泛微OA 数据表: `moderightinfo`

- **中文名称**: 模块权限设置表
- **所属模块**: `表单建模`
- **数据库表名**: `moderightinfo`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `browsersharetype` | 浏览框数据权限类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `javafileaddress` | java条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `id` | ID | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `modeid` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | 对应modeinfo表中的id |
| 5 | `righttype` | 权限级别 | `integer` | - | 是 | 否 | 否 | - | - | 0、新建；<br>1、查看；<br>2、编辑；<br>3、完全控制；<br>4、监控；<br>5、批量导入<br>99、没有权限 |
| 6 | `sharetype` | 权限类型 | `integer` | - | 是 | 否 | 否 | - | - | 1、人员；<br>2、分部；<br>3、部门；<br>4、角色；<br>5、所有人；<br>6、岗位；<br>80、创建人本人；<br>81、创建人直接上级<br>84、创建人分部<br>85、创建人部门<br>89、创建人所有上级<br>90、创建人本岗位 |
| 7 | `relatedid` | 共享对象id | `integer` | - | 是 | 否 | 否 | - | - | 如：共享对象为人员时，为人员的id，共享对象为部门时，为部门id，共享对象为岗位是，为岗位id |
| 8 | `rolelevel` | 共享级别(角色) | `integer` | - | 是 | 否 | 否 | - | - | 0、部门；<br>1、分部；<br>2、总部； |
| 9 | `showlevel` | 安全级别下限 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别范围最小值 |
| 10 | `javafilename` | java接口 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 仅用于拿实际表单创建的虚拟表单，模块的默认共享 |
| 11 | `layoutid` | 查看布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表中的id |
| 12 | `layoutid1` | 编辑布局id | `integer` | - | 是 | 否 | 否 | - | - | 对应modehtmllayout表中的id |
| 13 | `layoutorder` | 布局级别 | `integer` | - | 是 | 否 | 否 | - | - | 布局级别值越小，优先级越高 |
| 14 | `isrolelimited` | 是否受角色范围限制 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>2；否<br>受范围限制时，角色中的部分人员有权限，不受限制时按照角色级别，角色中的所有人用于权限 |
| 15 | `rolefieldtype` | 字段类型(角色) | `integer` | - | 是 | 否 | 否 | - | - | 1：人员<br>2：部门<br>3：分部 |
| 16 | `rolefield` | 字段id(角色) | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表中的id<br>其中-101表示创建人；-102表示创建人部门；-103表示创建人分部 |
| 17 | `higherlevel` | 上级关系 | `integer` | - | 是 | 否 | 否 | - | - | 仅用在共享在模块主字段为人员时。<br>1：创建人本人<br>2：创建人直接上级<br>3：创建人所有上级 |
| 18 | `importtype` | 导入类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：追加<br>2：覆盖<br>3：更新 |
| 19 | `conditiontype` | 权限条件类型 | `integer` | - | 是 | 否 | 否 | - | - | 1：普通类型<br>2：sql类型 |
| 20 | `conditionsql` | 权限条件sql | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 权限条件sql |
| 21 | `conditiontext` | 权限条件显示名 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 权限条件sql显示名称 |
| 22 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | 否 | 否 | - | - | 安全级别范围最大值 |
| 23 | `modifytime` | 安全级别范围最大值 21 | `varchar2` | 240 | 是 | 否 | 否 | - | - | 单条权限重构时间，次数据没有值时，单条权限重构不能显示，只有值时才会显示 |
| 24 | `hrmcompanyvirtualtype` | 多维度组织结构id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 保存多维度组织结构的id |
| 25 | `orgrelation` | 关联 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `joblevel` | 岗位级别 | `integer` | - | 是 | 否 | 否 | - | - | 0、部门；<br>1、分部；<br>2、总部； |
| 27 | `jobleveltext` | 岗位级别指定对象id | `varchar2` | 4000 | 是 | 否 | 否 | - | - | 保存岗位级别对应的对象以逗号分隔的id串 |

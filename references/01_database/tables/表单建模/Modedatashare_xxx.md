# 泛微OA 数据表: `Modedatashare_xxx`

- **所属模块**: `表单建模`
- **数据库表名**: `Modedatashare_xxx`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `browsersharetype` | 浏览框权限类型 | `integer` | - | 是 | - |
| 2 | `id` | id | `integer` | - | 否 | - |
| 3 | `sourceid` | 数据id | `integer` | - | 是 | 数据id，对应模块中设置的uf_xxx表中的id |
| 4 | `type` | 权限类型 | `integer` | - | 是 | 1、人员；  2、分部；  3、部门；  4、角色；  5、所有人；  6、岗位；  80、创建人本人；  81、创建人直接上级  84、创建人分部  85、创建人部门  89、创建人所有上级 90、创建人本岗位 |
| 5 | `content` | 共享对象id | `integer` | - | 是 | 如：共享对象为人员时，为人员的id，共享对象为部门时，为部门id，共享对象为岗位时，为岗位id |
| 6 | `seclevel` | 安全级别下限 | `integer` | - | 是 | 安全级别范围最小值 |
| 7 | `sharelevel` | 权限级别 | `integer` | - | 是 | 1、查看； 2、编辑； 3、完全控制 |
| 8 | `srcfrom` | 权限类型 | `integer` | - | 是 | 1、人员；  2、分部；  3、部门；  4、角色；  5、所有人；  6、岗位；  80、创建人本人；  81、创建人直接上级  84、创建人分部  85、创建人部门  89、创建人所有上级 90、创建人本岗位 |
| 9 | `opuser` | 操作人 | `integer` | - | 是 | 一般值和content相同，没有太大意义 |
| 10 | `isdefault` | 是否默认共享 | `integer` | - | 是 | 0：非默认共享，为用户自己手动添加的共享；1：默认共享，根据模块设置的权限生成的权限 |
| 11 | `layoutid` | 查看布局id | `integer` | - | 是 | 对应modehtmllayout表中的id |
| 12 | `layoutid1` | 编辑布局id | `integer` | - | 是 | 对应modehtmllayout表中的id |
| 13 | `layoutorder` | 布局级别 | `integer` | - | 是 | 布局级别值越小，优先级越高 |
| 14 | `sharesetid` | 建模数据权限规则id（角色） | `integer` | - | 是 | 仅在角色受权限控制值，此字段才会有值，对应modedatashare_xxx_set表中的id |
| 15 | `higherlevel` | 上级关系 | `integer` | - | 是 | 仅用在共享在模块主字段为人员时。  1：创建人本人  2：创建人直接上级  3：创建人所有上级 |
| 16 | `setid` | 建模数据权限规则Id | `integer` | - | 是 | 对应modedatashare_xxx_set表中的id |
| 17 | `rightid` | 模块权限设置id | `integer` | - | 是 | 模块权限设置id，对应moderightinfo表中的id |
| 18 | `requestid` | 流程id | `integer` | - | 是 | 流程requestid |
| 19 | `showlevel2` | 安全级别上限 | `integer` | - | 是 | 安全级别范围最大值 |
| 20 | `joblevel` | 岗位级别 | `integer` | - | 是 | 0、部门； 1、分部； 2、总部； |
| 21 | `jobleveltext` | 岗位级别指定对象id | `varchar2` | 4000 | 是 | 保存岗位级别对应的对象以逗号分隔的id串 |

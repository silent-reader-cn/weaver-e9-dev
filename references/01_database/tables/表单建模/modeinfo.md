# 泛微OA 数据表: `modeinfo`

- **中文名称**: 模块基本信息表
- **所属模块**: `表单建模`
- **数据库表名**: `modeinfo`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `empowmenttype` | 自定义目录 | `varchar2` | 10 | 是 | 否 | 否 | - | - | 值由逗号分隔，逗号前0表示临时赋权，1表示插入赋权，逗号后0表示未做自定义配置，1表示做了自定义配置 |
| 2 | `id` | 模块id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `modename` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `modedesc` | 描述 | `varchar2` | 1200 | 是 | 否 | 否 | - | - | - |
| 5 | `modetype` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应表modetreefield中的id |
| 6 | `formid` | 表单 | `integer` | - | 是 | 否 | 否 | - | - | 对应表workflow_bill中的id,表单建模中使用的表单一般都是自定义表单，formid的值一般都是小于0的整数 |
| 7 | `maincategory` | 附件上传1级目录 | `integer` | - | 是 | 否 | 否 | - | - | 附件上传目录，字段maincategory、subcategory和seccategory结合使用，共同组成附件上传目录 |
| 8 | `subcategory` | 附件上传2级目录 | `integer` | - | 是 | 否 | 否 | - | - | 同上 |
| 9 | `seccategory` | 附件上传3级目录 | `integer` | - | 是 | 否 | 否 | - | - | 同上 |
| 10 | `isimportdetail` | 允许创建时导入明细 | `integer` | - | 是 | 否 | 否 | - | - | 勾选此选项可以在新建时，使用excel导入明细 |
| 11 | `codeid` | 勾选此选项可以在新建时，使用excel导入明细 10 | `integer` | - | 是 | 否 | 否 | - | - | 编码id(暂保留) |
| 12 | `custompage` | 编码id(暂保留) 11 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 自定义页面地址，二次开发使用 |
| 13 | `defaultshared` | 是否允许修改默认共享 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不允许<br>1：允许<br>允许时，有完全控制权限的用户可以新增或删除默认共享 |
| 14 | `nondefaultshared` | 是否允许修改非默认共享 | `char` | 1 | 是 | 否 | 否 | - | - | 0：不允许<br>1：允许<br>允许时，有完全控制权限的用户可以新增或删除非默认共享 |
| 15 | `dsporder` | 显示顺序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 16 | `modecode` | 15 | `varchar2` | 256 | 是 | 否 | 否 | - | - | 32位uuid，导入模块时的唯一识别判断 |
| 17 | `isdelete` | 是否逻辑删除 | `integer` | - | 是 | 否 | 否 | - | - | 0：未删除<br>1：已删除<br>已删除的模块不会显示出来 |
| 18 | `subcompanyid` | 所属分部 | `integer` | - | 是 | 否 | 否 | - | - | 对应表hrmsubcompany中的id字段，用于表单建模分权功能 |
| 19 | `isallowreply` | 是否允许回复 | `integer` | - | 是 | 否 | 否 | - | - | 0：不允许回复<br>1：允许回复 |
| 20 | `categorytype` | 附件上传目录类型 | `integer` | - | 是 | 否 | 否 | - | - | 0：固定目录<br>1：选择目录 |
| 21 | `selectcategory` | 选择框字段id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 22 | `fileformat` | 福建字段 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 23 | `isaddrightbyworkflow` | 是否流程赋权 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `istagset` | 是否开启标签 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 25 | `replyposition` | 回复评论 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `iswatermark` | 是否水印 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `isimportdetailofeditlayout` | 是否明细导入 | `integer` | - | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `modeinfo`

- **所属模块**: `表单建模`
- **数据库表名**: `modeinfo`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `empowmenttype` | 自定义目录 | `varchar2` | 10 | 是 | 值由逗号分隔，逗号前0表示临时赋权，1表示插入赋权，逗号后0表示未做自定义配置，1表示做了自定义配置 |
| 2 | `id` | 模块id | `integer` | - | 是 | - |
| 3 | `modename` | 名称 | `varchar2` | 1000 | 是 | - |
| 4 | `modedesc` | 描述 | `varchar2` | 1200 | 是 | - |
| 5 | `modetype` | 所属应用 | `integer` | - | 是 | 对应表modetreefield中的id |
| 6 | `formid` | 表单 | `integer` | - | 是 | 对应表workflow_bill中的id,表单建模中使用的表单一般都是自定义表单，formid的值一般都是小于0的整数 |
| 7 | `maincategory` | 附件上传1级目录 | `integer` | - | 是 | 附件上传目录，字段maincategory、subcategory和seccategory结合使用，共同组成附件上传目录 |
| 8 | `subcategory` | 附件上传2级目录 | `integer` | - | 是 | 同上 |
| 9 | `seccategory` | 附件上传3级目录 | `integer` | - | 是 | 同上 |
| 10 | `isimportdetail` | 允许创建时导入明细 | `integer` | - | 是 | 勾选此选项可以在新建时，使用excel导入明细 |
| 11 | `codeid` | 勾选此选项可以在新建时，使用excel导入明细         10 | `integer` | - | 是 | 编码id(暂保留) |
| 12 | `custompage` | 编码id(暂保留)         11 | `varchar2` | 1000 | 是 | 自定义页面地址，二次开发使用 |
| 13 | `defaultshared` | 是否允许修改默认共享 | `char` | 1 | 是 | - |

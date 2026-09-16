# 泛微OA 数据表: `mode_customsearch`

- **中文名称**: 查询基本信息表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_customsearch`
- **主键**: `id`
- **字段数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `iswatermark` | 水印信息 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `sliderpercentage` | 滑块显示占比 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `isshowquerycondition` | 是否展开查询条件 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `javafileaddress` | java查询条件 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `modeid` | 模块名称 | `integer` | - | 是 | 否 | 否 | - | - | 模块id，对应modeinfo表的id |
| 7 | `customname` | 名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 8 | `customdesc` | 描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 9 | `defaultsql` | 固定查询条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | sql类型的查询条件sqlwhere |
| 10 | `disquicksearch` | 隐藏快捷搜索 | `integer` | - | 是 | 否 | 否 | - | - | 1：隐藏<br>0：不隐藏 |
| 11 | `opentype` | 数据打开方式 | `integer` | - | 是 | 否 | 否 | - | - | 0：弹出窗口<br>1：默认窗口 |
| 12 | `norightlist` | 无权限列表 | `char` | 1 | 是 | 否 | 否 | - | 0 | 1：无权限列表<br>0：不是无权限列表<br>无权限列表：表示查询列表显示出的数据为所有模块的数据，不受是否有权限控制 |
| 13 | `searchconditiontype` | 查询条件类型 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 1：sql<br>2：java |
| 14 | `javafilename` | where条件java类 | `varchar2` | 800 | 是 | 否 | 否 | - | - | where条件类型为java时，可以在java中返回where条件 |
| 15 | `pagenumber` | 每页显示记录数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 16 | `formid` | 表单名称 | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_bill表的id |
| 17 | `appid` | 所属应用 | `integer` | - | 是 | 否 | 否 | - | - | 对应modetreefield表的id |
| 18 | `dsporder` | 显示顺序 | `float` | 22 | 是 | 否 | 否 | - | - | - |
| 19 | `detailtable` | 子表 | `varchar2` | 480 | 是 | 否 | 否 | - | - | 子表的数据库表名 |
| 20 | `customsearchcode` | 32位uuid | `varchar2` | 256 | 是 | 否 | 否 | - | - | 唯一识别，主要用着应用导入导出是查询列表的导入导出 |
| 21 | `iscustom` | 自定义列宽/每页显示条数 | `integer` | - | 否 | 否 | 否 | - | 1 | - |

# 泛微OA 数据表: `docfrontpage`

- **中文名称**: 新闻页设置表
- **所属模块**: `知识管理`
- **数据库表名**: `docfrontpage`
- **主键**: `id`
- **字段数**: `29`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `frontpagename` | 新闻页名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 3 | `frontpagedesc` | 新闻页描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `isactive` | 是否活跃 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 5 | `departmentid` | 链接的部门id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 6 | `linktype` | 链接的种类 | `varchar2` | 2 | 是 | 否 | 否 | - | - | 0:部门<br>1:e-document<br>2:e-hrm<br>3:e-finance<br>4:e-crm<br>5:e-project<br>6:e-erp<br>7:customer<br>8:visiter<br>9:reseller<br>10:supplier |
| 7 | `hasdocsubject` | 是否显示文档主题 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 8 | `hasfrontpagelist` | 是否显示新闻页列表 | `char` | 1 | 是 | 否 | 否 | - | - | 0:否，1:是 |
| 9 | `newsperpage` | 每页新闻个数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `titlesperpage` | 每页标题新闻个数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `defnewspicid` | 默认的新闻图片id | `integer` | - | 是 | 否 | 否 | - | - | 即上传图片表中的id |
| 12 | `backgroundpicid` | 默认的背景图片id | `integer` | - | 是 | 否 | 否 | - | - | 即上传图片表中的id |
| 13 | `headerdocid` | 作为页眉的文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `footerdocid` | 作为页脚的文档id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 15 | `secopt` | 条件中安全级别选项 | `varchar2` | 16 | 是 | 否 | 否 | - | - | >=：大于或者等于<br><=：小于或者等于<br>=：等于 |
| 16 | `seclevelopt` | 条件中选定的安全级别 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 17 | `departmentopt` | 条件中选定的部门 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 18 | `dateopt` | 条件中选定的日期 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 19 | `languageopt` | 条件中选定的语言 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `clauseopt` | 输入的条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 21 | `newsclause` | 选为该新闻页文档的条件 where子句 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 22 | `languageid` | 语言的id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `publishtype` | 发布类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `importdocid` | 作为要闻的文档id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `newstypeid` | 新闻类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `typeordernum` | 类型排序个数 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 27 | `checkoutstatus` | 签出状态 | `integer` | - | 是 | 否 | 否 | - | - | 1：自动签出，0或其它：未签出 |
| 28 | `checkoutuserid` | 签出人id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 29 | `subcompanyid` | 分部 | `integer` | - | 是 | 否 | 否 | - | - | - |

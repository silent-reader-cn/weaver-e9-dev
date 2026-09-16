# 泛微OA 数据表: `mode_customdspfield`

- **中文名称**: 查询列表字段信息
- **所属模块**: `表单建模`
- **数据库表名**: `mode_customdspfield`
- **主键**: `id`
- **字段数**: `28`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `shownamelabel` | 显示转换 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 2 | `alignment` | 对齐方式 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 3 | `ismaplocation` | 开启地图 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 4 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | - |
| 5 | `customid` | 查询id | `integer` | - | 是 | 否 | 否 | - | - | 对应mode_customsearch表的id |
| 6 | `fieldid` | 字段id | `integer` | - | 是 | 否 | 否 | - | - | 对应workflow_billfield表的id |
| 7 | `isquery` | 是否查询条件 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 8 | `isshow` | 是否显示 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 9 | `showorder` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | 查询列表里字段的显示顺序 |
| 10 | `queryorder` | 查询条件显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | 在查询条件中，字段的显示顺序 |
| 11 | `istitle` | 链接字段 | `char` | 1 | 是 | 否 | 否 | - | - | 0：否<br>1：表单建模<br>2：工作流程<br>3：自定义 |
| 12 | `colwidth` | 列宽 | `number` | (15,2) | 是 | 否 | 否 | - | - | - |
| 13 | `isorder` | 是否排序 | `integer` | - | 是 | 否 | 否 | - | - | 1：排序<br>0：不排序 |
| 14 | `ordertype` | 排序类型 | `varchar2` | 800 | 是 | 否 | 否 | - | - | n：--<br>0：不能排序<br>a：默认升序<br>d；默认降序 |
| 15 | `ordernum` | 默认排序优先级 | `integer` | - | 是 | 否 | 否 | - | - | 默认排序优先级，值越小，优先级越高 |
| 16 | `isstat` | 是否统计 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 17 | `iskey` | 是否关键字查询字段 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否<br>设置为关键字字段后，可作为查询列表右上角的快速搜索框 |
| 18 | `isorderfield` | 是否排序字段 | `integer` | - | 是 | 否 | 否 | - | - | 作废 |
| 19 | `priorder` | 作废 13 | `char` | 4 | 是 | 否 | 否 | - | - | 作废 |
| 20 | `hreflink` | 链接地址 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 21 | `showmethod` | 是否显示方式 | `integer` | - | 是 | 否 | 否 | - | - | 1：显示转换<br>0：不转换<br>只有select框字段才能进行显示转换 |
| 22 | `isgroup` | 是否分组 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 23 | `searchparaname` | 条件参数 | `varchar2` | 400 | 是 | 否 | 否 | - | - | 条件参数 |
| 24 | `searchparaname1` | 条件参数1 | `varchar2` | 400 | 是 | 否 | 否 | - | - | - |
| 25 | `isadvancedquery` | 是否高级查询字段 | `char` | 1 | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 26 | `advancedqueryorder` | 高级查询条件显示顺序 | `integer` | - | 否 | 否 | 否 | - | 0 | - |
| 27 | `conditiontransition` | 显示转换条件 | `integer` | - | 是 | 否 | 否 | - | - | 1：是<br>0：否 |
| 28 | `editable` | 批量修改表 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |

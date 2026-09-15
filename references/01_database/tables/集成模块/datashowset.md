# 泛微OA 数据表: `datashowset`

- **所属模块**: `集成模块`
- **数据库表名**: `datashowset`
- **字段总数**: `34`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 修改日期 |
| 2 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 修改时间 |
| 3 | `sqltext1` | 条件1查询 | `varchar2` | 4000 | 是 | 条件1查询 |
| 4 | `sqltext2` | 条件2查询 | `varchar2` | 4000 | 是 | 条件2查询 |
| 5 | `nameheader` | 列1显示名 | `varchar2` | 4000 | 是 | 列1显示名 |
| 6 | `descriptionheader` | 列2显示名 | `varchar2` | 4000 | 是 | 列2显示名 |
| 7 | `wsworkname` | WebService空间名 | `varchar2` | 1000 | 是 | WebService空间名 |
| 8 | `id` | ID | `integer` | - | 否 | 自增长主键 |
| 9 | `showname` | 自定义浏览框标识 | `varchar2` | 1000 | 是 | 浏览框的唯一标识 |
| 10 | `showclass` | 展现类型 | `char` | 1 | 是 | 1 浏览框 2 查询页面 |
| 11 | `datafrom` | 数据来源 | `char` | 1 | 是 | 0 webservice ； 1  数据库 ；2 自定义地址 |
| 12 | `datasourceid` | 数据源 | `varchar2` | 800 | 是 | 数据源 |
| 13 | `sqltext` | 无条件查询 | `varchar2` | 4000 | 是 | 无条件查询 |
| 14 | `wsurl` | webservice地址 | `varchar2` | 1000 | 是 | webservice地址 |
| 15 | `wsoperation` | webservice接口方法 | `varchar2` | 1000 | 是 | webservice接口方法 |
| 16 | `xmltext` | xml文本 | `varchar2` | 4000 | 是 | xml文本 |
| 17 | `inpara` | 输入参数 | `varchar2` | 1000 | 是 | 输入参数 |
| 18 | `showtype` | 展现方式 | `char` | 1 | 是 | 1 列表式 ；2 树形； 3 自定义页面 |
| 19 | `keyfield` | 关键字段 | `varchar2` | 800 | 是 | 关键字段 |
| 20 | `parentfield` | 上级字段名 | `varchar2` | 1000 | 是 | 上级字段名 |
| 21 | `showfield` | 显示标题 | `varchar2` | 1000 | 是 | 显示标题 |
| 22 | `detailpageurl` | 链接地址 | `varchar2` | 1000 | 是 | 链接地址 |
| 23 | `typename` | 类型名称 | `char` | 1 | 是 | 类型名称 |
| 24 | `selecttype` | 选择类型 | `char` | 1 | 是 | 选择类型 |
| 25 | `showpageurl` | 外部页面地址 | `varchar2` | 1000 | 是 | 外部页面地址 |
| 26 | `browserfrom` | 浏览框来源方式 | `integer` | - | 是 | 0 E8之前 ； 1 建模浏览框 ；2 E8自定义浏览框 |
| 27 | `name` | 显示名称 | `varchar2` | 1000 | 是 | 显示名称 |
| 28 | `customid` | 浏览框id | `integer` | - | 是 | 对应mode_custombrowser表的id，且只有通过表单建模创建出的浏览框，此id才不为空 |
| 29 | `customhref` | 自定义地址 | `varchar2` | 4000 | 是 | 自定义地址 |
| 30 | `searchbyname` | 条件2查询 | `varchar2` | 4000 | 是 | 条件2查询 |
| 31 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 创建日期 |
| 32 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 创建时间 |
| 33 | `searchbyid` | 条件1查询 | `varchar2` | 4000 | 是 | 条件1查询 |
| 34 | `onlylowestnode` | 只能选最下级节点 | `varchar2` | 2 | 是 | 树形浏览框用:开关控制只选最下级节点 |

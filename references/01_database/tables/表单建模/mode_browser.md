# 泛微OA 数据表: `mode_browser`

- **中文名称**: 浏览按钮基础表
- **所属模块**: `表单建模`
- **数据库表名**: `mode_browser`
- **主键**: `id`
- **字段数**: `33`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `createdate` | 创建日期 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 2 | `createtime` | 创建时间 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 3 | `modifydate` | 更改日期 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 4 | `modifytime` | 更改时间 | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 5 | `id` | id | `integer` | - | 否 | 否 | 否 | - | - | - |
| 6 | `showname` | 显示名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `showclass` | java条件class | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 8 | `datafrom` | 数据源 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 9 | `datasourceid` | 数据id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 10 | `sqltext` | 条件 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 11 | `wsurl` | 外部接口url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 12 | `wsoperation` | 接口操作者 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 13 | `xmltext` | xml内容 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 14 | `inpara` | 参数 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 15 | `showtype` | 展现类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 16 | `keyfield` | 主键 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 17 | `parentfield` | 父字段 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 18 | `showfield` | 显示字段 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 19 | `detailpageurl` | 明细表页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 20 | `typename` | 类型名称 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 21 | `selecttype` | 选择类型 | `char` | 1 | 是 | 否 | 否 | - | - | - |
| 22 | `showpageurl` | 显示页面url | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 23 | `browserfrom` | 浏览框来源 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 24 | `name` | 名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 25 | `customid` | 查询id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `customhref` | 查询链接 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 27 | `sqltext1` | 条件1 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 28 | `sqltext2` | 条件2 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 29 | `nameheader` | 头名称 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 30 | `descriptionheader` | 详细描述 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 31 | `wsworkname` | 接口工作名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 32 | `searchbyid` | 条件1 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |
| 33 | `searchbyname` | 条件2 | `varchar2` | 4000 | 是 | 否 | 否 | - | - | - |

# 泛微OA 数据表: `hp_mobile_hpinfo`

- **中文名称**: 移动门户主页信息表
- **所属模块**: `门户管理`
- **数据库表名**: `hp_mobile_hpinfo`
- **主键**: `id`
- **字段数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `publishid` | 发布id | `varchar2` | 800 | 是 | 否 | 否 | - | - | - |
| 2 | `id` | 主键（主页id） | `integer` | - | 否 | 否 | 否 | - | - | - |
| 3 | `infoname` | 主页名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 4 | `infodesc` | 描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 5 | `styleid` | 样式id | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 6 | `picstyleid` | 图片样式ID | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |
| 7 | `layoutid` | 布局id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 8 | `subcompanyid` | 分部id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 9 | `isuse` | 是否使用 | `integer` | - | 是 | 否 | 否 | - | 1 | - |
| 10 | `creatortype` | 创建者类型 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `creatorid` | 创建者 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 12 | `parenthpid` | 父门户页面id | `integer` | - | 是 | 否 | 否 | - | - | - |
| 13 | `ordernum` | 排序 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 14 | `hplanuageid` | 多语言id | `integer` | - | 是 | 否 | 否 | - | 7 | - |
| 15 | `hpcreatorid` | 门户创建者id | `integer` | - | 是 | 否 | 否 | - | 1 | - |
| 16 | `hplastdate` | 门户最后更新日期 | `date` | 7 | 是 | 否 | 否 | - | - | - |
| 17 | `hplasttime` | 门户最后更新时间 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | - |

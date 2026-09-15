# 泛微OA 数据表: `prj_searchmould`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_searchmould`
- **字段总数**: `24`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `mouldname` | 模板名称 | `varchar2` | 1000 | 是 | 模板名称 |
| 3 | `userid` | 用户id | `integer` | - | 是 | 用户id |
| 4 | `prjid` | 项目id | `integer` | - | 是 | 项目id |
| 5 | `status` | 状态 | `varchar2` | 480 | 是 | 状态 |
| 6 | `prjtype` | 项目类型 | `varchar2` | 480 | 是 | 项目类型 |
| 7 | `worktype` | 工作类型 | `varchar2` | 480 | 是 | 工作类型 |
| 8 | `nameopt` | 名称(包含) | `integer` | - | 是 | 名称(包含) |
| 9 | `name` | 名称 | `varchar2` | 480 | 是 | 名称 |
| 10 | `description` | 备注 | `varchar2` | 1000 | 是 | 备注 |
| 11 | `customer` | 客户 | `integer` | - | 是 | 客户 |
| 12 | `parent` | 上级项目 | `integer` | - | 是 | 上级项目 |
| 13 | `securelevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 14 | `department` | 部门 | `integer` | - | 是 | 部门 |
| 15 | `manager` | 项目经理 | `integer` | - | 是 | 项目经理 |
| 16 | `member` | 项目成员 | `integer` | - | 是 | 项目成员 |
| 17 | `procode` | 项目编码 | `varchar2` | 800 | 是 | 项目编码 |
| 18 | `startdatefrom` | 开始日期(从) | `char` | 10 | 是 | 开始日期(从) |
| 19 | `startdateto` | 开始日期(至) | `char` | 10 | 是 | 开始日期(至) |
| 20 | `enddatefrom` | 结束日期(从) | `char` | 10 | 是 | 结束日期(从) |
| 21 | `enddateto` | 结束日期(至) | `char` | 10 | 是 | 结束日期(至) |
| 22 | `finish` | 进度(从) | `integer` | - | 是 | 进度(从) |
| 23 | `finish1` | 进度(至) | `integer` | - | 是 | 进度(至) |
| 24 | `subcompanyid1` | 分部 | `integer` | - | 是 | 分部 |

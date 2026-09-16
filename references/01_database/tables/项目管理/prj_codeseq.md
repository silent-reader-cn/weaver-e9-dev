# 泛微OA 数据表: `prj_codeseq`

- **中文名称**: 项目编码配置
- **所属模块**: `项目管理`
- **数据库表名**: `prj_codeseq`
- **主键**: `id`
- **字段数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 否 | 否 | - | - | 标识列 |
| 2 | `sequenceid` | 流水号 | `integer` | - | 是 | 否 | 否 | - | - | 流水号 |
| 3 | `subcompanyid` | 分部 | `integer` | - | 是 | 否 | 否 | - | - | 分部 |
| 4 | `departmentid` | 部门 | `integer` | - | 是 | 否 | 否 | - | - | 部门 |
| 5 | `capitalgroupid` | 项目类型 | `integer` | - | 是 | 否 | 否 | - | - | 项目类型 |
| 6 | `capitaltypeid` | 工作类型 | `integer` | - | 是 | 否 | 否 | - | - | 工作类型 |
| 7 | `buydateyear` | 年 | `integer` | - | 是 | 否 | 否 | - | - | 年 |
| 8 | `buydatemonth` | 月 | `integer` | - | 是 | 否 | 否 | - | - | 月 |
| 9 | `buydateday` | 日 | `integer` | - | 是 | 否 | 否 | - | - | 日 |
| 10 | `warehouseyear` | 备用字段 | `integer` | - | 是 | 否 | 否 | - | - | 备用字段 |
| 11 | `warehousemonth` | 备用字段 | `integer` | - | 是 | 否 | 否 | - | - | 备用字段 |
| 12 | `warehouseday` | 备用字段 | `integer` | - | 是 | 否 | 否 | - | - | 备用字段 |
| 13 | `assetid` | 备用字段 | `integer` | - | 是 | 否 | 否 | - | - | 备用字段 |

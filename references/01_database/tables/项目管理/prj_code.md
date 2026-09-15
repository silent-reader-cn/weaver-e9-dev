# 泛微OA 数据表: `prj_code`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_code`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `isuse` | 编码方式 | `integer` | - | 是 | 编码方式 |
| 3 | `subcompanyflow` | 分部流水 | `varchar2` | 80 | 是 | 分部流水 |
| 4 | `departmentflow` | 部门流水 | `varchar2` | 80 | 是 | 部门流水 |
| 5 | `capitalgroupflow` | 项目类型流水 | `varchar2` | 80 | 是 | 项目类型流水 |
| 6 | `capitaltypeflow` | 工作类型流水 | `varchar2` | 80 | 是 | 工作类型流水 |
| 7 | `buydateflow` | 日期流水 | `varchar2` | 80 | 是 | 日期流水 |
| 8 | `warehousingflow` | 备用字段 | `varchar2` | 80 | 是 | 备用字段 |
| 9 | `startcodenum` | 起始流水号 | `integer` | - | 是 | 起始流水号 |
| 10 | `assetdataflow` | 备用字段 | `varchar2` | 80 | 是 | 备用字段 |

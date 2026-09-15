# 泛微OA 数据表: `hrmresourceotherinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmresourceotherinfo`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `infoname` | 信息主题 | `varchar2` | 800 | 是 | 信息主题 |
| 4 | `startdate` | 相关起始日期 | `char` | 10 | 是 | 相关起始日期 |
| 5 | `enddate` | 相关结束日期 | `char` | 10 | 是 | 相关结束日期 |
| 6 | `docid` | 相关文档id | `integer` | - | 是 | 相关文档id |
| 7 | `inforemark` | 备注 | `varchar2` | 4000 | 是 | 备注 |
| 8 | `infotype` | 信息种类 | `integer` | - | 是 | 信息种类 |
| 9 | `seclevel` | 安全级别 | `integer` | - | 是 | 安全级别 |
| 10 | `createid` | 创建人id | `integer` | - | 是 | 创建人id |
| 11 | `createdate` | 创建日期 | `char` | 10 | 是 | 创建日期 |
| 12 | `lastmoderid` | 最后修改人id | `integer` | - | 是 | 最后修改人id |
| 13 | `lastmoddate` | 最后修改日期 | `char` | 10 | 是 | 最后修改日期 |

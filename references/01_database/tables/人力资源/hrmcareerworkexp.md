# 泛微OA 数据表: `hrmcareerworkexp`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmcareerworkexp`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `ftime` | 工作开始日期 | `char` | 10 | 是 | 工作开始日期 |
| 3 | `ttime` | 工作结束日期 | `char` | 10 | 是 | 工作结束日期 |
| 4 | `company` | 工作公司 | `varchar2` | 800 | 是 | 工作公司 |
| 5 | `jobtitle` | 工作职务 | `varchar2` | 800 | 是 | 工作职务 |
| 6 | `workdesc` | 工作描述 | `varchar2` | 4000 | 是 | 工作描述 |
| 7 | `applyid` | 应聘人id | `integer` | - | 是 | hrmcareerapply表应聘人id |

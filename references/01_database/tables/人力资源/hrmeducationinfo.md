# 泛微OA 数据表: `hrmeducationinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmeducationinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `startdate` | 开始时间 | `char` | 10 | 是 | 开始时间 |
| 4 | `enddate` | 结束时间 | `char` | 10 | 是 | 结束时间 |
| 5 | `school` | 学校 | `varchar2` | 800 | 是 | 学校 |
| 6 | `speciality` | 专业 | `varchar2` | 480 | 是 | 专业 |
| 7 | `educationlevel` | 学历 | `integer` | - | 是 | - |

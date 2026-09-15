# 泛微OA 数据表: `hrmtrainbeforework`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmtrainbeforework`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | 人员id |
| 3 | `trainname` | 培训名称 | `varchar2` | 480 | 是 | 培训名称 |
| 4 | `trainresource` | 培训单位 | `varchar2` | 480 | 是 | 培训单位 |
| 5 | `trainstartdate` | 培训开始日期 | `char` | 10 | 是 | 培训开始日期 |
| 6 | `trainenddate` | 培训结束日期 | `char` | 10 | 是 | 培训结束日期 |
| 7 | `trainmemo` | 备注 | `varchar2` | 4000 | 是 | 备注 |

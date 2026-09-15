# 泛微OA 数据表: `hrmfamilyinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmfamilyinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `resourceid` | 人力资源id | `integer` | - | 是 | 人力资源id |
| 3 | `member` | 家庭成员 | `varchar2` | 240 | 是 | 家庭成员 |
| 4 | `title` | 称谓 | `varchar2` | 240 | 是 | 称谓 |
| 5 | `company` | 工作单位 | `varchar2` | 800 | 是 | 工作单位 |
| 6 | `jobtitle` | 职位 | `varchar2` | 800 | 是 | 职位 |
| 7 | `address` | 地址 | `varchar2` | 800 | 是 | 地址 |

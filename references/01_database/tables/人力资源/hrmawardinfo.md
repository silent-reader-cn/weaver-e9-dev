# 泛微OA 数据表: `hrmawardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmawardinfo`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `rptitle` | 奖惩主题 | `varchar2` | 480 | 是 | 奖惩主题 |
| 3 | `rptypeid` | 奖惩种类 | `integer` | - | 是 | 奖惩种类 |
| 4 | `rpdate` | 奖惩日期 | `char` | 10 | 是 | 奖惩日期 |
| 5 | `rpexplain` | 奖惩原因 | `varchar2` | 1000 | 是 | 奖惩原因 |
| 6 | `rptransact` | 奖惩措施 | `varchar2` | 1000 | 是 | 奖惩措施 |
| 7 | `resourseid` | 奖惩人员 | `varchar2` | 4000 | 是 | 奖惩人员 |

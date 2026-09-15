# 泛微OA 数据表: `bill_hrmawardinfo`

- **所属模块**: `人力资源`
- **数据库表名**: `bill_hrmawardinfo`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | ID |
| 2 | `rptitle` | 奖惩标题 | `varchar2` | 480 | 是 | 奖惩标题 |
| 3 | `resource_n` | 员工id | `integer` | - | 是 | 员工id |
| 4 | `rpdate` | 奖惩日期 | `char` | 10 | 是 | 奖惩日期 |
| 5 | `rptypeid` | 奖惩种类 | `integer` | - | 是 | 奖惩种类 |
| 6 | `rpexplain` | 说明 | `varchar2` | 1000 | 是 | 说明 |
| 7 | `rptransact` | 相关处理 | `varchar2` | 1000 | 是 | 相关处理 |
| 8 | `requestid` | requestid | `integer` | - | 是 | requestid |

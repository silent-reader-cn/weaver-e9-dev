# 泛微OA 数据表: `smsvotinghrm`

- **所属模块**: `短信模块`
- **数据库表名**: `smsvotinghrm`
- **字段总数**: `8`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | &nbsp; |
| 2 | `smsvotingid` | 对应投票id | `integer` | 0 | 是 | &nbsp; |
| 3 | `smsvotingdetailid` | 对应投票明细id | `integer` | 0 | 是 | &nbsp; |
| 4 | `userid` | 投票人 | `integer` | 0 | 是 | &nbsp; |
| 5 | `receivesms` | 投票短信内容 | `varchar2` | 1000 | 是 | &nbsp; |
| 6 | `receivedate` | 投票日期 | `varchar2` | 80 | 是 | &nbsp; |
| 7 | `receivetime` | 投票时间 | `varchar2` | 80 | 是 | &nbsp; |
| 8 | `status` | 投票是否有效 | `integer` | 0 | 是 | 0 未投 1有效 2无效 |

# 泛微OA 数据表: `smsvoting`

- **所属模块**: `短信模块`
- **数据库表名**: `smsvoting`
- **字段总数**: `17`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | &nbsp; |
| 2 | `creater` | 创建人 | `integer` | 0 | 是 | &nbsp; |
| 3 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | &nbsp; |
| 4 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | &nbsp; |
| 5 | `subject` | 主题 | `varchar2` | 800 | 是 | &nbsp; |
| 6 | `senddate` | 发送日期 | `varchar2` | 80 | 是 | &nbsp; |
| 7 | `sendtime` | 发送时间 | `varchar2` | 80 | 是 | &nbsp; |
| 8 | `enddate` | 结束日期 | `varchar2` | 80 | 是 | &nbsp; |
| 9 | `endtime` | 结束时间 | `varchar2` | 80 | 是 | &nbsp; |
| 10 | `isseeresult` | 投票后查看结果 | `integer` | 0 | 是 | 0不可查看 1可查看 |
| 11 | `status` | 状态 | `integer` | 0 | 是 | 0未开始 1正常 |
| 12 | `remark` | 详细说明 | `varchar2` | 2000 | 是 | &nbsp; |
| 13 | `smscontent` | 短信内容 | `varchar2` | 1000 | 是 | &nbsp; |
| 14 | `portno` | 无 | `varchar2` | 400 | 是 | &nbsp; |
| 15 | `hrmids` | 接收人 | `varchar2` | 2000 | 是 | &nbsp; |
| 16 | `votingcount` | 投票数 | `integer` | 0 | 是 | &nbsp; |
| 17 | `vaildvotingcount` | 有效投票数 | `integer` | 0 | 是 | &nbsp; |

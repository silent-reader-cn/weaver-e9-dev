# 泛微OA 数据表: `votingresourcetemp`

- **所属模块**: `网上调查`
- **数据库表名**: `votingresourcetemp`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `votingid` | 调查id | `integer` | - | 是 | - |
| 2 | `questionid` | 问题id | `integer` | - | 是 | - |
| 3 | `optionid` | 选项id | `varchar2` | 200 | 是 | - |
| 4 | `resourceid` | 用户id | `integer` | - | 是 | - |
| 5 | `remark` | 填空题或选择题的其他选项 | `clob` | 4000 | 是 | 填空题或选择题的其他选项 |
| 6 | `operatedate` | 操作日期 | `varchar2` | 80 | 是 | - |
| 7 | `operatetime` | 操作时间 | `varchar2` | 80 | 是 | - |

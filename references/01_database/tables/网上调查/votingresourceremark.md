# 泛微OA 数据表: `votingresourceremark`

- **所属模块**: `网上调查`
- **数据库表名**: `votingresourceremark`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `votingid` | 调查id | `integer` | - | 是 | - |
| 2 | `questionid` | 问题id | `integer` | - | 是 | - |
| 3 | `resourceid` | 选项id | `integer` | - | 是 | - |
| 4 | `useranony` | 是否匿名 | `integer` | - | 是 | - |
| 5 | `otherinput` | 其他选项输入的内容 | `varchar2` | 4000 | 是 | - |
| 6 | `operatedate` | 操作日期 | `char` | 10 | 是 | - |
| 7 | `operatetime` | 操作时间 | `char` | 8 | 是 | - |

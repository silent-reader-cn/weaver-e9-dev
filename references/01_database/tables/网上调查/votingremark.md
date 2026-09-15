# 泛微OA 数据表: `votingremark`

- **所属模块**: `网上调查`
- **数据库表名**: `votingremark`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `votingid` | 调查id | `integer` | - | 是 | - |
| 2 | `resourceid` | 人员id | `integer` | - | 是 | - |
| 3 | `useranony` | 是否匿名 | `integer` | - | 是 | - |
| 4 | `remark` | 填空题或选择题其他选项 | `varchar2` | 4000 | 是 | 填空题或选择题其他选项 |
| 5 | `operatedate` | 操作日期 | `char` | 10 | 是 | - |
| 6 | `operatetime` | 操作时间 | `char` | 8 | 是 | - |

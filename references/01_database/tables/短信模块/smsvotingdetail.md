# 泛微OA 数据表: `smsvotingdetail`

- **所属模块**: `短信模块`
- **数据库表名**: `smsvotingdetail`
- **字段总数**: `5`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | 0 | 否 | 主键id |
| 2 | `smsvotingid` | 对应投票id | `integer` | 0 | 是 | &nbsp; |
| 3 | `regcontent` | 投票选项 | `varchar2` | 80 | 是 | 投票项 |
| 4 | `remark` | 说明 | `varchar2` | 1000 | 是 | &nbsp; |
| 5 | `count` | 投票数 | `integer` | 0 | 是 | 计数 |

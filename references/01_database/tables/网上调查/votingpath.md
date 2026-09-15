# 泛微OA 数据表: `votingpath`

- **所属模块**: `网上调查`
- **数据库表名**: `votingpath`
- **字段总数**: `6`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | id | `integer` | - | 否 | - |
| 2 | `type` | 是附件还是图片 | `integer` | - | 是 | - |
| 3 | `title` | 附件标题 | `nvarchar2` | 1000 | 是 | - |
| 4 | `optionid` | 选项id | `integer` | - | 是 | - |
| 5 | `imagefileid` | 所在服务器附件表id | `integer` | - | 是 | - |
| 6 | `innershow` | 排序 | `integer` | - | 是 | - |

# 泛微OA 数据表: `info_score`

- **所属模块**: `政务应用`
- **数据库表名**: `info_score`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | - |
| 3 | `siftid` | 待编信息id | `integer` | - | 是 | - |
| 4 | `infoid` | 上报信息id | `integer` | - | 是 | - |
| 5 | `j_type` | 刊型 | `integer` | - | 是 | - |
| 6 | `j_column` | 栏目 | `integer` | - | 是 | - |
| 7 | `score` | 得分 | `float` | - | 是 | - |
| 8 | `scoredate` | 日期 | `varchar2` | 10 | 是 | - |
| 9 | `scoretime` | 时间 | `varchar2` | 8 | 是 | - |
| 10 | `scoretype` | 得分类型 | `integer` | - | 是 | 0基础采用分1加分 |
| 11 | `rewardid` | 加分项id | `integer` | - | 是 | - |
| 12 | `j_type1` | 加分指定刊型 | `integer` | - | 是 | - |
| 13 | `j_column1` | 加分指定栏目 | `integer` | - | 是 | - |
